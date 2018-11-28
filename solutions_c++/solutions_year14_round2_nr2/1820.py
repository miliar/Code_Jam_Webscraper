

/**
AUTHOR:Rahul Shah
LINK:
WEBSITE:Codechef
PROBLEM:
**/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<cstring>
#include<stack>
#include<cstdlib>
using namespace std;
#define MOD 1000000007
#define ll long long
int arr[1005];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int a,b,k;
		cin>>a>>b>>k;
		for(int i=0;i<1005;i++)
			arr[i]=0;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
			{
				arr[i&j]++;
			}
		int cnt=0;
		for(int i=0;i<k;i++)
		{
			cnt+=arr[i];
		}
		cout<<"Case #"<<tc<<": "<<cnt<<endl;
	}
}
