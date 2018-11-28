#include<iostream>
#include<stdio.h>
using namespace std;
int ini[100][100],cut[100][100];
int main()
{
	freopen("test.txt","w",stdout);
	int t;
	cin>>t;
	int i,j,k;
	for(i=1;i<=t;i++)
	{
		int n,m;
		cin>>m>>n;
		for(j=0;j<m;j++)for(k=0;k<n;k++)ini[j][k]=100;
		for(j=0;j<m;j++)for(k=0;k<n;k++)cin>>cut[j][k];
		//for(j=0;j<m;j++){for(k=0;k<n;k++)cout<<cut[j][k]<<" ";cout<<endl;}
		int max;
		for(j=0;j<m;j++)
		{
			max=cut[j][0];
			for(k=0;k<n;k++)if(cut[j][k]>max)max=cut[j][k];//cout<<max<<endl;
			for(k=0;k<n;k++)if(ini[j][k]>max)ini[j][k]=max;
		}
		for(j=0;j<n;j++)
		{
			max=cut[0][j];
			for(k=0;k<m;k++)if(cut[k][j]>max)max=cut[k][j];
			for(k=0;k<m;k++)if(ini[k][j]>max)ini[k][j]=max;
		}
		//for(j=0;j<m;j++)
		//{
		//	for(k=0;k<n;k++)cout<<ini[j][k]<<" ";
		//	cout<<endl;
		//}
		bool yes=true;
		for(j=0;j<m;j++){for(k=0;k<n;k++)if(cut[j][k]!=ini[j][k])yes=false;}
		cout<<"Case #"<<i<<": ";
		if(yes==true)cout<<"YES"<<endl;else cout<<"NO"<<endl;
	}
}
