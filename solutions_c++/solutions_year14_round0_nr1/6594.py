#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
int t,k,i,j,ans;
int a[4][4];
int b[4][4];
int r1,r2;
cin>>t;
for(k=1;k<=t;k++)
{
int count=0;
printf("Case #%d: ",k);
int hash[17]={0};
cin>>r1;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		cin>>a[i][j];
for(i=0;i<4;i++)
hash[a[r1-1][i]]++;
cin>>r2;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		cin>>b[i][j];
for(i=0;i<4;i++)
hash[b[r2-1][i]]++;
for(i=1;i<=16;i++)
{
if(hash[i]==2) 
{count++; ans=i;}
}
if(count==1)
cout<<ans<<endl;
else if(count > 1)
cout<<"Bad magician!"<<endl;
else
cout<<"Volunteer cheated!"<<endl;
}
return 0;
}
