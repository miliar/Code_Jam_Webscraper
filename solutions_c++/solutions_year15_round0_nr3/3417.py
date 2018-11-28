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

//i2, j3, k4
int mlt(int a, int b){
	if(abs(a)==1) return a*b;
	if(abs(b)==1) return a*b;
	if(abs(a)==abs(b)) return (a/abs(a))*(b/abs(b))*-1;
	if(abs(a)==2 && abs(b)==3) return (a/abs(a))*(b/abs(b))*4;
	if(abs(a)==2 && abs(b)==4) return (a/abs(a))*(b/abs(b))*-3;
	if(abs(a)==3 && abs(b)==2) return (a/abs(a))*(b/abs(b))*-4;
	if(abs(a)==3 && abs(b)==4) return (a/abs(a))*(b/abs(b))*2;
	if(abs(a)==4 && abs(b)==2) return (a/abs(a))*(b/abs(b))*3;
	if(abs(a)==4 && abs(b)==3) return (a/abs(a))*(b/abs(b))*-2;
}

int ppow(int a, int x)
{
    if(x==0) return 1;
    if(x<0) return 1;
    int r=1;

    while ( x ) {
        if ( (x & 1) == 1 ){
            r = mlt(a,r);
        }

        x >>= 1;
		a = mlt(a,a);
	}

 return r;
}

int getval(char c){
if(c=='i') return 2;
			if(c=='j') return 3;
			if(c=='k') return 4;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int ans =0;
    getInt(T);
	
    REP(tt,T){
		getInt(L);getInt(X);
		bool isposs=false;
		getString(ss);
		if(L==1) {
			getString(s);
		} else {
			VI chaars;
			int val =0;
			REP(l,L){
			  getChar(c);
			  val = getval(c);
			  chaars.push_back(val);
			}
			
			bool isI=false;
			bool isJ =false;
			val = 1;
			REP(x,X){
			REP(l,L){
				if(val==2 && !isI) {
					isI = true;
				} else if(isI && val==4){
					isJ=true;
				}
				val = mlt(val, chaars[l]);
			}
			}
			
			if(val==-1 && isJ) isposs = true;
		}
		/*
		VI Ps;
		getInt(D);
		REP(d,D){
			getInt(P);
			Ps.push_back(P);
		}
		sort(Ps.begin(), Ps.end());
		VI cmins;
		cmins.push_back(Ps.back());
		int time = 0;
		while(Ps.back()>1){
			int lst = Ps.back();
			int cmin = 0;
			if(Ps.size()>1){
				if(Ps.back() != Ps.end()[-2]){
					Ps.pop_back();
					cmin++;
					Ps.push_back(lst/2);
					Ps.push_back((lst+1)/2);
				} else {
					while(Ps.back()==lst){
						Ps.pop_back();
						cmin++;
						Ps.push_back(lst/2);
						Ps.push_back((lst+1)/2);
					}
				}		
			} else {
				Ps.pop_back();
				cmin++;
				Ps.push_back(lst/2);
				Ps.push_back((lst+1)/2);
			}
			
			time+=cmin;
			sort(Ps.begin(), Ps.end());
			cmins.push_back(time+Ps.back());
		}
		sort(cmins.begin(),cmins.end());*/
        cout << "Case #" << (tt+1) << ": ";
        cout << (isposs ? "YES" : "NO");
        cout << '\n';
    }
    return 0;
}
