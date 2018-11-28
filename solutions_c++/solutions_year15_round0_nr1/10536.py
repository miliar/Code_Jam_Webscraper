#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int mini,ppl,t,s;
	char arr[1500];
	register int i,j;
	j=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&s);
		getchar();
		for(i=0;i<=s;i++)
		arr[i]=getchar();
		mini=0;
		ppl=arr[0]-'0';
		for(i=1;i<=s;i++)
		{
			if(ppl<i)
			{
				ppl-=mini;
				mini=i-ppl;
				ppl+=arr[i]-'0'+mini;
			}
			else
			ppl+=arr[i]-'0';
		}
		printf("Case #%d: %d\n",j++,mini);
	}
	return 0;
}