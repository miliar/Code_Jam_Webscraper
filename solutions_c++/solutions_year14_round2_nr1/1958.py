#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>
#include <time.h>
#include <queue>
#include <set>
#include <stack>

using namespace std;

#define PII pair<int,int>
#define MP make_pair
#define X first
#define Y second

int solve(vector<int>& vt){
    int sz = vt.size();
    int cum = accumulate(vt.begin(),vt.begin() + sz,0);
    int avg = cum/sz;
    int ret = 0,ret1;
    for (int i=0; i<sz; i++) {
        ret += abs(vt[i]-avg);
    }
    if (cum%sz) {
        for (int i=0; i<sz; i++) {
            ret1+=abs(vt[i]-avg-1);
        }
        ret = min(ret,ret1);
    }
    return ret;
    
}


int main()
{
    int i,T;
    cin>>T;
    for (i=1; i<=T; i++) {
        int j,N,k,mind,mcnt;
        cin>>N;
        vector<string> vs,mod;
        string inp;
        vector<map<int,int> > dp;
        bool imp = false;
        for (j=0; j<N; j++) {
            cin>>inp;
            vs.push_back(inp);
            string smod="";
            smod+=inp[0];
            map<int,int> cur = map<int,int>();
            mind = 0;
            mcnt = 1;
            for (k=1; k<(int)inp.size(); k++) {
                if (inp[k]==inp[k-1]) {
                    mcnt++;
                }
                else{
                    cur[mind] = mcnt;
                    mind++;
                    mcnt = 1;
                    smod += inp[k];
                }
            }
            mod.push_back(smod);
            cur[mind] = mcnt;
            dp.push_back(cur);
        }
        for (j=1; j<N; j++) {
            if (mod[j]!=mod[j-1]) {
                imp = true;
            }
        }
        if (imp) {
            cout<<"Case #"<<i<<": "<<"Fegla Won"<<endl;
        }
        else{
            int ans = 0;
            for (auto mi=dp[0].begin(); mi!=dp[0].end(); mi++) {
                
                vector<int> vt=vector<int>();
                for (j=0; j<N; j++) {
                    //mn = min(dp[j][mi->first],mn);
                    vt.push_back(dp[j][mi->first]);
                }
                
                ans += solve(vt);
                
            }
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
        
    }
    
    
    
    return 0;
}