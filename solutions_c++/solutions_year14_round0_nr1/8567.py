#include <iostream>
using namespace std;

int main() {
	int t,p,count,value,temp;
	int * a = new int[16];
	for(int i=0;i<16;i++)
		a[i] = 0;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		for(int k=0;k<2;k++)
		{
			cin>>p;
			for(int j=0;j<16;j++)
			{
				cin>>temp;
				if(j>=4*(p-1) && j<4*p)
				{
					a[temp-1]++;
				}
			}
		}
		count=0;
		for(int j=0;j<16;j++)
		{
			if(a[j]==2)
			{
				value = j+1;
				count++;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(count == 1)
		{
			cout<<value<<endl;
		}
		else if(count > 1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else if(count==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		for(int j=0;j<16;j++)
		a[j] = 0;
	}
	return 0;
}