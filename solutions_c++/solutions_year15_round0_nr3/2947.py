//----------------------JUGNU---------------------------//
#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define vt(a) vector <ll> a
#define st(a) set <ll> a
#define sti(a) set <ll>::iterator a
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%lld",&a)
#define sm(a,b) scanf("%lld%lld", &a, &b)
#define pr(a) printf("%lld\n", a)
#define pm(a,b) printf("%lld %lld\n", a, b)
#define cn(a) cin >> a
#define ct(a) cout << a << endl
#define isset(x,i) ((x>>i)&1)
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
using namespace std;
ll mult[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
ll check(ll x, ll y)
{
	if(x==1 && y==1)
		return 1LL;
	if(x==1 && y==3)
		return 1LL;
	if(x==2 && y==1)
		return 1LL;
	if(x==2 && y==2)
		return 1LL;
	if(x==3 && y==2)
		return 1LL;
	if(x==3 && y==3)
		return 1LL;
	return 0LL;
}
char s[100000];
int main()
{
	ll i, j, t, n, m, k, l, x, r, sign, temp, indx1, indx2, left, right;
	int flag;
	sc(t);
	fre(j, 1, t)
	{
		left = right = -1LL;
		flag = 0;
		sign = 0LL;
		sm(l, x);
		scanf("%s", s);
		fr(i, l, l*x)
			s[i] = s[i-l];
		//printf("%s\n", s);
		indx1 = 0;
		fr(i, 0, l*x)
		{
			indx2 = s[i] - 'i' + 1LL;
			sign = sign + check(indx1, indx2);
			temp = mult[indx2][indx1];
			sign = sign%2;
			if(temp==1 && sign==0 && left==-1)
				left = i;
			indx1 = temp;
		//	cout << "index1: " << indx1 << "sign: " << sign << endl;
		}
		sign = sign%2;
		//cout << temp << " " << sign << endl;
		if(temp==0 && sign==1)
			flag = 1;
		//cout << flag << endl;
		if(flag==1)
		{
			indx1 = 0;
			sign = 0LL;
			frr(i, l*x-1, 0)
			{
				indx2 = s[i] - 'i' + 1LL;
				sign = sign + check(indx2, indx1);
				temp = mult[indx2][indx1];
				sign = sign%2;
				if(temp==3 && sign==0)
				{
					right = i;
					break;
				}
				indx1 = temp;
			}
			if((right==-1) || (left==-1) || ((right-left)<=1))
				flag = 0;
		}
		if(flag==1)
			printf("Case #%lld: YES\n", j);
		else
			printf("Case #%lld: NO\n", j);
	}
return 0;
}
