#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <climits>
#define REP(i, m, n) for (int i=(int)(m); i<(int)(n); ++i)
#define REPE(i, m, n) for (int i=(int)(m); i<=(int)(n); ++i)
#define ZERO(i) memset((i), 0, sizeof(i));

//#define MYDEBUG

#ifdef MYDEBUG
#define p(_value) cout << " @" << #_value << ":" << _value << endl;
#define pv(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << _vec[_vindex] << ", "; cout << endl; }
#define pvp(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << "(" << _vec[_vindex].first << "," << _vec[_vindex].second << ")" << ", "; cout << endl; }
#else
#define p(_value) 
#define pv(_vec) 
#define pvp(_vec) 
#endif

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef unsigned long long ull;
typedef long long ll;

struct Trial{
    int deno;
    int nume;
};

Trial ParseTrial(ifstream& inputFileStream){

    Trial t;
    int i, j; char slash;    
    inputFileStream >> t.nume >> slash >> t.deno;
    if(!inputFileStream) cerr << "Read row string failed()." << endl, exit(1);
    return t;
}

void ParseProblemFile(string inputFileName, vector<Trial>& trials){
    ifstream inputFileStream(inputFileName, ios::in);
    if(!inputFileStream) cerr << "can not open file (" << inputFileName << ")." << endl, exit(1);

    int testCaseNum;
    inputFileStream >> testCaseNum;

    REP(testCaseId, 0, testCaseNum) trials.push_back(ParseTrial(inputFileStream));
}

void OutputResult(ostream& out, string s){
    static int caseNum = 1; out << "Case #" << caseNum++ << ":" << " " << s << endl;
}

void OutputResult(vector<string> ans){
    for(string s : ans) OutputResult(std::cout, s);
}

int 
gcd ( int a, int b ){
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

bool increase(int n1, int d1, int n2, int d2){
    // p(n1);
    // p(d1);
    // p(n2);
    // p(d2);
    while(d2 != d1){
        d2*=2; n2*=2;        
    }
    return n1<n2;
}

string SolveTrial(const Trial& t){
    int d = t.deno;
    int n = t.nume;
    
    if(n>=d) return "impossible";

    int div = gcd(d, n);
    d /= div;
    n /= div;

    int tmp = d;
    while(tmp%2==0){
        tmp/=2;        
    }
    if(tmp != 1) return "impossible";

    // p(n);
    // p(d);
  
    int ret = 1;
    while( increase(n, d, 1, pow(2, ret)) ){
        ret++;
    }
    return to_string(ret);
}

int main(int argc, char** argv){
    string inputFileName = (argc != 2) ? "test.in" : argv[1];

    vector<Trial> trials;
    ParseProblemFile(inputFileName, trials);

    vector<string> ans;
    for(Trial t : trials){
        static int testCase = 0; testCase++; p(testCase);
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);
    return 0;
}
