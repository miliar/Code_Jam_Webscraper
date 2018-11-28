#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
bool checkPalin(long long x){
	char s[16];
	sprintf(s,"%lld",x);
	int len=strlen(s);
	for(int i=0;i<len/2;++i)
		if(s[i]!=s[len-i-1])
			return false;
	return true;
}
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int size=0;
	long long v[64];
	for(long long i=1;i<10000001;++i)
		if(checkPalin(i) && checkPalin(i*i))
			v[size++]=i*i;
	int t,r;
	long long a,b;
	scanf("%d",&t);
	for(int k=1;k<=t;++k){
		scanf("%lld %lld",&a,&b);
		for(int i=r=0;i<size;++i)
			r+=v[i]>=a && v[i]<=b;
		printf("Case #%d: %d\n",k,r);
	}
	return 0;
}