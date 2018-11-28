#include <iostream>
#include <cstdio>
using namespace std;
int a[5][5];
int mark[20];
void makezero()
{
	for(int i=1;i<=20;i++)
		mark[i]=0;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,t,b,c,d,e,n,m;
	bool check;
	int ans;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>a[i][j];
		makezero();
		for(i=1;i<=4;i++)
			mark[a[n][i]]++;
		cin>>n;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>a[i][j];
		for(i=1;i<=4;i++)
			mark[a[n][i]]++;
		check=false;
		ans=0;
		for(i=1;i<=16;i++)
			if(mark[i]==2)
			{
				if(ans!=0)
					check=true;
				ans=i;
			}
		if(ans==0)
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else
			if(check==true)
				cout<<"Case #"<<k<<": Bad magician!"<<endl;
			else
				cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}



		

