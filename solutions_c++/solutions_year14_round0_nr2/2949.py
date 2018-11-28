//
//  main.cpp
//  CookieClickerAlpha
//
#include <cmath>
#include <fstream>
#include <iostream>
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


int main(int argc, const char * argv[])
{
    ofstream fo;
    ofstreamGetter("../../../outputl.txt", fo);
    fo.precision(7);
    
    // insert code here...
    ifstream fi;
    ifstreamGetter("../../../B-large.in", fi);
    
    string line;
    vector<string> line_segments;
    
    
    //get number of test cases
    int T = 0;
    getline(fi, line);
    T = stoi(line);
    
    line.clear();
    
    double ini_rate = 2;
    
    int case_cnt = 1;
    
    while (getline(fi, line)) {
        SeparateStringByDelimiter(line, ' ', line_segments);
        double C = stod(line_segments[0]);
        double F = stod(line_segments[1]);
        double X = stod(line_segments[2]);
        
        int opt_num_farms = (int)ceil((F * X-2 * C)/(F * C)) - 1;
        if (opt_num_farms < 0) {
            opt_num_farms = 0;
        }
        double duration = 0;
        for (int i = 0; i < opt_num_farms; i++) {
            duration += C/(ini_rate + i * F);
        }
        duration += X/(ini_rate + opt_num_farms * F);
        
        fo << "Case #" << case_cnt << ": " << fixed << duration << endl;
        
        case_cnt++;
        line.clear();
        line_segments.clear();
    }
    
    
    return 0;
}

