#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define all(a)  a.begin(),a.end() 
#define SL(n) scanf("%lld",&n)
#define PL(n) printf("%lld",n)
#define fill(a, x) memset(a,x,sizeof(a));
#define mod 1000000007

using namespace std;
typedef long long LL;
typedef vector <LL> VL;
typedef map <LL, LL> ML;
typedef pair<LL, LL> PL;
typedef vector <pair <LL, LL> > VPL;

int main(){
  LL T;
  SL(T);
  for(LL t=1;t<=T;++t){
    printf("Case #%lld: ", t);
    LL N;
    string temp;
    VL S;
    cin >> N >> temp;
    for(LL n=0;n<temp.sz;++n){
      S.pb(temp[n]-'0');
    }
    LL Ans=0;
    LL Persons=0;
    for(LL n=0;n<S.sz;++n){
      while(S[n]>=1){
        if(Persons < n){
          Ans++;
          Persons++;
        }
        else{
          S[n]--;
          Persons++;
        }
      }
    }
    printf("%lld\n", Ans);
  }
  return 0;
}
