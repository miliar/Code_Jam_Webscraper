#include <bits/stdc++.h>

#define fi first
#define se second
#define ll long long
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

using namespace std;

int t, d, p[10009], ans, h = 1;

multiset <int> S, emp;

void tap(int last, int sz)
{
	ans = min(ans, sz+last);
	
	if (last == 1)
		return;
	
	S.erase(S.find(last));
	
	if (last%2 == 0)
	{
		S.insert(last/2);
		S.insert(last/2);
		tap(*(--S.end()), sz+1);
		S.erase(S.find(last/2));
		S.erase(S.find(last/2));
	}
	else
	{
		int a = last/2;
		int b = last/2+1;
		
		b++, a--;
		
		if (a!=0)
		{
			S.insert(last/2+1);
			S.insert(last/2);
			tap(*(--S.end()), sz+1);
			S.erase(S.find(last/2+1));
			S.erase(S.find(last/2));
			
			S.insert(a);
			S.insert(b);
			tap(*(--S.end()), sz+1);
			S.erase(S.find(a));
			S.erase(S.find(b));
		}
		else
		{
			S.insert(last/2+1);
			S.insert(last/2);
			tap(*(--S.end()), sz+1);
			S.erase(S.find(last/2+1));
			S.erase(S.find(last/2));
		}
	}
	
	S.insert(last);
}

int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	cin >> t;
	
	while (t--)
	{
		cin >> d;
		
		ans = 0;
		
		S = emp;
		for (int i = 0; i < d; i++)
			cin >> p[i], ans = max(ans, p[i]), S.insert(p[i]);
		
		tap(*(--S.end()), 0);
		
		printf("Case #%d: %d\n", h, ans), h++;
	}
}
