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
    int n;
    VI v;    
};

void ParseTrial(ifstream& ifs, Trial& t){    
    ifs >> t.n;
    REP(i, 0, t.n){
        int tmp;
        ifs >> tmp;
        t.v.push_back(tmp);
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

string SolveTrial(const Trial& t){
    int n=t.n;
    VI v=t.v;
    int sum=0;
    REP(i, 0, n-1){        
        int d=v[i]-v[i+1];
        if(d>0){
            sum+=d;
        }
    }    

    int i=0, j=10000; int sum2=INT_MAX;
    while(i<j){
        
        int k=(i+j)/2;
        bool ok=true;
        int tmp=0;
        REP(p, 0, n-1){
            int d=v[p]-v[p+1];
            if(d>0){
                if(d>k){
                    ok=false;
                    break;
                }                
            }
            tmp+=min(k, v[p]);
        }
        
        if(ok){
            if(sum2 > tmp){
                p(k);
                sum2 = tmp;
            }
            j=k;            
        }else{
            i=k+1;
        }
    }

    string ret = to_string(sum) + " " + to_string(sum2);
    return ret;
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


