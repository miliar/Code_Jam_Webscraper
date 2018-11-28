#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		char str[102];
		scanf("%s",str);

		int l=strlen(str);

		char prev=str[0];
		int count=0;

		for(int j=1;j<l;j++)
		{
			if(prev!=str[j])
				count++;
			prev=str[j];
		}
		if(prev!=str[l-1])
			count++;
		if(str[l-1]=='-')
			count++;
		printf("Case #%d: %d\n",i+1,count);
	}

	return 0;
}






