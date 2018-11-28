#include<iostream>
#include<conio.h>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<cctype>
#include<iomanip>
using namespace std;
#define sz 10000000
#define ull unsigned long long
string key;
string target;
int maxi;
int tot;
int k,l,s;
int arr[10000000]={0};
char per[1000000];
void perm(int i)
{
	if(i>=s)
	{
		tot++;
		int match=0;
		for(int kk=0;kk<(s-l+1);kk++)
		{
			int f=1;
			for(int tps=0;(tps+kk)<(s) && (tps<l) ;tps++)
			{
				if(per[tps+kk]!=target[tps])
				{
					f=0;
//					cout<<"mis";
				}
			}
			if(f==1)
			{
				match++;
			}
		}
		arr[tot-1]=match;
//		cout<<match<<" "<<target<<" "<<arr[tot-1]<<endl;
		if(maxi<match)
		{
			maxi=match;
		}
	}
	else
	{
		for(int pp=0;pp<k;pp++)
		{
			per[i]=key[pp];
			perm(i+1);
		}
	}
}
void solve()
{
	cin>>k>>l>>s;
	cin>>key;
	cin>>target;
	maxi=0;
	tot=0;
	perm(0);
	float ans=0;
	for(int i=0;i<tot;i++)
	{
//		cout<<arr[i]<<" ";
		ans+=(maxi-arr[i]);
	}
	ans/=((double)(tot));
	printf("%0.7f",ans);
}
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}
