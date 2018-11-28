#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *f=fopen("B-large.in","r");
	FILE *f1=fopen("op","w");
	ios::sync_with_stdio(false);
	char s[101];
	int t,ans;
	fscanf(f,"%d",&t);
	for(int j=1;j<=t;j++)
	{
		ans=0;
		fscanf(f,"%s",s);
		int n=strlen(s);
		for(int i=1;i<n;i++)
		{
			if(s[i]!=s[i-1])
			ans++;
		}
		if(s[n-1]=='-')
		ans+=1;
		fprintf(f1,"Case #%d: %d\n",j,ans);
	}
	return 0;
}
