#include <bits/stdc++.h>
#define ll long long
#define sc(a) scanf("%lld", &a)
#define pr(a) printf("%lld\n", a)

using namespace std;

char str[105];
/*
ll call(ll in)
{
	ll st,i;
	if (in == 0) return 1;
	if (in < 0) return 0;
	if (str[0] == '-') {
		for (st = 0, i = in; i >= 0; st++, i--) {
			tem[st] = str[i];
			if (tem[st] == '+') tem[st] = '-';
			else tem[st] = '+';
		}
		for (st = 0; st <= in; st++) {
			str[st] = tem[st];
		}
		while (in >= 0 && str[in] == '+')
			in--;
		return 1+call(in);
	}
	else {
		str[0] = '-';
		for (st = 0, i = in; i >= 0; st++, i--) {
			tem[st] = str[i];
			if (tem[st] == '+') tem[st] = '-';
			else tem[st] = '+';
		}
		for (st = 0; st <= in; st++) {
			str[st] = tem[st];
		}
		while (in >= 0 && str[in] == '+')
			in--;
		return 2+call(in);
	}
}*/

ll check(string st)
{
	ll len = st.length();
	for (ll i = 0; i < len; i++)
		if (st[i] == '-') return 0;
	return 1;
}

ll call(ll len)
{
	char tem;
	queue<pair<string, int> > Q;
	map<string, int> vis;
	string a,b;
	ll dep,i,st,en;
	a = str;
	if (check(a)) {
		return 0;
	}
	Q.push(make_pair(a, 0));
	vis[a] = 1;
	while (1) {
		dep = Q.front().second;
		b = Q.front().first;
		Q.pop();
		for (i = 0; i < len; i++) {
			a = b;
			for (st = 0, en = i; st <= en; st++, en--) {
				tem = a[st];
				a[st] = a[en];
				a[en] = tem;
			}
			for (st = 0; st <= i; st++) {
				if (a[st] == '+') a[st] = '-';
				else a[st] = '+';
			}
			if (check(a)) {
				return dep+1;
			}
			else if (vis[a] == 0){
				vis[a] = 1;
				Q.push(make_pair(a, dep+1));
			}
		}
	}
}

int main()
{
	ll ans,cur,z,i,j,k,l,m,n,ct,t;
//	cout << "here\n";
	freopen("B-small-attempt2.in", "r", stdin);
//	cout << "there\n";
	freopen("opt.txt", "w", stdout);
//	cout << "where\n";
	sc(t);
	for (z = 1; z <= t; z++) {
		//cout << z << endl;
		scanf("%s", str);
		ans = call(strlen(str));
		printf("Case #%lld: %lld\n", z, ans);
	}

 	return 0;
}

