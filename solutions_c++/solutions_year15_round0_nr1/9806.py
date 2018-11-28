#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

void ReadInput(const char* filename, const char* filename2){

    std::ifstream infile(filename);
    std::ofstream outfile(filename2);

    std::string line;
    int cases=0;
    std::getline(infile, line);
    std::istringstream iss(line);
    iss >> cases;
    stringstream output;
    for (int tcase=1;tcase<=cases;tcase++){
        std::getline(infile, line);
        int smax;
        string levels;
        std::istringstream iss(line);
        if (!(iss >> smax >> levels))         break;
        if (levels.length()<smax+1)       break;
        //process test case
        vector<int> shyness;
        for (int i=0;i<=smax;i++)
            shyness.push_back(levels.at(i));

        if (smax==0){
             output<<"Case #"<<tcase<<": 0"<<endl;
            continue;
        }
        int friends=0;
        int nr_standing=shyness[0]-'0';
        for (int i=1;i<=smax;i++){
            int required=shyness[i]-'0';
            if (required>0 && i>nr_standing){
                //friends required
                friends += i-nr_standing;
                nr_standing +=friends;
            }
            nr_standing += required;
        }

        output<<"Case #"<<tcase<<": "<<friends<<endl;
    }
    outfile << output.str();
}


int main(int argc, char *argv[])
{

    ReadInput(argv[1],argv[2]);
    return 0;
}
