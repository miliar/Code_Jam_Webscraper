#include <bits/stdc++.h>

using namespace std;

#define loop(i,j,n) for(int i=(j); i<(n);i++)
#define ll long long
#define all(x) x.begin(),x.end()
#define SZ(x) ((int)((x).size()))
#define PB push_back
#define VI vector<int>
#define LLVI vector<long long int>
#define VS vector<string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main()
{
	READ("A-small-attempt1.in");
	WRITE("A-small-attempt1.out");

	ll t;

	cin>>t;
	int s,count1,n;
	string r;
	for(int re=1;re<=t;re++){
			count1=0;
			n=0;
			cin>>s>>r;
			for(int i=0;i<r.length();i++)
			{
				if(i>count1&&r[i]!='0')
				{
					n=n+i-count1;
					count1=count1+r[i]-'0'+n;
				}
				else if(i<=count1&&r[i]!='0')
					count1=count1+r[i]-'0';
			}
			cout<<"Case #"<<re<<": "<<n<<endl;
	}
}
