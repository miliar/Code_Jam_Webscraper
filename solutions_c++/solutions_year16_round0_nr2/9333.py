#include <stdio.h>
#include<string.h>
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;j++)
	{
		char s[100];
		scanf("%s",s);
		int l=strlen(s);
		int count=0;
		int ans=0;
		if(s[0]=='-')
		ans--;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			count++;
			while(s[i]=='-')
				i++;
			
		}
		//printf("count %d\n",count);
		//printf("len %d\n",l);
		
		ans+=2*count;
		printf("Case #%d: %d\n",j+1,ans);
	}
	return 0;
}

