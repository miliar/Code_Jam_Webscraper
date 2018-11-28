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

    getInt(T);
    REP(tt,T){
        getInt(N);
        getInt(X);
        vector<int> si;
        vector<bool> done;
        REP(i,N){
            getInt(S);
            si.push_back(S);
            done.push_back(false);
        }
        sort(si.begin(), si.end());

        //get last
        int ans=0;
        while(si.size()>0){
            while(si.size()>0 && done[si.size()-1]){
                si.pop_back();
            }
            if(si.size()==0) break;
            int l = si.back();
            si.pop_back();
            vector<int> ni;
            int i =0;
            if(si.size()==0 || si[0]+l > X) {
                ans++;
            }
            else{
                int poss=-1;
                int possidx=-1;
                while(si[i]+l <= X && i < si.size()){
                    if(!done[i]){
                        poss=si[i];
                        possidx=i;
                    }
                    i++;
                }
                if(poss>-1){

                    done[possidx]=true;
                }
                ans++;
            }
        }



        cout << "Case #" << (tt+1) << ": ";
        cout << ans;
        cout << '\n';
    }
   return 0;
}
