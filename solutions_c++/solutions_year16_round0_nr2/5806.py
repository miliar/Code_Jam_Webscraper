#include <bits/stdc++.h>
using namespace std;
#define ll long long
void change(char s[],int last)
{
	int i;
	for(i=0;i<=last;i++)
	{
		if(s[i]=='-')
		s[i]='+';
		else
		s[i]='-';
	}
}
int main() {
	int t,k;
	scanf("%d",&t);
	char s[105];
	for(k=1;k<=t;k++)
	{   int i,cnt=0;
		scanf("%s",s);
		int l=strlen(s);
		for(i=l-1;i>=0;i--)
		{
			if(s[i]=='-')
			{
				change(s,i);
				cnt++;
			}
		}
	 printf("Case #%d: %d\n",k,cnt);
	  
	}
	return 0;
}
