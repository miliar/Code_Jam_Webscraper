#define __STDC_LIMIT_MACROS
#include <iostream>
#include <iterator>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <list>
#include <time.h>
#include <bitset>
#include <algorithm>
#include <stdint.h>
#include <limits.h>
#include <iomanip>
#include <set>

#define rep(i,a,b) for(int i = a; i < b; ++i)
#define REP(i,n) rep(i,0,n)
#define getInt(i) int i;scanf("%d",&i)
#define getDouble(i) double i;scanf("%lf",&i)
#define getUll(i) ull i;scanf("%llu",&i)
#define getLl(i) ll i;scanf("%lld",&i)
#define getChar(c) char c; scanf("%c", &c);
#define getString(s) std::string s;std::getline(cin, s);
#define getWord(w) char w[100]; scanf("%s",w);
#define newLine(tmp) std::getline(cin, tmp);
#define sq(x) ((x)*(x))
#define mset(x,v) memset(x,v,sizeof(x))
#define chkC(x,n) (x[n>>6]&(1<<((n>>1)&31)))
#define setC(x,n) (x[n>>6]|=(1<<((n>>1)&31)))
#define __STDC_LIMIT_MACROS

using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

int main()
{
   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

    getInt(T);
    REP(tt,T){
        getInt(r1);
        set<int> poss;
        REP(qq,4){
            REP(ss,4){
                getInt(x);
                if(qq+1==r1){
                    poss.insert(x);
                }
            }
        }
        getInt(r2);
        vector<int> act;
        REP(qq,4){
            REP(ss,4){
                getInt(y);
                if(qq+1==r2 && poss.find(y)!=poss.end()) act.push_back(y);
            }
        }

        if(act.size()==0) cout << "Case #" << (tt+1)  << ": Volunteer cheated!\n";
        else if(act.size()>1) cout << "Case #" << (tt+1)  << ": Bad magician!\n";
        else cout << "Case #" << (tt+1)  << ": " << act[0] << "\n";


        //bool ans = (K+1) % (int)pow(2,N) == 0;
        //cout << "Case #" << (tt+1) << ": " << (g) << '\n';
    }


    return 0;
}
