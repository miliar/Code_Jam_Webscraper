#include <bits/stdc++.h>
#include <cstring>
#ifndef ONLINE_JUDGE
#define gc getchar
#else
#define gc getchar_unlocked
#endif
#define ll long long
#define nl() printf ("\n")
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define pi(x) printf ("%d",x)
#define pl(x) printf ("%lld",x)
#define pc(x) printf ("%c",x)
#define ps(x) printf ("%s",x)
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)
#define repu(i,a,n,step) for (int i = a; i < n; i += step)
#define repd(i,a,n,step) for (int i = a - 1; i >= n; i -= step)
using namespace std;
int readi () {
	int n=0,sign=0;
	char c=gc();
	while (c<48) {
		if (c==45) sign=1;
		c=gc();
	}
	while (c>47) {
		n=n*10+c-'0';
		c=gc();
	}
	if (sign) return (-n);
	return n;
}
ll readl () {
	ll n=0;int sign=0;
	char c=gc();
	while (c<48) {
		if (c==45) sign=1;
		c=gc();
	}
	while (c>47) {
		n=n*10+c-'0';
		c=gc();
	}
	if (sign) return (-n);
	return n;
}
int main() {
    ofstream out ("GCJ1.txt");
    int t,smax;
    string s;
    ll cnt=0,req=0;
    t = readi();
    repu(j,1,t+1,1) {
        smax = readi();
        cin>>s;
        int len = s.length();
        //cout<<s<<"\n";
        repu(i,0,len,1) {
            if (cnt >= i || s[i] < '1') {
        //        cout<<"c1:";
                cnt += (s[i]-'0');
            }
            else {
        //        cout<<"c2:";
                req += (i - cnt);
                cnt += (s[i]-'0' + i-cnt);
            }
        //    cout<<"i:"<<i<<" "<<cnt<<" "<<req<<"\n";
        }
        out<<"Case #"<<j<<": "<<req<<"\n";
        cnt = req = 0;
    }
return 0;
}
