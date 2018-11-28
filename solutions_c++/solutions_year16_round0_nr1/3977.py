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
    int a;
};

void ParseTrial(ifstream& ifs, Trial& t){
    
    ifs >> t.a;
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

void OutputResult(ostream& out, int caseNum, string s){
    out << "Case #" << caseNum << ":" << " " << s << endl;
}

void OutputResult(vector<string> ans){
    int i=0;
    for(string s : ans){
        OutputResult(std::cout, ++i, s);
    }
}

void changeBit(vector<string>& v, int i){
    REP(k, 0, v.size()){
        v[k][i] = (v[k][i] == '0') ? '1' : '0';
    }
}

void fill_mask(int m[10], ll a){
    while(a!=0){
        m[a%10]=1;
        a/=10;
    }
}

int check_mask(int m[10]){
    int ret=1;
    for(int i=0; i<10; ++i){
        ret &=m[i];
    }
    return ret;
}

string SolveTrial(const Trial& t){
    ll v = t.a;

    int mask[10];
    memset(mask, 0, sizeof(mask));

    if(v == 0) return "INSOMNIA";

    while(true){
        fill_mask(mask, v);
        if(check_mask(mask))break;
        v+=t.a;
    }
    return to_string(v);
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
        p(t.a);
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}


