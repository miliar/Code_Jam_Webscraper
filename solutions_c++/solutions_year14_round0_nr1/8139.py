
#include <iostream>
using namespace std;

int main() {
	
	int t,f1,f2,i,j,c=0,x,r;
	int a[5][5],b[5][5];
	cin>>t;
	x=1;
	while(t--)
{
	c=0;
	cin>>f1;
	for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	cin>>a[i][j];
	}
	}
	cin>>f2;
	for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	cin>>b[i][j];
	}
	}
	for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	if(a[f1-1][i]==b[f2-1][j])
	{c++; r=a[f1-1][i];}
	}
	}
	if(c==1)
	cout<<"Case #"<<x<<": "<<r<<"\n";
	else if(c==0)
	cout<<"Case #"<<x<<": "<<"Volunteer cheated!\n";
	else
	cout<<"Case #"<<x<<": "<<"Bad magician!\n";
	x++;
}
	
	return 0;
}