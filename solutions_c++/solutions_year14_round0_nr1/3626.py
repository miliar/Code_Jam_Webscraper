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

using namespace std;

vector<string> split(const string _s, const string del);
vector<int> loadFromLine(ifstream& file);
vector< vector<int> > loadFromLines(ifstream& file, int rows);
int toInt(string s) { int r = 0; istringstream ss(s); ss >> r; return r; }
string toStr(int n) { ostringstream ss; ss << n; return ss.str(); }

string solve(int first_answer, vector< vector<int> > arrangement1, int second_answer, vector< vector<int> > arrangement2)
{
    string ret;
    int first_idx = first_answer - 1;
    int second_idx = second_answer - 1;

    map<int, bool> checker;
    for(uint cols=0; cols<4; cols++){
        checker.insert(pair<int,bool>(arrangement1[first_idx][cols], true));
    }

    vector<int> answers;
    for(uint cols=0; cols<4; cols++){
        int num = arrangement2[second_idx][cols];
        if (checker[num]) answers.push_back(num);
    }

    if(answers.size() == 1) return toStr(answers[0]);
    if(answers.size() > 1) return "Bad magician!";
    if(answers.empty()) return "Volunteer cheated!";

    return ret;
}

int main(int argc, char ** argv)
{
    assert(argc==2 && "Usage ./a.out <input file name>");

    ifstream file(argv[1]);
    static const int CASE_NUM = loadFromLine(file)[0];

    for (int lineNum = 0; lineNum < CASE_NUM; lineNum++) {

        int first_answer = loadFromLine(file)[0];
        vector< vector<int> > arrangement1 = loadFromLines(file, 4);
        int second_answer = loadFromLine(file)[0];
        vector< vector<int> > arrangement2 = loadFromLines(file, 4);

        string result;
        result = solve( first_answer, arrangement1, second_answer, arrangement2);

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

vector<int> loadFromLine(ifstream& file){
    string line;
    getline(file, line);
    vector<string> tmp  = split(line, " ");
    vector<int> args;
    for (uint i=0; i<tmp.size(); i++) args.push_back(toInt(tmp[i]));
    return args;
}

vector< vector<int> > loadFromLines(ifstream& file, int rows){
    vector< vector<int> > matrix;
    for(int line = 0; line < rows; line++){
        vector<int> rows = loadFromLine(file);
        matrix.push_back(rows);
    }
    return matrix;
}

