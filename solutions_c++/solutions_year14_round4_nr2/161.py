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

#define vs vector<string>
#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define sqr(x) ((x)*(x))
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define READ(v,n) { FOR(i,n){int x;cin>>x;v.pb(x);} }
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
  cin>>K;
  FOR(k,K){
    int n;
    cin>>n;
    vi v;
    READ(v,n);
    int mm=999999999;
    int b=0;
    int bi=0;
    
    int num=0;
    
    while(sz(v)!=0){
        int mi=0;
        int mm=-1;
        FOR(i,sz(v)){
            if(mm==-1 || v[i]<mm){mm=v[i];mi=i;}
        }
        num+=min(mi,sz(v)-mi-1);
        v.erase(v.begin()+mi);
        //cerr<<num<<endl;
        //FOR(i,sz(v))cerr<<v[i];cerr<<endl;
    }
    cout<<"Case #"<<(k+1)<<": ";
    cout<<num<<endl;
    nextcase: 
    continue;      
  }
  
  
  end:
  return 0;
}
