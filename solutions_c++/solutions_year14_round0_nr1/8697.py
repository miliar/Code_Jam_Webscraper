#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int t,n1,n2,temp,ans;
	int a[4];
	a[0]=0;a[1]=0;a[2]=0;a[3]=0;
	int count=0;
	cin>>t;
	for (int i=0; i<t; i++)
	{
		int index=0;
		cin >>n1;
		for (int j=0; j<16; j++)
		{
			cin >>temp;
			if (j>=4*(n1-1) && j<4*n1) {a[index]=temp;index++;}
		}
		cin>>n2;
		for (int j=0; j<16; j++)
		{
			cin >>temp;
			if(j>=4*(n2-1) && j<4*n2)
			if (temp==a[0] || temp==a[1] || temp==a[2] || temp==a[3]) {count++;ans=temp;}
		}
		if (count==0) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if (count==1) cout<<"Case #"<<i+1<<": "<<ans<<endl;
		else cout<<"Case #"<<i+1<<": Bad magician!"<<endl;;
		count=0;
	}
}
