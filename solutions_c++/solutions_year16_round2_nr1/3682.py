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

// #define MYDEBUG

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
    string a;
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

int carray[26];
const string snum[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool zero(int arr[]){
    int c=0;
    for(int i=0; i<26; ++i) c+= arr[i];
    return (c==0) ? true : false;
}

bool decarr(int arr[], string s){    
    bool ret=true;
    for(char c : s){
        arr[c-'A']--;
        if(arr[c-'A'] < 0) ret=false;
    }
    return ret;
}

void fillarr(int arr[], string& s){
    memset(arr, 0, sizeof(arr));
    for(auto c:s){
        arr[c-'A']++;
    }
}

void concatstr(VI& v, string& os){
    sort(v.begin(), v.end());    
    for(int i=0; i<v.size(); ++i) os += to_string(v[i]);
}

bool df(int num, VI& v){
    
    if(num==10){
        return zero(carray) ? true : false;
    }

    bool ret;
    ret = df(num+1, v);
    if(ret) return true;

    string numstr = snum[num];
    int backarr[26]; VI backv;
    memcpy(backarr, carray, sizeof(backarr)); backv = v;
    while(true){
        if(false == decarr(carray, numstr)){
            break;
        }
        
        v.push_back(num);
        ret = df(num+1, v);
        if(ret)return true;
    }

    memcpy(carray, backarr, sizeof(backarr));
    v = backv;
    
    return false;
}

string SolveTrial(const Trial& t){
    string s = t.a;

    fillarr(carray, s);
    
    VI v;
    df(0, v);

    string ret;
    concatstr(v, ret);
    
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
        p(t.a);
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}


