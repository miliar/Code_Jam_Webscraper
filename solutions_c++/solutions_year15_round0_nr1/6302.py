#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	char x[1001]={0};
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		int n;
		scanf("%d",&n);
		cin >> x;
		int p=0;
		int per=0;
		for(int j=0;j<=n;j++)
		{
			if((x[j]-'0')!=0)
			{
				if((j-p)>0)
				{
					per += j-p;
					p+=j-p;
				}
				p+=x[j]-'0';
			}
		}
		printf("%d\n",per);
	}
	return 0;
}
