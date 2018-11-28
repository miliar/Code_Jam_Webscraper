#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define sz(a) ((int)((a).size()))
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define fv(a,b) for(__typeof(a.begin()) b = (a).begin(); b != (a).end(); ++b)
#define all(a) a.begin(),a.end()
#define min(a,b) a<b? a:b

using namespace std;
typedef long long LL;
typedef vector <int> VI;
typedef pair< int ,int > PII;
int main()
{
	int t;
	cin>>t;int x=1;
	while(t--)
	{
	int sm;int c=0;
	cin>>sm;
	string s;
	int sum=0;
	cin>>s;
	rep(i,sm+1)
	{

	    //cout<<(int)(s[i]-'0');
	    int k=(int)(s[i]-'0');
	    if(sum<i)
            {c++;
                sum++;
                }
        sum+=k;
	}
	cout<<"Case #"<<x<<": "<<c<<"\n";
	x++;
	}
	return 0;
}
