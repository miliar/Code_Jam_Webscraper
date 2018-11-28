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

#define MYDEBUG

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
    int N, J;
};

void ParseTrial(ifstream& ifs, Trial& t){
    ifs >> t.N;
    ifs >> t.J;
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

bool isPrime(string s, int d, VI& div){
    ll v=0;    
    for(int i=0; i<s.size(); ++i){
        v*=d;
        v+=s[i] - '0';  
    }

    cout << s << " " << d << " " << v << endl;

    for(ll j=2; j*j<v; ++j){
        if(v%j == 0){
            div.push_back(j);
            return false;
        }
    }
    return true;
}

string SolveTrial(const Trial& t){
    int N = t.N, J = t.J;
    ll ma = 1<<N;

    int found = 0;
    ostringstream os;
    for(ll i=(1<<N-1); i<(1<<N); ++i){

        ll tmp=i; string s; 
        while(tmp){
            s.insert(0, to_string(tmp%2));
            tmp/=2;
        }

        if(s[0]!='1' || s[s.size()-1]!='1') continue;

        bool ok=true; VI div;
        for(int k=2; k<=10; ++k){

            ll v=0;
            for(int j=0; j<s.size(); ++j){
                v*=k;
                v+=s[j]-'0';
            }

            if(isPrime(s, k, div)){
                ok=false; break;
            }
        }

        if(ok){
            os << "\n" << s;
            for(int m=0; m<div.size(); ++m){
                os << " " << div[m];
            }

            found++;
            if(found == J) break;
        }
    }

    p(found);
    return os.str();
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
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}


