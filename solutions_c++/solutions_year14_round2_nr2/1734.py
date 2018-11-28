#include<iostream>
using namespace std;
//---------------------------------

int x[1001][1001];

void preprocess()
{
	for(int i=0;i<=1000;i++)
	{
		for(int j=0;j<=1000;j++)
		{
			x[i][j]=i&j;
			
		}//cout<<endl;
	}
}
int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("code2.txt","w",stdout);
	
	preprocess();
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{

		int a,b,k;
		cin>>a>>b>>k;
		int count=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				//cout<<x[i][j]<<endl;
				if(x[i][j]<k)
					count++;
			}
		}
		cout<<"Case #"<<test<<": ";
		cout<<count<<endl;
	}
}
