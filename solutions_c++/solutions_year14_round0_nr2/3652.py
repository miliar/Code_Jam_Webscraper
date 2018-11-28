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

static const double BASE = 2.0;

double buyNextFarm( double salary, double C, double F, double X, double time){
    if (X < C) return X / salary;

    // cookie=C
    double time0 = C/salary;
    // not to buy next farm
    double time1 = (X - C) / salary;
    // buy next farm
    double new_salary = salary + F;
    double time2 = X / new_salary;

    // GOAL
    if (time1 < time2) return time + X/salary;

    // BUY FARM
    return buyNextFarm( new_salary, C, F, X, time+time0);
}

double solve(vector<double> inputs)
{
    assert( inputs.size()==3 && "ERROR:INPUT SIZE WRONG");

    double C = inputs[0];
    double F = inputs[1];
    double X = inputs[2];

    double salary = BASE;
    int time = 0;

    double answer = buyNextFarm(salary, C, F, X, time);

    return answer;
}

int main(int argc, char ** argv)
{
    assert(argc==2 && "Usage ./a.out <input file name>");

    ifstream file(argv[1]);
    int CASE_NUM = loadFromLine(file)[0];

    for (int lineNum = 0; lineNum<CASE_NUM; lineNum++)
    {
        vector<double> inputs;
        inputs = loadFromLine(file); // C F X

        double result = solve(inputs);

        cout << "Case #" << lineNum+1 << ": " << fixed << setprecision(7) << result << endl;
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
