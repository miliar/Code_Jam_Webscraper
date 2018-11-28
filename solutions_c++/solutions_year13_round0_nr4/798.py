// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;
#define ll long long
vector <int> org;
vector <vector <int> > in;
vector <int> op;
int K,N;
vector <int> emp;
vector <int> dp[2<<20];
vector <int> solve(ll msk){
	vector <int> & ref=dp[msk];
	if(ref.size()!=1||ref[0]!=-1)return ref;

	ll tmp=msk;
	int keys[201];
	memset(keys,0,sizeof(keys));
	for(int i=0;i<org.size();++i)keys[org[i]]++;

	int pos=0,cnt=0;;
	while(tmp){
		if(tmp&1){
			++cnt;
			keys[op[pos]]--;
			for(int i=0;i<in[pos].size();++i){
				keys[in[pos][i]]++;
			}
		}
		tmp>>=1;
		++pos;
	}
	if(cnt==N){
		ref=emp;
		return emp;
	}

	for(ll i=0;i<N;++i){
		if((msk>>i)&1)continue;
		if(keys[op[i]]>0){
			vector <int> res;	
			res = solve( (msk|(1LL<<i)));
			if(cnt+1+res.size()==N){
				vector <int> result;
				result.push_back(i);
				for(int j=0;j<res.size();++j){
					result.push_back(res[j]);
				}
				ref=result;
				return result;
			}
		}
	}
	ref=emp;	
	return emp;
}

int main()
{


	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t){
		org.clear();
		in.clear();
		op.clear();
		
		cin>>K>>N;

		org.resize(K);
		for(int i=0;i<K;++i){
			cin>>org[i];
		}
		
		op.resize(N);
		in.resize(N);
		for(int i=0;i<N;++i){
			cin>>op[i];
			int keyNum;
			cin>>keyNum;
			in[i].resize(keyNum);
			for(int j=0;j<keyNum;++j){
				cin>>in[i][j];
			}
		}

		for(ll i=0;i<(1<<N);++i)dp[i].clear(),dp[i].push_back(-1);
#if 0
		cout<<"org:"<<endl;
		for(int i=0;i<org.size();++i)cout<<org[i]<<" ";
		cout<<endl<<endl;

		cout<<"op:"<<endl;
		for(int i=0;i<N;++i)cout<<op[i]<<" ";
		cout<<endl<<endl;

		cout<<"in:"<<endl;
		for(int i=0;i<N;++i){
			for(int j=0;j<in[i].size();++j)cout<<in[i][j]<<" ";
			cout<<endl;
		}
#endif
		vector <int> result=solve(0);
		if(result.size()==0){
			cout<<"Case #"<<_t<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<_t<<": ";
			for(int i=0;i<result.size();++i){
				cout<<result[i]+1<<" ";
			}
			cout<<endl;
		}

	}

}



