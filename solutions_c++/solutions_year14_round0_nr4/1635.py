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

int main()
{
   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

   getInt(T);
     REP(tt,T){
       getInt(N);
       deque<double> naomi;
       deque<double> ken;
       REP(i,N) {
           getDouble(nn);
           naomi.push_back(nn);
       }
       REP(i,N) {
           getDouble(kk);
           ken.push_back(kk);
       }
       sort(naomi.begin(), naomi.end());
       sort(ken.begin(), ken.end());

       int k = 0;
       int deceit=0;
       int war = 0;

       REP(n,N){
           if(naomi[n]>ken[k]){
               k++;
               deceit++;
           }
       }
       k=N-1;
       REP(n,N){
           if(naomi[N-1-n]>ken[k]){
               war++;
           }
           else{
               k--;
           }
       }
       cout << "Case #" << (tt+1) << ": " << (deceit) << " "<<war << '\n';
     }

   /*
     C:  getInt(T);
    REP(tt,T){
        cout << "Case #" << (tt+1) << ":\n";
        getInt(R);getInt(C);getInt(M);

      D: getInt(T);
      REP(tt,T){
        getInt(N);
        REP(i,N) getDouble(naomi)
        REP(i,N) getDouble(ken)
     */
/*
    getInt(T);
    REP(tt,T){
        cout << "Case #" << (tt+1) << ":\n";
        getInt(R);getInt(C);getInt(M);
        int S = R*C-M;
        if(R==1 || C==1){
            if(R==1){
                REP(c,C-1){
                    cout << (c<M ? '*':'.');
                }
                cout << "c\n";
            } else if(C==1){
                REP(r,R-1){
                    cout << (r<M ? "*\n":".\n");
                }
                cout << "c\n";
            }
        }
        else if(R==2 || C==2){
            if(R==2){
                if(S==2 || (S>1 && S%2!=0)) cout << "Impossible\n";
                else if(S==1){
                        REP(c,C){
                            cout << "*";
                        }
                        cout <<'\n';
                        REP(c,C-1){
                            cout << "*";
                        }
                        cout << "c\n";
                }
                else{
                        REP(c,C-1){
                            if(c<M/2) cout << "*";
                            else cout << ".";
                        }
                        cout <<".\n";
                        REP(c,C-1){
                            if(c<M/2) cout << "*";
                            else cout << ".";
                        }
                        cout <<"c\n";
                }
            }
        }

        if(R*C==1) cout << "Case #" << (tt+1) << ":\n" << ".\n";

        //bool ans = (K+1) % (int)pow(2,N) == 0;
        cout << setprecision(100) << "Case #" << (tt+1) << ": " << (t) << '\n';
    }
*/

    return 0;
}
