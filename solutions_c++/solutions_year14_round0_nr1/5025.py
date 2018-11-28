#include <iostream>
using namespace std;

int main() {
	int s[4][4],r[4][4],a,b,d,g;
cin>>d;
for(int i=0;i<d;i++)
{
	int c=0;
cin>>g;
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
cin>>s[j][k];
}}
cin>>a;
for(int l=0;l<4;l++)
{
for(int m=0;m<4;m++)
{
cin>>r[l][m];
}}
for(int p=0;p<4;p++)
{
for(int q=0;q<4;q++)
{
if(s[g-1][p]==r[a-1][q])
{
b=s[g-1][p];
c++;
}}
}
if(c==1)
cout<<"\nCase #"<<i+1<<": "<<b;
else 
if (c>1)
cout<<"\nCase #"<<i+1<<": Bad magician!";
else
if(c==0)
cout<<"\nCase #"<<i+1<<": Volunteer cheated!";
}
	return 0;
}