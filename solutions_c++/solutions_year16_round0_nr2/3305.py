#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int T;
char s[102];
int len, ans;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&T);
	for (int k=1;k<=T;k++)
	{
		scanf("%s",s);
		len=strlen(s);
		s[len]='+';
		
		ans=0;
		for (int i=1;i<=len;i++)
		if (s[i]!=s[i-1])
			ans++;
		
		printf("Case  #%d: %d\n",k, ans);
	}
	
	fclose(stdin);
	fclose(stdout);			
	return 0;
}




