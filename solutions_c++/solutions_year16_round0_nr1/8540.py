#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<string>
#include<climits>
#include <fstream>
#include<queue>
#include<cstdlib>
#include<iomanip>
#define rep(i,n) for(int i=0;i<n;i++)
#define repup(i,a,b) for(int i=a;i<=b;i++)
#define repdn(i,a,b) for(int i=b;i>=b;i--)
#define scd(n) scanf("%d",&n);
#define scl(n) scanf("%lld",&n);
#define scs(str) scanf("%s",str);
#define prdl(n) printf("%d\n",n);
#define prll(n) printf("%lld\n",n);
#define prd(n) printf("%d",n);
#define prl(n) printf("%lld",n);
#define pb push_back;
#define mp make_pair;
#define vi vector<int>;
#define vp vector< pair<int ,int> >;
typedef long long ll;
using namespace std;
ll mod=1e9+7;
int main()
{
	ofstream myfile;
	myfile.open ("example.txt");
	int t,n;
	cin>>t;
	
	repup(i,1,t)
	{
		cin>>n;
		bool c[10]={0};
		long long temp=n;
		bool flag=0;
		int k=1;
		while(flag==0 && n!=0)
		{
			temp=k*n;
			long long temp2=temp;
			vector <int> vect;
			while(temp2>0)
			{
				vect.push_back(temp2%10);
				temp2/=10;
			}
			for(int j=0;j<vect.size();j++)
				c[vect[j]]=1;
			flag=1;	
			for(int j=0;j<10;j++)
				{
					if(c[j]==0)
					{
						flag=0;
						break;
					}
						
				}
				k++;	
		}
		if(flag)
		myfile<<"Case #"<<i<<": "<<temp<<endl;
		else
		myfile<<"Case #"<<i<<": INSOMNIA"<<endl;
	}
	return 0;
}
