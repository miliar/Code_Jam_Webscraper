#include <vector>
#include <iterator>
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
    vector< vector<int> > v;
};

void ParseTrial(ifstream& ifs, Trial& t){
    
    ifs >> t.n;
    t.v = vector< vector<int> >(t.n*2-1, vector<int>(t.n, 0) );

    for(int i=0; i<t.n*2-1; i++){
        for(int j=0; j<t.n; j++){
            ifs >> t.v[i][j];
        }
    }

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


void extractAndSort(int i, vector< vector<int> >& v1, vector< vector<int> >& v2, vector< vector<int> >& vv){

    for(int k=0; k<vv.size(); ++k){
        p(k);
        if(1<<k & i){
            v1.push_back(vv[k]);
        }else{
            v2.push_back(vv[k]);
        }
    }
    
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
}

bool verify(vector< vector<int> >& v1, vector< vector<int> >& v2, vector<int>& m){

    p(v1.size());
    p(v1[0].size());

    // create
    vector< vector<int> > v11;
    for(int i=0; i<v1.size(); ++i){
        VI tmp;
        for(int j=0; j<v1.size(); ++j){
            tmp.push_back(v1[j][i]);
        }
        v11.push_back(tmp);
    }

    // compare
    VI check(v1.size(), 0);
    for(VI a : v2){
        for(int i=0; i<v11.size(); ++i){
            if(a == v11[i]){
                check[i]=1;
            }
        }
    }

    int cc = 0;
    for(int i=0; i<check.size(); ++i){
        if(check[i] == 0){
            m=v11[i];
        }else{
            ++cc;
        }
    }
    
    return (cc==v1.size()-1) ? true : false;
}

string concatVector(vector<int>& v){
    stringstream ss;
    copy(v.begin(), v.end(), std::ostream_iterator<int>(ss, " "));
    return ss.str();
}

string SolveTrial(const Trial& t){
    int n = t.n;
    const int ln = 2*n-1;
    vector< vector<int> > vv = t.v;
    
    // loop for list
    string ret;    
    for(int i=0; 1<<ln; ++i){
        if(__builtin_popcount(i) != n) continue;

        // create and sort vector
        vector< vector<int> > v1, v2;
        extractAndSort(i, v1, v2, vv);

        // verify and find missed.
        vector<int> m;
        if(true == verify(v1, v2, m)){
            ret = concatVector(m);
            break;
        }
    }
    return ret;
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


