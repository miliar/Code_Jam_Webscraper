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

struct ti{
  int sta;
  int n;
};



bool operator<(const ti &a, const ti &b){
  if (a.sta==b.sta)
    return a.n>b.n;
  return a.sta<b.sta;
}


int main(){
  int T; cin>>T;
  ll p=1000002013;
  for (int tc=1; tc<=T; ++tc){
    ll N; int M; cin>>N>>M;
    vector<ti> v;
    priority_queue<ti> q;
    ll ans=0;
    ll ans2=0;

    for (int i=0; i<M; ++i){
      ll a, b, c;
      cin>>a>>b>>c;
      ti tit;
      tit.sta=a;
      tit.n=c;
      v.push_back(tit);
      tit.sta=b;
      tit.n=-c;
      v.push_back(tit);
      ll bob=(2*N+1-b+a)*(b-a)/2;
      bob%=p;
      bob*=c;
      ans2+=bob;
      ans2%=p;
    }
    sort(v.begin(), v.end());
    for (int i=0; i<v.size(); ++i){
      if (v[i].n>0){
	q.push(v[i]);
      }
      else{
	while (v[i].n<0){
	  ti tit=q.top();
	  q.pop();
	  if (tit.n+v[i].n>0){
	    ll bob=(2*N+1+tit.sta-v[i].sta)*(-tit.sta+v[i].sta)/2;
	    bob%=p;
	    bob*=(-v[i].n);
	    bob%=p;
	    ans+=bob;
	    ans%=p;
	    tit.n+=v[i].n;
	    v[i].n=0;
	    q.push(tit);
	    
	  }
	  else{
	    v[i].n+=tit.n;
	    ll bob=(2*N+1+tit.sta-v[i].sta)*(-tit.sta+v[i].sta)/2;
	    bob%=p;
	    bob*=tit.n;
	    bob%=p;
	    ans+=bob;
	    ans%=p;
	  }
	}
      }
    }
    ans=(ans2-ans+p)%p;
    cout<<"Case #"<<tc<<": "<<ans<<endl;
  }
  return 0;
}
