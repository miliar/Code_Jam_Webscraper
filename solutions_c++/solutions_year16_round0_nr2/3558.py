#include<bits/stdc++.h>
using namespace std;
char a[110];
int main()
{
	int t,cs,i,l,idx,cnt;
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++)
	{
		scanf("%s",a);
		l=strlen(a);
		idx=0;i=0;cnt=0;
		while(i<l)
		{
			while(a[i]==a[idx]&&i<l)
			{
				i++;
			}
			if(i<l)
			{
				idx=i;cnt++;
			}
		}
		if(a[0]=='-'&&!(cnt&1)) cnt+=1;
		else if(a[0]=='+'&&(cnt&1)) cnt+=1;
		printf("Case #%d: %d\n",cs,cnt);
	}
}
