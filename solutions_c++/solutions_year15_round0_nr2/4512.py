#include<bits/stdc++.h>
#define ll long long int
using namespace std;
ll poo(vector<ll> temp, ll sec)
{
		//cout<<sec;
	int y;
	/*for(y=0; y<temp.size(); y++)
		cout<<temp[y]<<" ";
	cout<<endl;*/
	sort(temp.begin(), temp.end());
	ll sz=temp.size();
	ll x=temp[sz-1];
	if(x<=2)
		return sec+x;
	vector<ll> a, b;
	a=temp;
	b=temp;
	for(int i=0;i<sz;i++)
		temp[i]--;
	ll ans=poo(temp, sec+1);
	int i;
	for(i=(x/2)-1; i<=(x/2); i++)
	{
		std::vector<ll> v = a;
		if(i<=1 || x-i<=1)
			continue;
		v.pop_back();
		v.push_back(i);
		v.push_back(x-i);
		ans = min(ans, poo(v,sec+1));

	}
	
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	ll t, ca, i;
	cin>>t;
	for(ca=1;ca<=t;ca++)
	{
		ll n;
		cin>>n;
		vector<ll> v;
		ll temp;
		for(i=0;i<n;i++)
		{
			cin>>temp;
			v.push_back(temp);
		}
		ll ans=poo(v, 0);
		cout<<"Case #"<<ca<<": ";
		cout<<ans<<"\n";
	}
}