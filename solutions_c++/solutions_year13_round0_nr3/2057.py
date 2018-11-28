#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

bool est_pal(ll nb)
{
	vector<int> dec;
	while(nb > 0)
	{
		dec.push_back(nb % 10);
		nb /= 10;
	}
	for(int i = 0; i < dec.size(); i++)
	{
		if(dec[i] != dec[dec.size() -1-i])
			return false;
	}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	vector<ll> nbs;

	for(ll i = 1; i <= 10000000; i++)
	{
		ll carre = i*i;
		if(est_pal(carre) && est_pal(i))
		{
			nbs.push_back(carre);
		}

	}
	for(int g=0; g<t; g++)
	{		
		ll a,b;
		scanf("%lld%lld", &a,&b);
		ll cpt=0;
		int debut1 = -1, fin1 = nbs.size(), debut2 = -1, fin2 = nbs.size();
		while(fin1 - debut1 > 1)
		{
			int milieu = (debut1 + fin1)/2;
			if(nbs[milieu] < a)
				debut1 = milieu;
			else
				fin1 = milieu;
		}
		while(fin2 - debut2 > 1)
		{
			int milieu = (debut2 + fin2)/2;
			if(nbs[milieu] > b)
				fin2 = milieu;
			else
				debut2 = milieu;
		}
		printf("Case #%d: %d\n", g+1, fin2 - fin1);
	}
	return 0;
}
