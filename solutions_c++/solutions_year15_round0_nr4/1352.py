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
    int x;
    int r;
    int c;
};

void ParseTrial(ifstream& ifs, Trial& t){    
    ifs >> t.x;
    ifs >> t.r;
    ifs >> t.c;
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

string SolveTrial(const Trial& t){
    int x=t.x;
    int r=t.r;
    int c=t.c;

    p(x);p(r);p(c);

    vector< pair<int, int> > v(4);
    v[0] =make_pair(1,1);
    v[1] =make_pair(1,2);
    v[2] =make_pair(2,3);
    v[3] =make_pair(2,4);

    int s1=min(r,c);
    int s2=max(r,c);

    if(s1 < v[x-1].first || s2 < v[x-1].second){
        return "Richard";
    }

    if(r*c%x!=0){
        return "Richard";
    }

    if(x==4 && s1==2 && s2<7) return "Richard";

    return "Gabriel";
}

int main(int argc, char** argv){
    string inputFileName;
    if(argc != 2){
        inputFileName = "as.in";
    }else{
        inputFileName = argv[1];
    }

    vector<Trial> trials;
    ParseProblemFile(inputFileName, trials);

    vector<string> ans;
    for(Trial t : trials){

        static int testCaseNum = 0;
        testCaseNum++;
        p(testCaseNum);

//        cout << "start: " << testCaseNum << endl;
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}


