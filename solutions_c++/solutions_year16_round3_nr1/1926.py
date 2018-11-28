#include <iostream>
#include<cstdio>
#include<utility>
#include<algorithm>
using namespace std;
#define mp make_pair
//int a[26];
typedef pair<int,int> pii;
pii a[26];
int main() {
	// your code goes here
//freopen("A-large.in", "r",stdin);
//	freopen("first3big.txt", "w",stdout);
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		int n,val;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&val);
			a[i]=mp(val,i);
		}
		sort(a,a+n);
		while(1)
		{
			if(a[n-1].first==0)
			{
				break;
			}
			if(n>2 && a[n-1].first==a[n-2].first && a[n-2].first==a[n-3].first){
					a[n-1].first-=1;
				cout<<(char)(a[n-1].second+65)<<" ";
				
			}
			else if(a[n-1].first==a[n-2].first)
			{
			a[n-1].first-=1;
			a[n-2].first-=1;
			cout<<(char)(a[n-1].second+65)<<(char)(a[n-2].second+65)<<" ";
			}
			else
			{
				a[n-1].first-=1;
				cout<<(char)(a[n-1].second+65)<<" ";
			}
			sort(a,a+n);
			// for(int i=0;i<n;i++)
			// {
			// 	cout<<a[n-1].first<<" ";
			// }
			// cout<<"\n";
		}
		cout<<"\n";
	}
	
	return 0;
}
