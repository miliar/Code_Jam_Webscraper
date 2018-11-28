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
    int x;
    cin>>n>>x;
    vi v;
    READ(v,n);
    sort(all(v));
    int sum=0;
    for(int i=n-1;i>=0;i--){
        int c=v[i];

        for(int j=i-1;j>=0;j--){
            if(v[j]+c<=x){v.erase(v.begin()+j); i--; break;}
        }   
        sum++;
    }
   
    cout<<"Case #"<<(k+1)<<": ";
    cout<<sum<<endl;
    nextcase: 
    continue;      
  }
  
  
  end:
  return 0;
}
