/*	 Hello World!	*/

#include <bits/stdc++.h>

#define pb push_back
#define pf push_front
#define mp make_pair
#define f first
#define s second
#define let(x,a) __typeof(a) x(a)
#define all(a) (a).begin(),(a).end() 
#define endl '\n'
#define present(c,x) ((c).find(x) != (c).end()) 
#define tr(v,it) for( let(it,v.begin()) ; it != v.end() ; it++)
#define rtr(v,it) for( let(it,v.rbegin()) ; it != v.rend() ; it++)
#define rep1(i,n) for(int i=0; i<(int)n;i++)
#define rep2(i,a,b) for(int i=(int)a; i<=(int)b; i++)

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#define LL long long int
#define PII pair<int,int>
#define VI vector<int>
#define inf INT_MAX

using namespace std;

void FastIO()
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
}

int main()
{
	FastIO();
	int t,ans;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		ans=0;
		cout<<"Case #"<<i<<": ";
		reverse(all(s));
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='-')
			{
				ans++;
				if(s[s.length()-1]=='+')
				{
					for(int k=s.length()-1;k>=j;k--)
					{
						if(s[k]=='+') s[k]='-';
						else break;
					}
					ans++;
				}
				reverse(s.begin()+j,s.end());
				for(int k=j;k<s.length();k++)
				{
					if(s[k]=='-')
					{
						s[k]='+';
					}
					else
					{
						s[k]='-';
					}
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}