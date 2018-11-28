#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
typedef __int64 LL;
LL palin[100];
LL palindrome(LL i)
{
	LL l,k,m,j;
	char s[100];
	sprintf(s,"%I64d",i);
	l=strlen(s);
	k=0;
	m=l-1;
	j=0;
	while(k<m)
	{
		if(s[k]!=s[m])
		{
			return 0;
		}
		k++;
		m--;
	}
	return 1;
}

int main()
{
	  freopen("input.txt","r",stdin);
	  freopen("output.txt","w",stdout);
	LL i,j,k,l,m,n,test,cas=1,a,b;
	string s,ss;
	l=0;
	for(i=1;i<=10000000;i++)
	{
		if(palindrome(i)==1)
		{
			k=i*i;
			if(palindrome(k)==1)
			{
				palin[l++]=k;
			}
		}
	}	
	scanf("%I64d",&test);
	while(test--)
	{
		scanf("%I64d%I64d",&a,&b);
		m=0;
		for(i=0;i<l;i++)
		{
			if(palin[i]>=a&&palin[i]<=b)
				m++;
		}
		printf("Case #%I64d: %I64d\n",cas++,m);
	}

	return 0;
}
		
