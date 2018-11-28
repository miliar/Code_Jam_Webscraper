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
#define ppiipii pair< pair<int,int>,pair<int,int> >
#define vppiipii vector< pair< pair<int,int>,pair<int,int> > >
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

bool between(int x, int a, int b){
    return (a<x && x<b);
}

int dist(ppiipii p1, ppiipii p2){
    if(p1.first.first==p2.second.first || p1.second.first==p2.first.first){
      if(between(p1.first.second,p2.first.second,p2.second.second)){return 0;}
      if(between(p1.second.second,p2.first.second,p2.second.second)){return 0;}
      if(between(p2.first.second,p1.first.second,p1.second.second)){return 0;}
      if(between(p2.second.second,p1.first.second,p1.second.second)){return 0;}
    }
    if(p1.first.second==p2.second.second || p1.second.second==p2.first.second){
      if(between(p1.first.first,p2.first.first,p2.second.first)){return 0;}
      if(between(p1.second.first,p2.first.first,p2.second.first)){return 0;}
      if(between(p2.first.first,p1.first.first,p1.second.first)){return 0;}
      if(between(p2.second.first,p1.first.first,p1.second.first)){return 0;}
    }
    
    if(between(p1.first.first, p2.first.first, p2.second.first) || between(p1.second.first, p2.first.first, p2.second.first)
        || (p1.first.first==p2.first.first) || (p1.second.first==p2.second.first) || 
        between(p2.first.first, p1.first.first, p1.second.first) || between(p2.second.first, p1.first.first, p1.second.first)
    ){
        //cerr<<"t"<<min(abs(p1.first.second-p2.second.second), abs(p1.second.second-p2.first.second))<<endl; 
        return min(abs(p1.first.second-p2.second.second), abs(p1.second.second-p2.first.second));    
    }

    if(between(p1.first.second, p2.first.second, p2.second.second) || between(p1.second.second, p2.first.second, p2.second.second)
         || (p1.first.second==p2.first.second) || (p1.second.second==p2.second.second) ||
         between(p2.first.second, p1.first.second, p1.second.second) || between(p2.second.second, p1.first.second, p1.second.second) 
    ){
        //cerr<<"tt "<<min(abs(p1.first.second-p2.second.second), abs(p1.second.second-p2.first.second))<<endl; 

        return min(abs(p1.first.first-p2.second.first), abs(p1.second.first-p2.first.first));    
    }
    
    int xx, yy;
    xx=min(abs(p1.first.first-p2.second.first), abs(p1.second.first-p2.first.first));
    yy=min(abs(p1.first.second-p2.second.second), abs(p1.second.second-p2.first.second));
    //cerr<<"o "<<xx<<yy<<endl;
    return max(xx,yy);

}

int main(void){
  int K;
  cin>>K;
  FOR(k,K){
    int w,h,b;
    cin>>w>>h>>b;
    vppiipii v;
    v.pb(mp(mp(-1,0),mp(0,h)));
    v.pb(mp(mp(w,0),mp(w+1,h)));
    FOR(i,b){
        int x,y,xx,yy;
        cin>>x>>y>>xx>>yy;
        v.pb(mp(mp(x,y),mp(xx+1,yy+1)));    
    }
    int n=v.size();
    vector <vector <int> > di;
    vi vv=vi(n,0);
    FOR(i,n){di.pb(vv);}
    
    FOR(i,n)FOR(j,n){
      if(i>=j)continue;
//      cerr<<"dist"<<i<<","<<j<<":"<<d<<endl;
      int d=dist(v[i],v[j]);
      //cerr<<"dist"<<i<<","<<j<<":"<<d<<endl;
      di[i][j]=d;
      di[j][i]=d;
    }
    vi hl=vi(n,-1);
    vi closed = vi(n,0);
    hl[0]=0;
    
    while(true){
        //cerr<<".";
        int mm=-1;
        int c=-1;
        FOR(i,n){
          if(closed[i]!=0)continue;
          if(hl[i]==-1)continue;
          if(mm==-1 || hl[i]<mm){mm=hl[i];c=i;}
        }
        //cerr<<c<<" "<<hl[c]<<endl;
        
        if(c==1){break;}
        closed[c]=1;
        FOR(i,n){
            if(c==i)continue;
            if(hl[i]==-1 || hl[c]+di[c][i]<hl[i]){hl[i]=hl[c]+di[c][i];}    
        }
        //FOR(i,n)cerr<<hl[i]<<",";cerr<<endl;
    }
    
    cout<<"Case #"<<(k+1)<<": ";
    cout<<hl[1]<<endl;
    nextcase: 
    continue;      
  }
  
  
  end:
  return 0;
}
