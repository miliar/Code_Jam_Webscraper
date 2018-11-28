/* Coded by Mercury email:mercury200Hg@gmail.com */
#include<bits/stdc++.h>
#define ll long long
#define f(a,b,c) for(ll int i=a;i<b;i+=c)
using namespace std;
int b[1005];

void toint(int Smax,char a[1005]) { // Convert string to integer array
	for(int i=0;i<=Smax;i++) {
		b[i]=a[i]-'0';
	}
}
void update(int Smax,int in,int k) { // Update cumulative array from index in with factor of k
	for(int i=in;i<=Smax;i++) {
		b[i] += k;
	}
}

void p_array(int Smax) {
	for(int i=0;i<=Smax;i++) {
		cout << b[i] << " ";
	}
	cout << endl;
}

void solve(int Smax,int cas) {
	int ans=0;
	for(int i=1;i<=Smax;i++) { // Cumulative array
		b[i]=b[i]+b[i-1];
	}
	for(int i=1;i<=Smax;i++) {
		if(b[i-1]>=i) {
			//Do nothing
		}
		else {
			int k = abs(b[i-1]-i);
			b[i-1]+= k;
			ans+=k;
			update(Smax,i,k);
		}
	}
	printf("Case #%d: %d\n",cas,ans);
	//cout << ans << endl;
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	//freopen("A-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		int Smax;
		scanf("%d",&Smax);
		char a[Smax+5];
		scanf("%s",a);
		//freopen("A-large.out","a",stdout);
		if(Smax==0) {
			printf("Case #%d: 0\n",i);
		}
		else {
			toint(Smax,a);
			solve(Smax,i);
		}
	}
	return 0;
}

