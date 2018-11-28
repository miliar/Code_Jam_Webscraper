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
vector <ll> v;
ll dp[15][10];
ll E,R,N;
ll solve(int pos, int energy){
	ll ref=dp[pos][energy];
	if(ref!=-1)return ref;
	if(pos==v.size())return 0;
	ll result=0;
	for(int i=0;i<=energy;++i){
		result=max(result,v[pos]*i+solve(pos+1,min(E,energy-i+R)));

	}
	ref=result;
	return result;
}
int main(void)
{
	int T;
	cin>>T;

	for(int _t=1;_t<=T;++_t){	
		memset(dp,-1,sizeof(dp));	
		cin>>E>>R>>N;
		v.clear();
		v.resize(N);
		for(int i=0;i<N;++i){
			cin>>v[i];
		}
	
		ll result=solve(0,E);
		
		
		cout<<"Case #"<<_t<<": "<<result<<endl;
		cerr<<"cerr:"<<_t<<endl;	
	}
}


//	cout.setf(ios::fixed);

