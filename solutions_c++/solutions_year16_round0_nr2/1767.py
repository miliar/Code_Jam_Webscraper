#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("Bin.txt","r",stdin);
	freopen("Bout.txt","w",stdout);
	int T;
	cin>>T;
	char str[105];
	int a[105];
	for(int t=1;t<=T;t++)
	{
		scanf("%s",str);
		int n=strlen(str);
		for(int j=0;j<n;j++)
			a[j]=((str[j]=='-')?1:0);
		int cnt=0;
		for(int j=n-1;j>=0;j--)
		{
			if(a[j]==0)
				continue;
			int k=0;
			while(a[k]==0)
			{
				k++;
			}
			if(k>0)
			{
				reverse(a,a+k);
				while(k>0)
				{
					k--;
					a[k]=1-a[k];
				}
				cnt++;
			}
			reverse(a,a+j+1);
			for(k=0;k<=j;k++)
				a[k]=1-a[k];
			cnt++;
		}
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}