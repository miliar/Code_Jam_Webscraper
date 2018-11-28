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
#include <string>

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
    int m,n;
    cin>>m>>n;
    vs v;
    FOR(i,m){string s;cin>>s;v.pb(s);}
    vi w;
    int resnum=0;
    FOR(i,m){w.pb(0);}
    int b=-1;
    
    while(true){
        int num=0;
        FOR(i,n){
            vs vv;
            FOR(j,m){
                if(w[j]==i){vv.pb(v[j]);}
            }
            set<string> s;
            FOR(j,sz(vv)){
                while(true){
                    s.insert(vv[j]);
                    if(vv[j]=="")break;
                    vv[j]=vv[j].substr(0,vv[j].length()-1);
                }    
            }
            num+=s.size();
        }
        //cout<<num<<endl;
        if(num>b){b=num;resnum=0;}
        if(num==b){resnum++;}
        
        
        w[0]++;
        for(int i=0;i<m;i++){
            if(w[i]>=n){w[i]=0;if(i+1>=m){goto next;}w[i+1]++;}
        }
        
    }
    next:
    
    
    cout<<"Case #"<<(k+1)<<": ";
    cout<<b<<" "<<resnum<<endl;
    nextcase: 
    continue;      
  }
  
  
  end:
  return 0;
}
