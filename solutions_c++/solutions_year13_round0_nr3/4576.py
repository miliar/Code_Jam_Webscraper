#include <cmath>
#include <iostream>
using namespace std;
typedef long long ll;
ll a,b,tsts;
int c[20];
bool palin(ll x)
{
	int cou=0;
	while(x)
	{
		c[cou++]=x%10;
		x/=10;
	}
	for(int i=0;i<cou;i++)
		if(c[i]!=c[cou-1-i])
			return false;
	return true;
}
int main()
{
	cin >> tsts;
	for(int qq=1;qq<=tsts;qq++)
	{
		cin >> a >> b;
		ll ans=0;
		ll tmp;
		if(ll(sqrt(a))*ll(sqrt(a))==a)
			tmp=sqrt(a);
		else
			tmp=sqrt(a)+1;
		for(ll i=tmp;i*i<=b;i++)
			if(palin(i) && palin(i*i))
				ans++;
		cout << "Case #" << qq << ": " << ans << endl;
	}
	return 0;
}
