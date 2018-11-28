#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>



using namespace std;

typedef long long ll;


int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    int N; ll P; cin>>N>>P;
    ll en=1;
    ll to=1;
    
    P-=1;
    
    ll tre=(en<<(N-1));
    ll ans=tre*2-1;
    for (int i=0; i<N; ++i){
      if ((tre&P)==0){
	ans=((en<<i)-1)*2;
	break;
      }
      tre/=2;
    }
    en=1;
     
    for (int i=0; i<N; ++i){
      if ((to&P)==0 && P>to){
	P-=to;

      }
      to+=to;
    }
    ll c=1;
    ll ans2=0;
    to=(en<<(N-1));
    for (int i=N-1; i>=0; --i){
      if ((to&P)==0){
	ans2+=c;
	c+=c;
      }
      to/=2;
    }
    ans2=(en<<N)-ans2-1;
    
    


    
    cout<<"Case #"<<tc<<": "<<ans<<" "<<ans2<<endl;
  }
  return 0;
}
