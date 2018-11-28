#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)
#define pr(a) printf("%d",a)
#define prn(a) printf("%d\n",a)
#define scll(a) scanf("%lld",&a)
#define prll(a) printf("%lld",a)
#define prlln(a) printf("%lld\n",a)
typedef long long LL;
struct w {
	int n[3];
};
int num = 0;
string ans1;
w getans(int n, int cur) {
	if(n==0) {
		w x;
		x.n[0] = x.n[1]= x.n[2] = 0;
		x.n[cur] = 1;
		ans1.pb(cur);
		return x;
	}
	w x;
	x.n[0] = x.n[1]= x.n[2] = 0;
	w x1 = getans(n-1, cur);
	w x2 = getans(n-1, (cur+1)%3);
	repi(i,0,3) x.n[i] = x1.n[i] + x2.n[i];
	return x;
}
void sort1(string& a, int l, int n) {
	if(n==0) return;
	sort1(a,l,n-1);
	sort1(a,l + (1<<(n-1)),n-1);
	int b = 0;
	for(int i=l;i<l + (1<<(n-1));++i) {
		int r = i + (1<<(n-1));
		if(a[i] == a[r]) continue;
		if(a[i] < a[r]) break;
		b = 1;
		break;
	} 
	if(b) {
		for(int i=l;i<l+(1<<(n-1));++i) {
			int r = i + (1<<(n-1));
			swap(a[i],a[r]);
		}
	}
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	repi(tt,1,t+1) {
		string best="9";
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		w ans[3];

		repi(i,0,3) {
			ans1.clear();
			ans[i] = getans(n,i);
			if(ans[i].n[0]==p 
				&& ans[i].n[1]==r
				&& ans[i].n[2]==s) {
				sort1(ans1,0,n);
				best = min(best, ans1);
			}
		}
		for(char& x: best) {
			if(x==0) x = 'P';
			if(x==1) x='R';
			if(x==2) x='S';
		}
		if(best == "9") best = "IMPOSSIBLE";
		cout<<"Case #"<<tt<<": "<<best<<endl;
	}
	return 0;
}