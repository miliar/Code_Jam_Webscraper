//God & me
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int maxn=1e6;
int n;
bool have[10];
bool check(int n){
  while(n > 9)
    have[n % 10] = 1,n /= 10;
  have[n] = 1;
  for(int i=0;i<10;i++)
    if(!have[i])
      return 0;
  return 1;
}
main(){
  //ios::sync_with_stdio(0),cin.tie(0);
  int t;cin>>t;
  int T=0;
  while(t--){
    memset(have,0,sizeof have);
    cin>>n;
    cout<<"Case #"<<++T<<": ";
    int cn=n;
    bool ok=0;
    for(int i=1;i<maxn;i++){
      if(check(n)){
	cout<<n<<'\n';
	ok=1;
	break;
      }
      int tmp;
      if(__builtin_add_overflow(n,cn,&tmp))  break;
      n += cn;
    }
    if(!ok)
      cout<<"INSOMNIA\n";
  }
  return 0;
}
