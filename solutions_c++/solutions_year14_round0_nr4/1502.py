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
#define READ(v,n) { FOR(i,n){double x;cin>>x;v.pb(x);} }
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
  cout.precision(15);
  int K;
  cin>>K;
  FOR(k,K){
    int n;
    cin>>n;
    vector <double> v1,v2;
    READ(v1,n);
    READ(v2,n);
    sort(all(v1));
    sort(all(v2));
    
    vector <double> v11,v22;
    v11=v1;
    v22=v2;
    int m=n;

    FOR(i,n){
      if(v11[i]<v22[i]){goto con;}
    } 
    m=n; goto skip;
    con:
    while(m){
      v11.erase(v11.begin());         
      v22.erase(v22.begin()+m-1);
      m--;
      FOR(i,m){
        if(v11[i]<v22[i]){goto n;}
      }
      break;      
      n:continue;
    }
    skip:
    
    v11=v1;
    v22=v2;
    int m2=n;
    int c=0;
    while(m2){
      int i=0;
      while(v22[i]<v11[0]){i++;if(i==m2){i=0;break;}}
      if(v11[0]>v22[i])c++;
      v11.erase(v11.begin());         
      v22.erase(v22.begin()+i);  
      m2--;      
    
    }
    
    cout<<"Case #"<<(k+1)<<": ";
    cout<<m<<" ";
    cout<<c<<endl;
    
        

  }
  return 0;
}
