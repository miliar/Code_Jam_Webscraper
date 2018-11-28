#include <cstdio>
#include <algorithm>
#include <stack>

using namespace std;
#define MOD 1000002013ll

int main()
{
  int T;
  scanf("%d",&T);
  for(int C=1;C<=T;C++){
    long long N;
    int m;
    scanf("%lld%d",&N,&m);
    pair<long long,long long> P[2000];
    long long M=0;
    for(int i=0;i<m;i++){
      long long o,e,p;
      scanf("%lld%lld%lld",&o,&e,&p);
      P[2*i].first=o;
      P[2*i].second=-p;
      P[2*i+1].first=e;
      P[2*i+1].second=p;
      M=(M+(e-o)*(2*N-(e-o-1))/2%MOD*p%MOD)%MOD;
    }
    sort(P,P+2*m);
    stack<pair<long long,long long> > S;
    long long K=0;
    for(int i=0;i<2*m;i++){
      long long t=P[i].first,p=-P[i].second;
      if(p>0){
	S.push(make_pair(p,t));
      }
      else{
	p=-p;
	while(p){
	  pair<long long,long long> pr=S.top();
	  S.pop();
	  long long r=pr.first,s=pr.second;
	  //printf("%lld %lld\n",s,r);
	  if(p>=r){
	    p-=r;
	    K=(K+(t-s)*(2*N-(t-s-1))/2%MOD*r%MOD)%MOD;
	  }
	  else{
	    //p=0;
	    K=(K+(t-s)*(2*N-(t-s-1))/2%MOD*p%MOD)%MOD;
	    //p=0;
	    S.push(make_pair(r-p,s));
	    p=0;
	  }
	  //printf("%lld\n",K);
	}
      }
    }
    printf("Case #%d: %lld\n",C,(M+MOD-K)%MOD);
  }
  return 0;
}
