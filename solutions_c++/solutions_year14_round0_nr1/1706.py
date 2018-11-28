#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cstring>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define sqr(x) ((x)*(x))
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define READ(v,n) { FOR(i,n){ll x;cin>>x;v.pb(x);} }
#define FREAD(v,n) { FOR(i,n){int x;in>>x;v.pb(x);} }
#define WRITE(v) "";FOR(i,sz(v))cout<<v[i]<<" ";cout
#define FWRITE(v) "";FOR(i,sz(v))out<<v[i]<<" ";out
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ppb pop_back
typedef long long ll;
typedef unsigned long long ull;
using namespace std;



int main(void){
  int K;
  int res=-1;
  cin>>K;
  FOR(k,K){
           cout<<"Case #"<<(k+1)<<": ";
           res=-1;
           int x;
           cin>>x;
           int y;
           FOR(i,(x-1)*4){cin>>y;}         
           vi v;
           READ(v,4);
           FOR(i,(4-x)*4){cin>>y;}         

           cin>>x;
           FOR(i,(x-1)*4){cin>>y;}         
           vi v2;
           READ(v2,4);
           FOR(i,(4-x)*4){cin>>y;}         
           
           FOR(i,4){
           FOR(j,4){
             if(v[i]==v2[j]){
               if(res!=-1){cout<<"Bad magician!"<<endl; goto next;}
               res=v[i];
             }        
           }}
           if(res==-1){cout<<"Volunteer cheated!"<<endl; goto next;}
           cout<<res<<endl;
    next: continue;
  }
  return 0;
}
