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
#include <string.h>
#include <limits.h>

#define REP(i, m, n) for (int i=(int)(m); i<(int)(n); ++i)
#define p(_value) cout << " @" << #_value << ":" << _value << endl;
#define pv(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << _vec[_vindex] << ", "; cout << endl; }
#define pvp(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << "(" << _vec[_vindex].first << "," << _vec[_vindex].second << ")" << ", "; cout << endl; }

using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef unsigned long long ull;

#define MYDEBUG 0

struct Trial{
    int n;
    vector<string> v;
};

void ParseTrial(ifstream& inputFileStream, Trial& t){    
    inputFileStream >> t.n;
    REP(k, 0, t.n){
        string tmp;
        inputFileStream >> tmp;
        t.v.push_back(tmp);
    }
    if(!inputFileStream) cerr << "Read row string failed()." << endl, exit(1);
}

void ParseProblemFile(string inputFileName, vector<Trial>& trials){
    ifstream inputFileStream(inputFileName, ios::in);
    if(!inputFileStream) cerr << "can not open file (" << inputFileName << ")." << endl, exit(1);

    int testCaseNum;
    inputFileStream >> testCaseNum;

    REP(testCaseId, 0, testCaseNum){
        Trial t;
        ParseTrial(inputFileStream, t);
        trials.push_back(t);
    }
}

void OutputResult(ostream& out, string s){
    static int caseNum = 1;
    out << "Case #" << caseNum++ << ":" << " " << s << endl;
}

void OutputResult(vector<string> ans){
    for(string s : ans) OutputResult(std::cout, s);
}

string SolveTrial(const Trial& t){
    vector<string> v = t.v;
    vector<int> index(v.size(), 0);
    int cnt = 0;
    while(true){
        int minCons = 100000;
        int maxCons = 0;
        char prevc = '#';
        REP(i, 0, v.size()){
            int& ind = index[i];
            int cons = 0;
            char c = '/';
            if(ind >= v[i].size()){
                continue;
            }else{
                c = v[i][ind];
                ++ind;
                ++cons;
            }

            while(ind < v[i].size() && v[i][ind] == v[i][ind-1]){
                ++ind;
                ++cons;
            }

            minCons = min(cons, minCons);
            maxCons = max(cons, maxCons);

            if(i == 0){
                prevc = c;
            }else{
                if(prevc != c) return "Fegla Won";
                if(i == v.size()-1){
                    cnt += maxCons - minCons;
                }
            }

            // p(i);
            // p(minCons);
            // p(maxCons);
        }

        REP(k, 0, index.size()){
            if(index[k] >= v[k].size()) goto while_out;
        }
    }

while_out:

    REP(k, 0, index.size()){
        if(index[k] < v[k].size()) return "Fegla Won";
    }

    return to_string(cnt);
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
#if MYDEBUG
        static int testCase = 0;
        testCase++;
        p(testCase);
#endif
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);
    return 0;
}


