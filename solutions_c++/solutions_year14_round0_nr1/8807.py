#include<iostream>
using namespace std;
int main()
{
	int a[5][5],b[5][5];
	int i,j,k,c1,c2,t,p,count=1;
	cin>>t;
	while(count<=t)
	{
		k=0;
		cin>>c1;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
        		cin>>a[i][j];
		cin>>c2;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
        		cin>>b[i][j];
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		if(a[c1][i]==b[c2][j])
		{
			p=i;
			k++;
		}
		if(k==1)
		cout<<"Case #"<<count<<": "<<a[c1][p]<<"\n";
		if(k>1)
		cout<<"Case #"<<count"<<"Bad magician!\n";
		if(k<1)
		cout<<"Case #"<<count"<<"Volunteer cheated!\n";
		count++;
	}
	return 0;
}
