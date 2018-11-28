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
//Sometimes I use boost - rules mean I need to say where it comes from:
//Boost library available at http://www.boost.org/

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
		int need = 0;
		int tot = 0;
		getInt(S);
		REP(s,S+2){
			getChar(c);
			if(s==0) continue;
			if(s==1){
				tot+=c-48;
			} else {
				if(s-1 > tot){
					need += s-1 -tot;
					tot = s-1;
				}
				tot+=c-48;
			}
		}
        cout << "Case #" << (tt+1) << ": ";
        cout << need;
        cout << '\n';
    }
    return 0;
}
