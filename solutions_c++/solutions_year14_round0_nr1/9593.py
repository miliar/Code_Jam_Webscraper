#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t,tt=1,x;
	cin>>t;
	int a[16];
	while(tt<=t)
	{
		memset(a,0,sizeof(a));
		int r1,r2;
		cin>>r1;
		r1--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(r1==i)
					a[x-1]++;
			}
		}
		cin>>r2;
		r2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(r2==i)
					a[x-1]++;
			}
		}
		int count2=0;
		int count2v=0;
		for(int i=0;i<16;i++)
		{
			if(a[i]==2)
			{
				count2++;
				count2v=i;
			}
		}
		cout<<"Case #"<<tt<<": ";
		
		if(count2==0)
		{
			cout<<"Volunteer cheated!\n";
		}
		else if(count2 == 1)
		{
			cout<<count2v+1<<endl;
		}
		else
		{
			cout<<"Bad magician!\n";
		}

		tt++;
	}
	return 0;
}