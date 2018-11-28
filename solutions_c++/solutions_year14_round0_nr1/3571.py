#include<iostream>
using namespace std;
int main()
{
	int t;
	int cases=1;
	scanf("%d",&t);
	while(t--)
	{
		int a[4][4]={},b[4][4]={};
		int count[20]={};
		int answer=0;
		int ans=0;
		int row;
		scanf("%d",&row);
		int flag=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
				if(i==row-1)
				{
					count[a[i][j]]++;
				}
			}
		}
		int num;
		scanf("%d",&num);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
				if(i==num-1)
				{
					if(count[b[i][j]]>0)
					{
						//cout<<"HAHA"<<endl;
						ans++;
						answer=b[i][j];
					}
				}
			}
		}
		if(ans==1)
		{
			cout<<"Case #"<<cases<<": "<<answer<<endl;
		}
		else if(ans>1)
		{
			cout<<"Case #"<<cases<<": "<<"Bad magician!"<<endl;
		}
		else if(ans==0)
		{
			cout<<"Case #"<<cases<<": "<<"Volunteer cheated!"<<endl;
		}
		cases++;
	}
}
