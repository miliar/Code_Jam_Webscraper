#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int caseno=1;
	while(t--)
	{
		int count=0;
		int num;
		bool arr[17]={0};
		int m,n,temp;
		cin>>m;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>temp;
				if(i==m-1)
				{
					arr[temp]=1;
				}
			}
		}
		cin>>n;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>temp;
				if(i==n-1)
				{
					if(arr[temp]==1)
					{
						count++;
						num=temp;
					}
				}
			}
		}
		if(count==1)
			printf("Case #%d: %d\n",caseno,num);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",caseno);
		else
			printf("Case #%d: Bad magician!\n",caseno);
		caseno++;
	}
	return 0;
}
