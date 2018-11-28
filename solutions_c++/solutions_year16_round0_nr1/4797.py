#include <bits/stdc++.h>

using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)<0?-(x):(x))
#define pii pair<int,int>
#define m_p make_pair(n,m)
#define mod 1000000007
#define pb push_back
#define bp(x) __builtin_popcount(x)
typedef long long int ll;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);
	int t,n,i,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int i=1;
		ll num;
		set <int> s;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<z<<": INSOMNIA\n";
		}
		else
		{
			while(s.size()!=10)
			{
				num=i*n;
				while(num!=0)
				{
					s.insert(num%10);
					num/=10;
				}
				i++;
			}
			cout<<"Case #"<<z<<": "<<(i-1)*n<<"\n";
		}
	}
	return 0;
}
