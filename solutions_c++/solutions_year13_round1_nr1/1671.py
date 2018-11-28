/*...........
..N.I.K.A....
..L.O.S.A....
...........*/
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#define Pi 3.14159265358
#define fi first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
long long n, m, k, i, j, T, t, r, ti, R=1, rr=1, res;
main(){
       freopen("IA.in","r",stdin);
       freopen("IA.out","w",stdout);
       cin>>T;
       for(i=1;i<=T;i++){
                         res=0;
                         cin>>r;
                         cin>>t;
                         R=r;
                         rr=r+1;
                         ti=t;
                         while(true)
                         {
                          if(rr*rr-R*R<=ti){
                                              res++;
                                              ti-=rr*rr-R*R;
                                              R+=2;
                                              rr+=2;
                                              }
                          else{
                               break;
                               }
                          } 
                          cout<<"Case #"<<i<<":"<<" "<<res<<endl;
                         }
       //system("pause");
       }
