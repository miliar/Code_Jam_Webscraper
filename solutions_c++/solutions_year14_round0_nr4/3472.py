#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cassert>
#include <iomanip>

using namespace std;

vector<string> split(const string _s, const string del);
vector<double> loadFromLine(ifstream& file);
int toInt(string s) { int r = 0; istringstream ss(s); ss >> r; return r; }
double toDouble(string s) { double r = 0; istringstream ss(s); ss >> r; return r; }
string toStr(int n) { ostringstream ss; ss << n; return ss.str(); }
string dToStr(double n) { ostringstream ss; ss << n; return ss.str(); }

int warpoints(int block_num, vector<double> naomi_blocks, vector<double> ken_blocks){
    int ken_points = 0;

    uint j=0;
    for(uint i=0; i<naomi_blocks.size(); i++){
        for(; j<ken_blocks.size(); j++){
            if( naomi_blocks[i] < ken_blocks[j]){
                remove(naomi_blocks.begin(), naomi_blocks.end(), naomi_blocks[i]);
                ken_points++;
                if( j == ken_blocks.size() - 1 ) return block_num - ken_points;
            }
        }
    }

    return block_num - ken_points;
}

int dwarpoints(int block_num, vector<double> naomi_blocks, vector<double> ken_blocks){
    vector<int> naomi_points;

    // induce big cards from ken
    for(uint i=0; i<naomi_blocks.size(); i++){

        int last_blocks = ken_blocks.size();
        int possible_point = last_blocks - warpoints(last_blocks, ken_blocks, naomi_blocks);
        naomi_points.push_back(possible_point);

        if( naomi_blocks.front() < ken_blocks.back()) break;
        remove(naomi_blocks.begin(), naomi_blocks.end(), naomi_blocks.front());
        remove(ken_blocks.begin(), ken_blocks.end(), ken_blocks.back());
    }

    return *max_element(naomi_points.begin(), naomi_points.end());
}


string solve(int block_num, vector<double> naomi_blocks, vector<double> ken_blocks)
{
    sort(naomi_blocks.begin(), naomi_blocks.end());
    sort(ken_blocks.begin(), ken_blocks.end());

    // LOSE
    if(naomi_blocks.back() < ken_blocks.front()) return "0 0";

    // toldNaomi > chosenKen toldNaomi != chosenKen
    int naomi_war_point = warpoints(block_num, naomi_blocks, ken_blocks);
    int naomi_dwar_point = dwarpoints(block_num, naomi_blocks, ken_blocks);
    ostringstream ss;
    ss << naomi_dwar_point << " " << naomi_war_point;
    return ss.str();
}

int main(int argc, char ** argv)
{
    assert(argc==2 && "Usage ./a.out <input file name>");

    ifstream file(argv[1]);
    int CASE_NUM = loadFromLine(file)[0];

    for (int lineNum = 0; lineNum<CASE_NUM; lineNum++)
    {
        int num_of_blocks = loadFromLine(file)[0];
        vector<double> naomi_blocks = loadFromLine(file);
        vector<double> ken_blocks = loadFromLine(file);

        string result = solve(num_of_blocks, naomi_blocks, ken_blocks);

        cout << "Case #" << lineNum+1 << ": " << result << endl;
    }

    return 0;
}

vector <string> split(const string _s, const string del)
{
    vector <string> ret;
    string s = _s;

    while (!s.empty())
    {
        size_t pos = s.find(del);
        string sub = "";
        sub = s.substr(0, pos);
        ret.push_back(sub);
        if (pos != string::npos)
        pos += del.size();
        s.erase(0, pos);
    }

    return ret;
}

vector<double> loadFromLine(ifstream& file){
    string line;
    getline(file, line);
    vector<string> tmp  = split(line, " ");
    vector<double> args;
    for (uint i=0; i<tmp.size(); i++) args.push_back(toDouble(tmp[i]));
    return args;
}
