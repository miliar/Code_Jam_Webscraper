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
    cout.precision(15);
  int K;
  cin>>K;
  FOR(k,K){
    ll N, p, q, r, s;
    cin>>N>>p>>q>>r>>s;
    vector <ll> v;
    FOR(i,N){v.pb((i*p+q)%r+s);}    
    vector <ll> vs;
    vs.pb(0);
    ll sum=0;
    FOR(i,N){sum+=v[i];vs.pb(sum);}
    
    
    //FOR(i,sz(vs)){cerr<<vs[i]<<",";}cerr<<endl;
    ll mm=-1;
    FOR(i,N+1){
        ll rem = vs[N] - vs[i];
        int b = lower_bound(all(vs),rem/2+vs[i])-vs.begin();
        ll mmm=-1;
        if(b<=N) mmm=max(vs[i],max(vs[b]-vs[i],vs[N]-vs[b]));
        if(mm==-1 || mmm<mm){mm=mmm;}
        if(b+1<=N) mmm=max(vs[i],max(vs[b+1]-vs[i],vs[N]-vs[b+1]));        
        if(mm==-1 || mmm<mm){mm=mmm;}        
        if(b-1>=0 && b-1<=N) mmm=max(vs[i],max(vs[b-1]-vs[i],vs[N]-vs[b-1]));        
        if(mm==-1 || mmm<mm){mm=mmm;}        

//        cerr<<i<<"."<<b<<"."<<mmm<<endl;
    }
    
    
    
    cout<<"Case #"<<(k+1)<<": ";
    cout<<1-((double)mm/(double)vs[N])<<endl;
    nextcase: 
    continue;      
  }
  
  
  end:
  return 0;
}
