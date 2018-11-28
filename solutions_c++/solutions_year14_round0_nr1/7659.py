#include<iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int p=0;p<t;p++)
	{
		int a,b,x;
		int aa[4],bb[4],k=0;
		cin>>a;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(i==a-1)
					aa[k++]=x;
			}
		}
		k=0;
		cin>>b;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(i==b-1)
					bb[k++]=x;
			}
		}
		k=0;
		int pos;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(aa[i]==bb[j])
				{
					k++;
					pos=i;
				}
			}
		}
		cout<<"Case #"<<p+1<<": ";
		if(k==1)
			cout<<aa[pos];
		else if(k==0)
			cout<<"Volunteer cheated!";
		else
			cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}