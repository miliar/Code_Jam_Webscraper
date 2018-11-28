#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,t,j,flag,count=0;
	cin>>t;
	char** dataset = new char*[t];
	for(i=0;i<t;i++)
        dataset[i] = new char[1000];
	int *size = new int[t];
	for(i=0;i<t;i++)
	{
		cin>>dataset[i];
		size[i]=strlen(dataset[i]);
	}
	getchar();
	for(i=0;i<t;i++)
	{
		count=0;
		while(1)
		{
			flag=-1;
			for(j=size[i]-1;j>=0;j--)
			{
				if(dataset[i][j]=='-')
				{
					flag=j;
					break;
				}
			}
			if(flag!=-1)
			{
				for(j=0;j<=flag;j++)
				{
					if(dataset[i][j]=='+')
						dataset[i][j]='-';
					else
						dataset[i][j]='+';
				}
				count++;
			}
			else if(flag==-1)
			{
				printf("Case #%d: %d\n",i+1,count);
				break;
			}
		}
	}
	return 0;
}
