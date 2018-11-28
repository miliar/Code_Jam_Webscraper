#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <string.h>
#include <limits.h>

//#define MYDEBUG

#define REP(i, m, n) for (int i=(int)(m); i<(int)(n); ++i)

#ifdef MYDEBUG
#define p(_value) cout << "@" << #_value << ":" << _value << endl;
#define pv(_vec) { cout << "@" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << _vec[_vindex] << ", "; cout << endl; }
#else
#define p(_value) 
#define pv(_vec) 
#endif


using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef unsigned long long ull;
typedef long long ll;

struct Trial{
    string s;
};

void ParseTrial(ifstream& ifs, Trial& t){
    ifs >> t.s;
    if(!ifs){
        cerr << "Read row string failed()." << endl;
        exit(1);
    }
}

void ParseProblemFile(string inputFileName, vector<Trial>& trials){
    // Open input file.
    ifstream inputFileStream(inputFileName, ios::in);
    if(!inputFileStream){
        cerr << "can not open file (" << inputFileName << ")." << endl;
        exit(1);
    }

    // Read the number of test case.
    int testCaseNum;
    inputFileStream >> testCaseNum;

    // Read all the input
    REP(testCaseId, 0, testCaseNum){
        Trial t;
        ParseTrial(inputFileStream, t);
        trials.push_back(t);
    }
}

void OutputResult(vector<string> ans){
    int i=0;
    for(string s : ans){
        std::cout << "Case #" << ++i << ":" << " " << s << endl;
    }
}

void flip(string& s){
    for(int i=0; i<s.size(); ++i){
        s[i] = (s[i]=='-') ? '+' : '-';
    }
}

string SolveTrial(const Trial& t){
    string s = t.s;
    reverse(s.begin(), s.end());
    int ret=0;
    for(int i=0; i<s.size(); ++i){
        if(s[i]=='-'){
            flip(s);
            ret++;
        }
    }
    return to_string(ret);
}

int main(int argc, char** argv){
    string inputFileName;
    if(argc != 2){
        inputFileName = "test.in";
    }else{
        inputFileName = argv[1];
    }

    vector<Trial> trials;
    ParseProblemFile(inputFileName, trials);

    vector<string> ans;
    for(Trial t : trials){

        static int testCaseNum = 0;
        testCaseNum++;
        p("start:");
        p(testCaseNum);        
        p(t.s);
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}


