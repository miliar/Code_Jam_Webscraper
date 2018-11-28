#include<iostream>
using namespace std;
int main()
{
	int t,tc,i,j,no,a,win,prob[20];
	cin>>t;
	for (tc=1;tc<=t;tc++)
	{
		for (i=1;i<=16;i++) prob[i]=0;
		cin>>a;
		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				cin>>no;
				if (i+1==a)
				{
					prob[no]+=1;
				}
			}
		}
		cin>>a;
		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				cin>>no;
				if (i+1==a)
				{
					prob[no]+=1;
				}
			}
		}
		win=0;
		for (i=1;i<=16;i++)
		{
			if (win==0&&prob[i]==2)
			{
				win=i;
			}
			else if (prob[i]==2)
			{
				win=-1;
			}
		}
	//	for (i=1;i<=16;i++) cout<<prob[i]<<" ";
		if (win==-1)
		{
			cout<<"Case #"<<tc<<": Bad magician!"<<endl;
		}
		else if (win==0)
		{
			cout<<"Case #"<<tc<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<tc<<": "<<win<<endl;
		}
	}
	return 0;
}
