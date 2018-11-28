#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define MAX 1000000007
#define f_i(st) freopen(st,"r",stdin);
#define f_o(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
	//f_i("B-large.in");
	//f_o("b-large-out.txt");
	int test,t;
	const int s = 2501;
	scan(test);
	for(t=1;t<=test;t++)
	{
		cout<<"Case #"<<t<<": ";
		int hash[s];
		int i,n;
		scan(n);
		vector<vector<int> > v(2*n);
		vector<int> res;
		fill(hash,0);
		//cout<<"declaration"<<endl;
		for(i=0;i<2*n-1;i++)
		{
		//	cout<<"In outer "<<n<<endl;
			for(int j=1;j<=n;j++)
			{
				int x;
				scan(x);
				v[i].pb(x);
				hash[x]++;
				//cout<<i<<" "<<j<<endl;
			}
		}
		for(i=0;i<s;i++)
		{
			if(hash[i]%2!=0)
			{
				res.pb(i);
			}
		}
	//	cout<<res.size()<<endl;
		sort(res.begin(),res.end());
		for(i=0;i<res.size();i++)
		{
			cout<<res[i]<<" ";
		}
		cout<<endl;
	}
 	return 0;
}


