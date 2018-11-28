#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
	int t,j=1;
	cin>>t;
	int x,r,c;
	while(j<=t)
	{
		cin>>x>>r>>c;
		if(x>=7)
			printf("Case #%d: RICHARD\n",j++);
		else
		{
			if((r%x==0&&c>=x-1)||(c%x==0&&r>=x-1))
				printf("Case #%d: GABRIEL\n",j++);
			else
				printf("Case #%d: RICHARD\n",j++);
		}
	}
	return 0;
}