#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int test=1,i,len,ans,t;
	char s[105];
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		scanf(" %s",s);	
		printf("Case #%d: ",test++);
		len=strlen(s);
		for(i=0;i<len;)
		{
			if(s[i]=='+')
			while(i<len && s[i]=='+') i++;
			else
			while(i<len && s[i]=='-') i++;
			ans++;
		}
		if(s[len-1]=='+') ans--;
		printf("%d\n",ans);
	}
	return 0;
}