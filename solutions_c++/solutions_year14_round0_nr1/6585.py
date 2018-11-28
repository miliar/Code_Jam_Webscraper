#include<iostream>
using namespace std;

int main()
{
	int n,a[4][4],b[4][4],e,t,temp,r1,r2,i,j;
	cin>>t;
	n=0;
	while(n++!=t)
	{
		temp = 0;
		cin>>r1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>a[i][j];
		cin>>r2;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>b[i][j];
		r1--;
		r2--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		if(a[r1][i]==b[r2][j])
		{
			temp++;
			e = a[r1][i];
			if(temp==2)
			break;
		}
		cout<<"Case #"<<n<<": ";
		if(temp == 0)
		cout<<"Volunteer cheated!";
		else if (temp==1)
		cout<<e;
		else
		cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}
