#include<iostream>
#include<iomanip>
#include<math.h>
#include<sstream>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
int T,n,m,flag,ans[10002],a[101][101],sub[101][101],tem;
cin>>T;
for(int i=0;i<T;i++)
{
	cin>>n;
	cin.ignore(256,' ');
	cin>>m;
	cin.ignore(256,'\n');
	for(int j=0;j<n;j++)
	for(int k=0;k<m;k++)
	cin>>a[j][k];
	int max=a[0][0];
	for(int j=0;j<n;j++)
	for(int k=0;k<m;k++)
	{if(max<a[j][k])max=a[j][k];}
	
	
	for(int j=0;j<n;j++)
	for(int k=0;k<m;k++)
	a[j][k]=max-a[j][k];
if(n==1||m==1)
ans[i]=1;
else{	

	do{
	for(int j=0;j<n;j++)
	for(int k=0;k<m;k++)
	sub[j][k]=0;


	flag=0;
	for(int j=0;j<n;j++)
	{
	if(!((a[j][0]==0)||(a[j][m-1]==0)))
	{tem=0;
	for(int k=0;k<m;k++)
	if(a[j][k]==0){tem=1;break;}
	if(!tem)
	for(int k=0;k<m;k++)
	{sub[j][k]=1;flag=1;}
	}
	}


	for(int k=0;k<m;k++)
	{
	if(!((a[0][k]==0)||(a[n-1][k]==0)))
	{tem=0;
	for(int j=0;j<n;j++)
	if(a[j][k]==0){tem=1;break;}
	if(!tem)
	for(int j=0;j<n;j++)
	{sub[j][k]=1;flag=1;}
	}
	}



	if(flag){
		for(int j=0;j<n;j++)
		for(int k=0;k<m;k++)
		a[j][k]=a[j][k]-sub[j][k];
		}






	}while(flag);

	int temp=1;
	for(int j=0;j<n;j++){
	if(!temp)break;
	for(int k=0;k<m;k++)
	if(a[j][k]!=0){ans[i]=0;temp=0;break;}
	}	
	if(temp)ans[i]=1;
}
}
for(int i=0;i<T;i++)
if(ans[i])
cout<<"Case #"<<(i+1)<<": "<<"YES\n";
else
cout<<"Case #"<<(i+1)<<": "<<"NO\n";
return 0;
}
