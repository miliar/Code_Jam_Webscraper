#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <climits>
#include <bits/stdc++.h>
#define lli long long int
#define gc getchar_unlocked
#define get(t) scanf("%d",&t)
void scanint(int &x)
{
	register int c=gc();
	x=0;
	for(;c<48||c>57;c=gc());
	for(;(c>47&&c<58);c=gc()){x=(x<<1)+(x<<3)+c-48;}
}
int *val;
using namespace std;
int find1(int n)
{
	int ans=0;
	for(int i=0;i<n-1;i++)
		if(val[i]>val[i+1])
			ans+=val[i]-val[i+1];
	return ans;
}
int find2(int n)
{
	int gc=0;
	for(int i=0;i<n-1;i++)
		if(val[i]>val[i+1])
			gc=max(gc,val[i]-val[i+1]);
	int ans=0;
	for(int i=0;i<n-1;i++)
		ans+=(val[i]>gc?gc:val[i]);
	return ans;
}
int main()
{
	ifstream fin;
	ofstream fout;
	int t;
	cin>>t;
	int t1=1;
	while(t--)
	{
		int n;
		cin>>n;
		val=new int[n];
		for(int i=0;i<n;i++)
			cin>>val[i];
		int ans1=find1(n);
		int ans2=find2(n);
		printf("Case #%d: %d %d\n",t1++,ans1,ans2);
	}
	return 0;
}
