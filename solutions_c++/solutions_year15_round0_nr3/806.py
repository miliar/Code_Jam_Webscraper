#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;

const int mult[4][4]={
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4}
};

int mul(int a, int b)
{
	int res=mult[(a&3)][(b&3)];
	int sgn=((res&4)>0);
	sgn+=((a&4)>0);
	sgn+=((b&4)>0);
	sgn&=1;
	res&=3;
	if(sgn) return (res|4);
	else return res;
}

int t;
ll l;
ll x;
char str[10005];
int s[10005];
int pre[10005];
int post[10005];
pair<ll,ll> k1, k2;

pair<ll,ll> find_forw(int pre[10005], ll l, int c)
{
	int vis[88];
	for(int i=0; i<8; i++) vis[i]=0;
	int t[88];
	int rep=0;
	t[rep++]=0;
	vis[0]=1;
	while(!vis[mul(t[rep-1], pre[l-1])]) {
		vis[mul(t[rep-1], pre[l-1])]=1;
		t[rep++]=mul(t[rep-1], pre[l-1]);
	}
	for(int i=0; i<rep; i++) {
		if(t[i]==c) return make_pair(i, -1);
		for(ll j=0; j<l-1; j++) {
			if(mul(t[i], pre[j])==c) return make_pair(i, j);
		}
	}
	return make_pair(-1, -1);
}

pair<ll,ll> find_backw(int pre[10005], ll l, int c)
{
	int vis[88];
	for(int i=0; i<8; i++) vis[i]=0;
	int t[88];
	int rep=0;
	t[rep++]=0;
	vis[0]=1;
	while(!vis[mul(pre[0], t[rep-1])]) {
		vis[mul(pre[0], t[rep-1])]=1;
		t[rep++]=mul(pre[0], t[rep-1]);
	}
	for(int i=0; i<rep; i++) {
		if(t[i]==c) return make_pair(i, l);
		for(ll j=l-1; j>0; j--) {
			if(mul(pre[j], t[i])==c) return make_pair(i, j);
		}
	}
	return make_pair(-1, -1);
}

int exp(int b, ll e)
{
	int res=0;
	while(e) {
		if(e&1) res=mul(res, b);
		e>>=1;
		b=mul(b, b);
	}
	return res;
}

int main()
{
scanf("%d\n", &t);

for(int q=1; q<=t; q++) {
	scanf("%lld %lld\n", &l, &x);
	scanf("%s\n", str);
	for(int i=0; i<l; i++) {
		if(str[i]=='1') s[i]=0;
		else if(str[i]=='i') s[i]=1;
		else if(str[i]=='j') s[i]=2;
		else s[i]=3;
	}
	pre[0]=s[0];
	for(int i=1; i<l; i++) pre[i]=mul(pre[i-1], s[i]);
	post[l-1]=s[l-1];
	for(int i=l-2; i>=0; i--) post[i]=mul(s[i], post[i+1]);
	k1=find_forw(pre, l, 1);
	k2=find_backw(post, l, 3);
	if(k1.first==-1 || k2.first==-1) {
		printf("Case #%d: NO\n", q);
		continue;
	}
	if(k1.first*l+k1.second+1>=l*x-k2.first*l-(l-k2.second)) {
		printf("Case #%d: NO\n", q);
		continue;
	}
	ll between=x-k1.first-k2.first;
	if(k1.second>=0) between--;
	if(k2.second>=0) between--;
	between=max(between, 0LL);
	int j=0;
	if(l*x-k2.first*l-(l-k2.second)-(k1.first*l+k1.second)<4*l) {
		for(ll i=k1.first*l+k1.second+1; i<l*x-k2.first*l-(l-k2.second); i++) j=mul(j, s[i%l]);
	}
	else {
		j=exp(pre[l-1], between);
		if(k1.second>=0) j=mul(post[k1.second+1], j);
		if(k2.second<l) j=mul(j, pre[k2.second-1]);
	}
	if(j==2) {
		printf("Case #%d: YES\n", q);
	}
	else {
		printf("Case #%d: NO\n", q);
	}
}

	return 0;
}
