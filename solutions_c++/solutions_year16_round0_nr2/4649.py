#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,t1 = 0;
	scanf("%d",&t);
	while(t--)
	{
		t1++;
		int n = 0;
		char s[101];
		scanf("%s",s);
		int a[101];
		
		for(int i=0;s[i]!='\0';i++)
			{
				n++;
				if(s[i]=='-')a[i]=0;
				else a[i] = 1;
			 }
			 int cnt = 0;
		for(int i=n-1;i>=0;i--)
		{
			if(a[i]==1)
				continue;
			else{
				cnt++;

				for(int j=i;j>=0;j--)
					if(a[j]==1)a[j] = 0;
					else a[j] = 1;
			}
		}
		printf("Case #%d: %d\n",t1,cnt);
	}
	return 0;
}