#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>

#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define pi pair<long long, long long>
#define MOD 1000002013

using namespace std;

int n,m,cs;
ll opt,norm,o[1100],e[1100],p[1100],a[2200],sum,dst,prev;
stack<pi > vp;

int main(){

  cin>>cs;

  rep(ii,cs){
    cin>>n>>m;
    norm = 0;
    opt = 0;

    rep(i,m){
      cin>>o[i]>>e[i]>>p[i];
      dst = e[i]-o[i];
      norm = (norm+p[i]*(dst*(2*n-dst+1)/2%MOD)%MOD)%MOD;
      a[i*2]=o[i];a[i*2+1]=e[i];
    }
    sort(a,a+2*m);
    prev = -1;

    rep(i,2*m){
      //cout<<i<<" "<<a[i]<<endl;
      if(prev == a[i])continue;

      sum = 0;
      rep(j,m)if(o[j]==a[i])sum += p[j];
      if(sum!=0){
	vp.push(pi(a[i],sum));
	//cout<<"Push : "<<a[i]<<" "<<sum<<endl;
      }
      prev = a[i];

      rep(j,m){
	if(e[j]==a[i]){
	  while(p[j]>0){
	    pi sp = vp.top(); vp.pop();
	    if(sp.second > p[j]){
	      sp.second -= p[j];
	      dst = e[j]-sp.first;
	      opt = (opt + p[j]*((ll)(2*n-dst+1)*dst/2%MOD)%MOD)%MOD;
	      //cout<<"Pop "<<e[j]<<" : "<<dst<<" "<<opt<<" inc : "<<inc<<endl;
	      p[j] = 0;
	      vp.push(sp);
	    }
	    else {
	      dst = e[j]-sp.first;
	      opt = (opt + sp.second*((ll)(2*n-dst+1)*dst/2%MOD)%MOD)%MOD;
	      //ll inc = p[j]*((ll)(2*n-dst+1)*dst/2%MOD)%MOD;
	      //cout<<"Pop "<<e[j]<<" : "<<dst<<" "<<opt<<" inc : "<<inc<<" "<<p[j]<<" "<<endl;
	      p[j] -= sp.second;
	    }
	  }
	}
      }
    }
    cout<<"Case #"<<ii+1<<": "<<(norm+MOD-opt)%MOD<<endl;
  }

}
