#include<iostream>
#include<string>
#include<vector>
#include<list>
#include<stack> 
#include<queue> 
#include<set>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

inline bool IsPal(long long num)
{
	char buf[100];
	sprintf(buf,"%lld",num);
	int end=strlen(buf);
	for(int i=0,j=end-1;i<j;++i,--j)
		if(buf[i]!=buf[j])
			return false;
	return true;			
}

int main()
{
	
	freopen("\\GOOGLE data\\C-small-attempt0.in","r",stdin);
	freopen("\\GOOGLE data\\C-small-attempt0.out","w",stdout);
	int t;
	long long a,b;
	scanf("%d",&t);
	for(int nt=1;nt<=t;nt++)
	{
		scanf("%lld%lld",&a,&b);
		long long start = (long long)sqrt(a),ans=0;
		if(IsPal(a)&&sqrt(a)-start==0&&IsPal(start)) ans++;
		start++;		
		for(long long t=start*start;t<=b;)
		{
			if(IsPal(start)&&IsPal(t)) ans++;
			start++;
			t = start*start;		
		}
		printf("Case #%d: %d\n",nt,ans);
	}			
	return 0;
}
