#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <utility>
#define pii pair<int, int>
#define VI vector < int >
#define PB push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORD(i,a,b) for(i=a;i>b;i--)
typedef long long LL;
using namespace std;
int main()
{
	int i,j,k,n,t,r1,r2;
	cin>>t;
	int a[5][5];
	int a1[5][5];
	int b[20]={0};
	int nn=t;
	while(t--)
	{
		for(i=0;i<20;i++)
			b[i]=0;
		cin>>r1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{	
				cin>>a[i][j];
				if(i==r1-1)
					b[a[i][j]]++;
			}
		int ans=0,aabhas;
		cin>>r2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{	
				cin>>a[i][j];
				if(i==r2-1)
					if(b[a[i][j]]>0)
					{	
						ans++;
						aabhas=a[i][j];
					}
			}
		cout<<"Case #"<<nn-t<<": ";
		if(ans==0)
			cout<<"Volunteer cheated!\n";
		else if(ans==1)
			cout<<aabhas<<endl;
		else 
			cout<<"Bad magician!\n";
	}
	return 0;
}

