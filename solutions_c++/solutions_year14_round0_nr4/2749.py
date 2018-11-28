//
//  main.cpp
//  DeceitfulWar
//

#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

//output file stream getter, no mode constraints
void ofstreamGetter(std::string path, std::ofstream &f)
{
	f.open(path);
	if (!f.is_open())
	{
		std::cout << "Err path: " << path << std::endl;
		exit(-1);
	}
}

//input file stream getter, no mode constraints
void ifstreamGetter(string path, ifstream &f)
{
	f.open(path);
	if (!f.is_open())
	{
		std::cout << "Err path: " << path << std::endl;
		exit(-1);
	}
}

void SeparateStringByDelimiter(string &input, char delimiter, vector<string>& output)
{
	//std::cout << line << endl;
	istringstream iss(input);
	string segment;
	//interpret this line
	while (getline(iss, segment, delimiter))
	{
		output.push_back(segment);
	}
}

int NaomiPointInWar(set<double> &Naomi, set<double> &Ken, int N)
{
    int KenPoint = 0;
    set<double>::iterator itn = Naomi.begin();
    for (set<double>::iterator itk = Ken.begin(); itk != Ken.end(); itk++) {
        if (*itk > *itn) {
            KenPoint++;
            itn++;
        }
        else{
            //do nothing, ken is going to find a larger wood to beat this itn
        }
    }
    return N - KenPoint;
}

int NaomiPointInDeceitfulWar(set<double> &Naomi, set<double> &Ken)
{
    int NaomiPoint = 0;
    set<double>::iterator itk = Ken.begin();
    for (set<double>::iterator itn = Naomi.begin(); itn != Naomi.end(); itn++) {
        if (*itn > *itk) {//naomi can cheat to say *itn wood is larger than Ken's heaviest wood to win 1 point by finding a smallest wood that is heavier than Ken's smallest wood
            NaomiPoint++;
            itk++;
        }
        else{//point to lose anyway
            //so do nothing, and go to next larger wood
        }
    }
    return NaomiPoint;
}

int main(int argc, const char * argv[])
{
    ofstream fo;
    ofstreamGetter("../../../output.txt", fo);
    fo.precision(7);
    
    // insert code here...
    ifstream fi;
    ifstreamGetter("../../../D-large.in", fi);
    
    string line;
    vector<string> line_segments;
    
    
    //get number of test cases
    int T = 0;
    getline(fi, line);
    T = stoi(line);
    
    line.clear();
    
    
    int case_cnt = 1;
    
    int N = 0;
    set<double> Naomi;
    set<double> Ken;
    while (getline(fi, line)) {

        N = stoi(line);
        line.clear();
        
        getline(fi, line);//read Naomi
        SeparateStringByDelimiter(line, ' ', line_segments);
        for (auto it = line_segments.begin(); it != line_segments.end(); it++) {
            Naomi.insert(stod(*it));
        }
        line.clear();
        line_segments.clear();
        
        getline(fi, line);//read Ken
        SeparateStringByDelimiter(line, ' ', line_segments);
        for (auto it = line_segments.begin(); it != line_segments.end(); it++) {
            Ken.insert(stod(*it));
        }
        line.clear();
        line_segments.clear();
        
        //processing
        int NaomiPointWar = NaomiPointInWar(Naomi, Ken, N);
        int NaomiPointDeceitfulWar = NaomiPointInDeceitfulWar(Naomi, Ken);
        
        fo << "Case #" << case_cnt << ": " << NaomiPointDeceitfulWar << " " << NaomiPointWar << "\n";
        
        
        Naomi.clear();
        Ken.clear();
        case_cnt++;
    }
    
    fo.close();
    fi.close();
    
    return 0;
}

