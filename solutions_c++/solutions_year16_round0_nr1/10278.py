
#include <bits/stdc++.h>

using namespace std;

#define pb(x) push_back(x);
#define in(y) insert(y);
#define tt(t) while(t--)
#define itr ::iterator it;
#define ffitr(v) for(auto it = v.begins();it!=v.end();it++)
#define ll long long
#define vi vector<int>
#define ii pair<int, int>
#define vii vector<ii>
#define si set<int>
#define msi map<string, int>
#define newline printf("\n")
#define ff(n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()
#define PI 3.141
#define INF MAX_INT

int main ()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t_;
    cin>>t_;
    vector<ll> num(10,0);
    int c = 0;
    for(int t=1;t<=t_;t++)
    {
    	ll n;
    	cin>>n;
    	set<ll> s;
    	bool insomnia = false;
    	ll no = n;
    	for(ll i=1;true;i++)
    	{
    		if(s.find(n*i)!=s.end()){insomnia = true;break;}
    		no = n*i;
    		ll k = no;
    		while(k!=0)
    		{
    			int r = k%10;
    			if(num[r]==0)c++;
    			num[r]++;
    			k/=10;
    		}
    		if(c==10)break;
    		s.in(no);
    	}
    	if(insomnia){cout<<"Case #"<<t<<": "<<"INSOMNIA";newline;}
    	else {cout<<"Case #"<<t<<": "<<no; newline;}
    	c = 0;
    	ff(10)num[i]=0;
    }
    return 0;
}