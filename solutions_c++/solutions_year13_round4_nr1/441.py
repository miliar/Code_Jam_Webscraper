#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<functional>
#include<map>

using namespace std;

int N;

// long long f(long long n){
// int  s=0;
//   for(int i=1;i<=n;i++){
//     s=(s+N+1-i)%1000002013;
//   }
//   return s;
// }

int main(){
  int T;
  cin>>T;
  long long MM=1000002013;
  for(int i=1;i<=T;i++){
    long long N,M;
    cin>>N>>M;
    long long o[1000],e[1000],p[1000];
    long long s=0;
    map<long long,long long> in,out;
    for(int j=0;j<M;j++){
      cin>>o[j]>>e[j]>>p[j];
      long long ni=e[j]-o[j];
      s+=((N+1)*ni-ni*(ni+1)/2)%1000002013*(p[j]%1000002013);
      s%=1000002013;
      in[o[j]]+=p[j];
      out[e[j]]+=p[j];
    }
    long long l=0;
    for(map<long long,long long>::iterator it=out.begin();it!=out.end();it++){
      while(it->second){
	map<long long,long long>::iterator itt=in.upper_bound(it->first);
	itt--;
	//	cout<<it->first<<' '<<itt->first<<endl;
	long long nm=min(it->second,itt->second);
	long long ni=it->first-itt->first;
	l+=((N+1)*ni-ni*(ni+1)/2)%1000002013*(nm%1000002013);
	l%=1000002013;
	it->second-=nm;
	itt->second-=nm;
	if(itt->second==0){
	  in.erase(itt);
	}
      }
    }
    //    cout<<s<<' '<<l<<endl;
    cout<<"Case #"<<i<<": "<<(s-l+1000002013)%1000002013<<endl;
  }
  return 0;
}
