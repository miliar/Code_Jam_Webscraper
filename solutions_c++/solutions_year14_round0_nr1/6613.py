#include<bits/stdc++.h>
typedef long long int LL;
typedef unsigned long long int ULL;

#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 


#define SET(v, val) memset(v, val, sizeof(v))
#define mp(a,b)    make_pair(a,b)
#define pb(n)      push_back(n)
#define PI 3.14159265
#define F first
#define S second


template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }

using namespace std;

int main()
{
	int t,r1,r2,a,b,c,d,x=1;
	set<int> v1,v2;
	cin>>t;
	while(t--)
	{
		v1.clear();
		v2.clear();
		cin>>r1;
		for(int i=1;i<=4;i++)
		{
			cin>>a>>b>>c>>d;
			if(r1==i)
			{
				v1.insert(a);
				v1.insert(b);
				v1.insert(c);
				v1.insert(d);
			}
		}
		cin>>r2;
		for(int i=1;i<=4;i++)
		{
			cin>>a>>b>>c>>d;
			if(r2==i)
			{
				v2.insert(a);
				v2.insert(b);
				v2.insert(c);
				v2.insert(d);
			}
		}
		vector<int> ans;
		tr(v1,it)
		{
			tr(v2,it2)
			{
				if(*it == *it2)
					ans.pb(*it);
			}
		}
		if(ans.size()==1)
			cout<<"Case #"<<x<<": "<<ans[0]<<endl;
		else if(ans.size()==0)
			cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<x<<": "<<"Bad magician!"<<endl;
		//cout<<ans.size()<<endl;
		x++;
		ans.clear();
	}
	return 0;
}
