#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

const long long limit	=	100000000000000LL;
//const long long limit	=	1000;

inline bool check(long long x)
{
	char s[20];
	sprintf(s,"%I64d",x);
	int len=strlen(s);
	for (int i=0;i+i<len;++i){
		if (s[i]!=s[len-1-i]){
			return false;
		}
	}
	return true;
}

int main()
{
	vector<long long> ans;
	for (long long i=1;i*i<=limit;++i){
		if (check(i) && check(i*i)){
			ans.push_back(i*i);
//printf("%I64d\n",i*i);
		}
	}
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		long long A,B;
		scanf("%I64d%I64d",&A,&B);
		assert(A<=B && B<=limit);
		int total=upper_bound(ans.begin(),ans.end(),B)-lower_bound(ans.begin(),ans.end(),A);
		printf("Case #%d: %d\n",test,total);
	}
	return 0;
}
