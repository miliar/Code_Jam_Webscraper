#include<bits/stdc++.h>
using namespace std;
bool check(int a[],int n,int m)
{
	int c=0,s=1,f=1000;
	for(int k=1;k<=1000&&k<=m;k++){
		int z=0;
		for(int i=0;i<n;i++)
		{
			z+=((a[i]-1)/k);
		}
		if(k+z<=m)return true;
	}
	return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int a[1000];
	for(int T=0;T<t;T++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
		sort(a,a+n);
		int s=0,f=1000;
		while(s<=f)
		{
			int m=(s+f)>>1;
			if(check(a,n,m))
			f=m-1;
			else
			s=m+1;
		}
		cout<<"Case #"<<T+1<<": "<<s<<endl;
	}
	return 0;
}