#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

int arr[1009];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,x=0;cin>>t;
	while(t--){
		int n;cin>>n;
		for(int i=0;i<n;++i)cin>>arr[i];
		int y=0,z=0,rate=0;

		for(int i=1;i<n;++i)if(arr[i]<arr[i-1])y+=arr[i-1]-arr[i],rate=max(rate,arr[i-1]-arr[i]);

		for(int i=0;i<n-1;++i)z+=min(arr[i],rate);

		cout<<"Case #"<<++x<<": "<<y<<" "<<z<<"\n";
	}
	return 0;
}
