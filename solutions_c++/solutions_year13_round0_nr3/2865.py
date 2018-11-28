#pragma warning (disable: 4530) 
#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
#include<climits>


#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;

typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0,1,1,-1,-1},dy[]={0,-1,0,1,1,-1,-1,1};//right down left up
int test;
bool isPar(ll x){
  char buff[100];
  sprintf(buff,"%lld",x);
  string s = buff;
  string s2 = buff;
  reverse(all(s2));
  return s == s2;
}
int main(){
  scanf("%d",&test);
  rep(t,test){
    ll A,B;
    cin>>A>>B;
    ll res = 0;
    ll cc = 0;
    for(ll i = sqrt((double)A); i * i <= B; i++){
      ll sq = i * i;
      if(A <= sq && sq <= B && isPar(sq) && isPar(i)){
	//	printf("%lld = (%lld * % lld)\n",sq,i,i);	
	res++;
      }
    }    
    printf("Case #%d: %lld\n",t + 1,res);
  }
}
