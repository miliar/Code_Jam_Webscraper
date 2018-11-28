/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;

int arr[1003];

int main() 
{	
	int t;
	scanf("%d",&t);
	int rt=t;
	while(t--)
	{
		string s;
		cin>>s;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='+')
			{
				arr[i]=1;
			}
			else
			{
				arr[i]=0;
			}
		}
		int len=s.length();
		int n;
		scanf("%d",&n);
		int ans=0;
		/*printf("%d %d\n",len,n);*/

		for(int i=0;i<=(len-n);i++)
		{
			if(arr[i]==1)
			{	
				continue;
			}
			ans++;	
			for(int j=i;j<i+n;j++)
			{
				arr[j]^=1;
			}
		}
		int flg=0;
		for(int i=0;i<len;i++)
		{
			if(arr[i]==0)
			{
				flg=1;
				break;
			}
		}
		if(flg==0)
		{
			printf("Case #%d: %d\n",rt-t,ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",rt-t);
		}	
	}
	return 0;
}