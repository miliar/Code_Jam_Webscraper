#include <bits/stdc++.h>

#define debug(a)

using namespace std; 
typedef long double ld;

const ld eps = 1e-12;

bool equal(ld a, ld b)
{
	return abs(a - b) < eps;
}

int n;

ld V, X;
vector< pair<ld, ld> > v;

bool ok(ld t)
{
	debug( printf("ok(%Lf)\n", t); )
	multiset< pair<ld, ld> > dod, uj;
	ld fal = V;
	for(auto & i : v)
	{
		ld mv = min(V + 10, t * i.first);
		debug( printf("mv = %Lf\n", mv); )
		if(equal(i.second, X))
			fal -= mv;
		else if(i.second < X)
			dod.insert(make_pair(mv, X - i.second));
		else
			uj.insert(make_pair(mv, i.second - X));
	}
	while(fal > 0 && !equal(fal, 0))
	{
		if(dod.empty() || uj.empty())
			return false;
		pair<ld, ld> a = *dod.begin();
		dod.erase(dod.begin());
		pair<ld, ld> b = *uj.begin();
		uj.erase(uj.begin());

		debug( printf("mam (%Lf, %Lf), (%Lf, %Lf)\n", a.first, a.second, b.first, b.second); )

		ld temp = min(b.first * b.second, a.first * a.second);

		a.first -= temp / a.second;
		b.first -= temp / b.second;

		fal -= temp / a.second + temp / b.second;
		debug( printf("fal = %Lf\n", fal); )

		if(b.first * b.second < a.first * a.second)
			dod.insert(a);
		else
			uj.insert(b);
	}
	debug( printf(" = true\n"); )
	return true;
}

ld przyp()
{
	v.clear();
	scanf("%d%Lf%Lf", &n, &V, &X);
	ld a = 0.0, b = 0.0;
	for(int i = 0; i < n; i++)
	{
		ld r, c;
		scanf("%Lf%Lf", &r, &c);
		v.emplace_back(r, c);
		b = max(b, V / r + 5);
	}
	ld c;
	for(int i = 0; i < 10000; i++)
	{
		c = (a + b) / 2;
		if(ok(c))
			b = c;
		else
			a = c;
	}
	if(!ok(b))
		throw 1;
	return b;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		try{
			printf("%.10Lf\n", przyp());
		}
		catch(int x)
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
