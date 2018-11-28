#include<bits/stdc++.h>
using namespace std;
char s[10005];
int main() {
	int t,sm,ctr=0,ctr1=1,ans=0;
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		scanf("%d%s",&sm,s);
		ctr=s[0]-'0';
		//printf("ctr=%d\n",ctr);
		for(int i=1;i<=sm;i++)
		{
			if(i>ctr)
			{
				//printf("ashu");
				int p=i-ctr;
				ans+=p;
				ctr+=p;
			}
			{
				ctr+=s[i]-'0';
			}
		}
		printf("Case #%d: %d\n",ctr1,ans);
		ctr1++;
	}
	return 0;
}
