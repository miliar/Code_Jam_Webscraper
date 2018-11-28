#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	scanf("%d",&n);
	for(int i = 0;i<n;i++)
	{
		char str[128];
		scanf("%s",str);
		int len = strlen(str);
		int flip = 0;
		for(int j = 0;j<len-1;j++)
		{
			if(str[j] != str[j+1])flip++;
		}
		printf("Case #%d: %d\n",i+1,flip + (str[len-1] == '-'?1:0));
	}
}
