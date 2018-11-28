#include<iostream>
#include<conio.h>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<cstdio>
#define ull unsigned long long
#define sz (int)1e7
using namespace std;
vector<int> vcc;
int arr[sz];
void solve()
{
	int ans=0,sum=0;
	int n;
	cin>>n;
	string a;
	cin>>a;
	for(int i=0;i<=n;i++)
	{
		if(sum<i && a[i]!='0')
		{
			ans=ans+(i-sum);
			sum=sum+(i-sum);
		}
		sum+=(a[i]-'0');
	}
	cout<<ans;
}


int main()
{
	
	
	
//	freopen("input.in","r",stdin);
//	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}
