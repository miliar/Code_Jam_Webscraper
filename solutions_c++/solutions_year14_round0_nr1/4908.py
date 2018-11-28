#include<iostream>
#include<stdio.h>
using namespace std;
int a[4][4],b[4][4];
int main()
{
	freopen("test.txt","w",stdout);
	int t;cin>>t;int m,n;
	int ii,i,j,k;
	for(ii=1;ii<=t;ii++)
	{
		bool visited[17];int answer=0;bool bad=false;
		for(i=1;i<=16;i++)visited[i]=0;
		cin>>m;
		m--;
		for(i=0;i<4;i++)for(j=0;j<4;j++)cin>>a[i][j];
		for(i=0;i<4;i++)
		visited[a[m][i]]=1;
		cin>>n;
		n--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)cin>>b[i][j];
		for(i=0;i<4;i++)
		{
			if(!visited[b[n][i]])visited[b[n][i]]=1;
			else if(answer==0)answer=b[n][i];
			else if(answer!=0)bad=true;
		}
		cout<<"Case #"<<ii<<": ";
		if(!bad && answer!=0)cout<<answer<<endl;
		else if(bad)cout<<"Bad magician!"<<endl;
		else if(answer==0)cout<<"Volunteer cheated!"<<endl;
	}
}
