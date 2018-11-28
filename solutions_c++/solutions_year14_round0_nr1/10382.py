#include <iostream>
#include<stdio.h>

using namespace std;
int T,Q,ans,it,a[10][10],b[10][10],i,j,x,y;
int main() {

	freopen("q.txt","r",stdin);
freopen("ans.txt","w",stdout);

	cin>>T;
	for(it=1;it<=T;it++)
	{
		cin>>x;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		cin>>a[i][j];
		
		
		
		cin>>y;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		cin>>b[i][j];

	Q=false;
	for(i=1;i<=4;i++)
	for(j=1;j<=4;j++)
	if(a[x][i]==b[y][j])
	{
		if(Q==false)
		{
			Q=true;
			ans=a[x][i];
		}
		else
		Q=3;
	}
	
	if(Q==3)
	cout<<"Case #"<<it<<": Bad magician!"<<endl;
	else if(Q==0)
		cout<<"Case #"<<it<<": Volunteer cheated!"<<endl;
	else
	cout<<"Case #"<<it<<": "<<ans<<endl;

	}
	
	
	return 0;
}





/*#include<iostream>
#include<vector>
using namespace std;
long long  a,b,y,i,r,l,d[2500][2500],n,m,j,x,rem=1000000007,sum;
vector<int> v[2500];

long long f(int n,int k)
{
	if(d[n][k])
		return d[n][k];
	long long sum=0;
	
	//sum=f(n-1,k);
	
	for(int i=1;i<k;i++)
		for(int j=0;j<v[n].size();j++)
			{
				sum+=f(v[n][j],i);
				sum=sum%rem;
			}
		
		sum++;
		sum=sum%rem;

		d[n][k]=sum;
		return sum;
}
int main()
{
	int n,k;
	///d[n][k]
//	for(i=1;i<=2000;i++)
//		d[i][1]=1;
	//for(i=1;i<=2000;i++)
	//	d[1][i]=1;

	for(k=1;k<=2000;k++)
		for(n=1;n<=2000;n++)
		{
			d[n][k]++;
		
			for(x=n+n;x<=2000;x+=n)
				for(int u=k+1;u<=2000;u++)
				d[x][u]+=d[n][k];
		}
//	cout<<d[6][1]<<endl;
		/*
	for(x=1;x<=2000;x++)
		for(i=x+x;i<=2000;i+=x)
			v[i].push_back(x);
	////////////////////////////////
	//while(cin>>n>>k){
	
		
		for(i=1;i<=9;i++)
		{
			cout<< "n="<<i<< "   ";
			for(j=1;j<=10;j++)
				cout<<d[i][j]<<" ";
			cout<<endl;
		}
		cout<<"pooh"<<endl;

//	cin>>n>>k;
	long long x=0;
for(n=1;n<10;n++)
{
	x=0;
	cout<<"n="<<n<<"   ";
	for(int j=1;j<10;j++)
	{

	for(i=1;i<=n;i++)
	{
		x+=d[i][j];
		x=x%rem;
	}

	cout<<x<<" ";//<<endl;
//	}
	}
	cout<<endl;
}
	return 0;
}*/