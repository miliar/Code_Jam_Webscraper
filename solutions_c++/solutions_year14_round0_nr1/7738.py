#include<fstream>
#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{

ifstream in;
ofstream ou;
int t,i,j,status,val,n=1;
int row1,row2,arr1[4][4],arr2[4][4];

in.open("A-small-attempt1.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("A-small.txt",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>t;
cout<<t;
while(n<=t)
{
status=0;	
ou<<"Case #"<<n<<": ";
in>>row1;
//cout<<row1;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
in>>arr1[i][j];
in>>row2;
//cout<<row2;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
in>>arr2[i][j];

for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
	
	if(arr1[row1-1][i]==arr2[row2-1][j])
	{
		status=status+1;
		val=arr1[row1-1][i];
//		cout<<"\n\""<<val<<"\"\n";
	}	
}


if(status==1)
ou<<val<<"\n";
else if(status>=2)
ou<<"Bad magician!\n";
else
ou<<"Volunteer cheated!\n";
n++;
}

in.close();
ou.close();
return 0;

}
