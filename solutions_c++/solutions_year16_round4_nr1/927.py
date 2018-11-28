#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<string>
#define pb push_back
using namespace std;

int T,N,R,P,S;
string sol,tsol;
map<char,string> par;
vector<string> s,ts;

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    par['R'] = "RS";
    par['S'] = "PS";
    par['P'] = "PR";
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d%d%d%d",&N,&R,&P,&S);
        int inR = R, inP = P, inS = S;
        bool ok = 1;
        for(int i=1;i<=N;++i) {
            if((R+S+P)%2 == 0 && R+S >= P && R+P >= S && P+S >= R) {
                int newR = (R+S-P)/2;
                int newP = (P+R-S)/2;
                int newS = (S+P-R)/2;
                R = newR;
                P = newP;
                S = newS;
            } else {
                ok = 0;
            }
        }
        if(!ok) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(R==1) {
            sol = "R";
        } else if(P==1) {
            sol = "P";
        } else {
            sol = "S";
        }
        for(int i=1;i<=N;++i) {
            tsol = "";
            for(auto c: sol) {
                tsol = tsol + par[c];
            }
            sol = tsol;
        }
        s.clear();
        for(int i=0;i<sol.size();++i) {
            s.pb(sol.substr(i,1));
        }
        for(int l=1;l<=N;++l) {
            ts.clear();
            for(int i=0;i<s.size();i+=2) {
                if(s[i] > s[i+1]) {
                    ts.pb(s[i+1] + s[i]);
                } else  {
                    ts.pb(s[i]+s[i+1]);
                }
            }
            s = ts;
        }
        cout<<s[0]<<"\n";
        if(inP != count(s[0].begin(),s[0].end(),'P')) cout<<" NOOOOO";
        if(inS != count(s[0].begin(),s[0].end(),'S')) cout<<" NOOOOO";
        if(inR != count(s[0].begin(),s[0].end(),'R')) cout<<" NOOOOO";

    }
    return 0;
}

