#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

	int t;
	char str[1010];
	char ans[1010];
	int k=0,i;
	scanf("%d",&t);
	
	while(t--)
	{
		k++;
		scanf("%s",str);
		int l=strlen(str);	
		char s;
		
		s=str[0];
		ans[0]=str[0];
		
		for(i=1;i<l;i++)
		{
			if(str[i]>=s)
			{
				s=str[i];
				
				for(int j=i-1;j>=0;j--)
					ans[j+1]=ans[j];
				ans[0]=s;
			}
			else
			{
				ans[i]=str[i];
			}
		}
		
		printf("Case #%d: ",k);
		for(i=0;i<l;i++)
			printf("%c",ans[i]);
		printf("\n");
	}
	return 0;
}
