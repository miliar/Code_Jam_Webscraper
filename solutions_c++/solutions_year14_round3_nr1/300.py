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
#include <deque>

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
typedef vector<int> VI;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int ans =0;
    getInt(T);
    REP(tt,T){
        ull P=0; ull Q=0;
        scanf("%llu/%llu",&P ,&Q);
        cout << "Case #" << (tt+1) << ": ";



        if(P==0) cout << "impossible";
        else if(Q==1) cout << "0";
        else if(Q%2!=0) cout << "impossible";
        else {
            //first find power of denom

            int ans = 0;
            ull newQ = Q;
            while(newQ%2==0){
                newQ=newQ/2;
                ans++;
            }
            if(P%newQ!=0) cout << "impossible";
            //else if(P/(Q+0.0)>=0.5) cout << "1";
            else{
                P=P/newQ;
                while(P/2 > 0){
                    P=P/2;
                    ans--;
                }
                cout << ans;
            }
        }


        cout << '\n';
    }
    return 0;
}
