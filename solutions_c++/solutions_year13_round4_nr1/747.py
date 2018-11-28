#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int T,N,M,o,e,p;
long long num[2002];

const int INF=0x7fffffff;
const long long MOD=1000002013;

struct node{
	int o,e,p;
};

vector<node> in;
vector<int> hashx;

int getid(int x){
	int l=0,r=hashx.size()-1;
	while(l<r){
		int m=(l+r)/2;
		if(hashx[m]<x) l=m+1;
		else r=m;
	}
	return l;
}

long long cost(long long len){
	long long ans;
	ans= (2*N-len+1)*len/2;
	ans%=MOD;
	return ans;
}

long long getlen(){
	int pre=-1,res=-1,end;
	long long cnt=INF;
	for(int i=0; i<=hashx.size(); ++i){
		if(num[i]){
			if(pre==-1) pre=i;
			cnt=min(cnt,num[i]);
		}
		else{
			if(pre==-1) continue;
			else{
				res=hashx[i]-hashx[pre];
				end=i;
				break;
			}
		}
	}
	if(res!=-1){
		for(int i=pre; i<end; ++i){
			num[i]-=cnt;
		}
	}
	if(res!=-1)
	return cost(res)*cnt;
	else return -1;
}


int main(){
	freopen("a.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	
	long long ans2;
	cin>>T;
	for(int cas=1; cas<=T; ++cas){
		cin>>N>>M;
		hashx.clear();
		in.clear();
		ans2=0;
		node tmp;
		for(int i=0; i<M; ++i){
			cin>>tmp.o>>tmp.e>>tmp.p;
			hashx.push_back(tmp.o);
			hashx.push_back(tmp.e);
			ans2+=cost(tmp.e-tmp.o)*tmp.p;
			ans2%=MOD;
			in.push_back(tmp);
		}
		sort(hashx.begin(),hashx.end());
		hashx.erase(unique(hashx.begin(),hashx.end()),hashx.end());

		for(int i=0; i<M; ++i){
			int to=getid(in[i].o);
			int te=getid(in[i].e);
			for(int j=to; j<te; ++j){
				num[j]+=in[i].p;
			}
		}
		long long ans=0;
		while(1){
			long long deta=getlen();
			if(deta==-1) break;
			ans+=deta%MOD; ans%=MOD;
		}
		cout<<"Case #"<<cas<<": ";
		cout<<((ans2-ans)%MOD+MOD)%MOD<<endl;
	}

}