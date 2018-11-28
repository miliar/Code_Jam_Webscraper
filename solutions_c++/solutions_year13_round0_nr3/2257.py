#include<cstdio>
#include<vector>
#include<cmath>
#define MAX 10000000
using namespace std;

int t,i,j,res;
long long a,b;
vector<long long> f;

bool check(long long x){
	vector<int> t;
	while(x>0){
		t.push_back(x%10);
		x/=10;
	}
	for(int i=0; 2*i<=t.size(); ++i)
		if(t[i]!=t[t.size()-i-1]) return false;

	return true;
}

int main(){
	scanf("%d",&t);
	for(i=1; i<=MAX; ++i){
		long long cur=(long long)i*i;
		if(check(i) && check(cur)) f.push_back(cur);
	}

	for(int i=1; i<=t; ++i){
		res=0;
		scanf("%lld%lld",&a,&b);
		for(int j=0; j<f.size(); ++j)
			if(f[j]>=a && f[j]<=b) ++res;	
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}
