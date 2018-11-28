//header files
 
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;
 
//end of header files
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define FOR(i,n)                for(int i=0;i<n;i++)  
#define FOR2(i,n)                for(int i=1;i<=n;i++)  
#define inf 1000000000
#define   M 1000000007
 
#define maxn 1000000
#define maxt 100000
typedef long long int LL;
typedef long long int lld;
typedef long int ld;
 
int main()
{
	freopen("AIn.txt","r",stdin);
	freopen("AOut.txt","w",stdout);	
	int test;
	
	cin>>test;
	int count = 1;
	while(test--)
	{
		int x,y;
		cin>>x;
		int a[5][5];
		x--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>y;
		int b[5][5];
		y--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
				
			}
		}
		int temp=0;
		int array[5]={0};
		for(int i=0;i<4;i++)
		{
			int t = a[x][i];
			for(int j=0;j<4;j++)
			{
				if(t==b[y][j])	
				{
					array[temp] = t;
					temp++;		
					break;
				}
			}
		}
		if(temp==1)
		{
			cout<<"Case #"<<count<<": "<<array[0]<<endl;
		}
		else if(temp==0)
		{
			cout<<"Case #"<<count<<": "<<"Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<count<<": "<<"Bad magician!"<<endl;
		}
		count++;
	}
	return 0;
}
