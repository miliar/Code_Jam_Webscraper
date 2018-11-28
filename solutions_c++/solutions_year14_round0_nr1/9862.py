#include <iostream>
using namespace std;

int main() {
	int i,x;
	cin>>x;
	for(i=1;i<=x;++i)
	{
		int a[16],b[16],r1,r2,flag=0,j,num;
		cin>>r1;
		for(j=0;j<16;++j)
		{
			cin>>a[j];
		}
		cin>>r2;
		for(j=0;j<16;++j)
		{
			cin>>b[j];
		}
		for(j=(r1-1)*4;j<r1*4;++j)
		{
			for(int k=(r2-1)*4;k<r2*4;++k)
			{
				if(a[j]==b[k])
				{
					flag++;
					num=a[j];
				}
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<i<<": "<<num<<endl;
		}
		else if(flag>1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else if(flag==0)
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}

	return 0;
}
