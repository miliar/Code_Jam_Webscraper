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
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator
#define Tree int ind, int L, int R
#define Left 2*ind,L,(L+R)/2
#define Right 2*ind+1,(L+R)/2+1,R
using namespace std;
string s;
int X, R, C, t;
main(){
       freopen("C.in","r",stdin);
       freopen("C.out","w",stdout);
       cin>>t;
       for(int I=1;I<=t;I++)
        {
         cin>>X>>R>>C;
         if (R > C) swap(R,C);
         if(X==1){  cout<<"Case #"<<I<<": GABRIEL"<<endl; continue; }
         if(X==2)
          {
           if((R*C)%2==1){  cout<<"Case #"<<I<<": RICHARD"<<endl; continue; }
           cout<<"Case #"<<I<<": GABRIEL"<<endl;
           continue;
          }
         if(X==3)
          {
           if(R >= 2 && (R*C)%3 == 0)cout<<"Case #"<<I<<": GABRIEL"<<endl;
           else cout<<"Case #"<<I<<": RICHARD"<<endl;
          }
         if(X==4)
          {
           if(R >= 3 && (R*C)%4 == 0)cout<<"Case #"<<I<<": GABRIEL"<<endl;
           else cout<<"Case #"<<I<<": RICHARD"<<endl;
          }
        }
       }
