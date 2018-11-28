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
#include <iomanip>
#include <limits.h>
#include <NTL/ZZ.h>
//#include <sys/time.h>
//#include <time.h>
using namespace NTL;
using namespace std;
#define ll long long
int main(void)
{
	int T;
	cin>>T;

	for(int _t=1;_t<=T;++_t){	
	cout<<"Case #"<<_t<<": "<<endl;
	

		ll R,N,M,K;
		cin>>R>>N>>M>>K;
		for(int _r=1;_r<=R;++_r){
		vector <ll> k;
		k.resize(K);
		for(int j=0;j<K;++j){
			cin>>k[j];
		}

		bool done=false;
		ll maxi=1;
		for(ll i=0;i<N;++i)maxi*=M;
		for(ll i=0;i<=maxi;++i){
			ll tmp=i;
			vector <ll> ans;
			ans.resize(N);
			bool skip=false;
			for(int j=0;j<N;++j){
				ans[j]=tmp%M;
				++ans[j];
				tmp/=M;
				if(ans[j]==1){
					skip=true;
					break;
				}
			}
			if(skip)continue;
			bool fail=false;
			for(int j=0;j<K;++j){
				int num=k[j];
				
				for(int p=0;p<N;++p){
					if(num%ans[p]==0)num/=ans[p];
				}
				if(num!=1){
					//cout<<num<<endl;
					fail=true;
					break;
				}
			}
		
			if(!fail){
				for(int j=0;j<N;++j){
					cout<<ans[j];
				}
				done=true;
				cout<<endl;
				break;
			}

		}
		if(!done){
			for(int j=0;j<N;++j)cout<<2;cout<<endl;
		}
		}
		cerr<<"cerr:"<<_t<<endl;
	}
}


//	cout.setf(ios::fixed);

