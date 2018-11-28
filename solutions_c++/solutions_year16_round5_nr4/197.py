#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long

int L, N;
string B;
string G[100];

string S1, S2;
char C[] = {'0', '1', '?'};

string curS = "";
char cv = '0';
map<string, string> all;
string order;

void eval(char c) {
    if (c == '0' || c == '1') cv = c;
    else curS += cv;
}

void genAll(int a = 0, int b = 0) {
    if (a < S1.size()) {
        string s = curS;
        char v = cv;
        order += '0';

        eval(S1[a]);
        genAll(a+1, b);
        swap(s, curS);
        cv = v;
        order.pop_back();
    }

    if (b < S2.size()) {
        string s = curS;
        order.push_back('1');
        char v = cv;
        eval(S2[b]);
        genAll(a, b+1);
        swap(s, curS);
        cv = v;
        order.pop_back();
    }

    if (a == S1.size() && b == S2.size()) {
        all[curS] = order;
    }
}

void evalAll() {
    if (all.count(B) == 1) return;

    for (int i=0;i<N;++i) {
        if (all.count(G[i]) != 1) return;
    }

    printf("Possible solution is: %s %s\n", S1.c_str(), S2.c_str());

    for (int i=0;i<N;++i) {
        printf("  %s = %s\n", G[i].c_str(), all[G[i]].c_str());
    }
}
    

void gen(int which, int pos=0) {
    if (pos != 0) {
        if (which == 0) {
            gen(1);
        } else {
            genAll();
            evalAll();
            all.clear();
        }
    }

    if (pos > 4) return;


    string& s = which ? S1 : S2;
    
    for (int i =0;i<3;++i) {
        s += C[i];
        
        gen(which, pos+1);

        s.resize(s.size()-1);
    }
}


int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        cin>>N>>L;
        for (int i=0;i<N;++i) cin >> G[i];
        cin>>B;

        /*
        S1="";S2="";
        gen(0);
        */

        bool good = true;
        for (int i=0;i<N;++i) {
            if(G[i] == B) good = false;
        }

        string A = "?";
        string O = "0";
        for (int i=0;i<L-1;++i) {
            A += "0?";
            O += "1";
        }

        string ans = good ? A + " " + O : "IMPOSSIBLE"; 

        printf("Case #%d: %s\n", t, ans.c_str());
    }
}
