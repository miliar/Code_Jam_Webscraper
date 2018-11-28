#include <iostream>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
outer:{
cout<<"Case #"<<i<<": ";
int row1,row2;
int cards1[4][4],cards2[4][4];
cin>>row1;
row1--;
for(int j=0;j<4;j++)
	{
	for(int k=0;k<4;k++)
	{
		cin>>cards1[j][k];
	}
	}
	cin>>row2;
	row2--;
for(int j=0;j<4;j++)
        {
	        for(int k=0;k<4;k++)
		        {
			cin>>cards2[j][k];
		}
			
	}
int finl,flag=0;
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
if(cards1[row1][j]==cards2[row2][k])
{
if(flag==1)
{
cout<<"Bad magician!"<<endl;
i++;
goto outer;
}
else
{
flag=1;
finl=cards1[row1][j];
}
}}}
if( flag==0)
{
cout<<"Volunteer cheated!"<<endl;
}
else
{
cout<<finl<<endl;
}

}
return 0;
}
