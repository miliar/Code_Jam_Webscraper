#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

long long num[100],a,b;
int nl,t;
char s[20];

int ck(long long i)
{
	sprintf(s,"%lld",i);
	int l=0,h=strlen(s)-1;
	while(l<h)
	{
		if(s[l]!=s[h]) break;
		l++;
		h--;
	}
	if(l<h) return 0;
	long long j=sqrt(i);
	if(j*j<i) return 0;
	sprintf(s,"%lld",j);
	l=0,h=strlen(s)-1;
	while(l<h)
	{
		if(s[l]!=s[h]) break;
		l++;
		h--;
	}
	if(l<h) return 0;
	return 1;
}

void mknum(long long j,long long k)
{
	if(j>100000000000000ll) return;
	long long i;
	if(ck(j)) num[nl++]=j;
	for(i=1;i<10;i++) mknum(i*k+j*10+i,k*100);
}

main()
{
	long long i,j,k;
	for(i=1;i<10;i++) mknum(i,100ll);
	sort(num,num+nl);
	scanf("%*d");
	while(~scanf("%lld%lld",&a,&b))
	{
		for(i=0;num[i]<a&&i<nl;i++);
		i--;
		for(j=0;num[j]<=b&&j<nl;j++);
		j--;
		printf("Case #%d: %d\n",++t,j-i);
	}
}
