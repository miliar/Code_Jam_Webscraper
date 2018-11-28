#include <bits/stdc++.h>
using namespace std;
#define ll

ifstream inf("test.txt");
ofstream of("out.txt");

ll int n=16;
ll int p[11][33];
ll int c=0;

int check(ll int x){
	int f[11];
	for(int b=2;b<=10;b++){
		ll int v=0;
		for(int i=0;i<n;i++){
			ll int temp = (x&(1<<i))==0?0:1;
			v+=(temp*p[b][i]);
		}
		ll int t=v;
		ll int j=2;
		ll int sq = sqrt(t);
		while(j<=sq){
			if (t%j==0){
				f[b] = j;
				break;
			}
			j++;
		}
		if (j>sq) return 0;
	}
	for(int i=n-1;i>=0;i--){
		if (x&(1<<i)) cout << 1;
		else cout << 0;
	}
	cout << " ";
	for(int i=2;i<=10;i++) cout << f[i] << " ";
	cout << endl;
	//cout << c <<" " << endl;
	c++;
	return 0;
}

int main(){
	for(int i=2;i<=10;i++){
		p[i][0] = 1;
		for(int j=1;j<n;j++) p[i][j] = p[i][j-1]*i;
	}
	ll int s = pow(2,n-1)+1;
	ll int l = pow(2,n)-1;
	while(s<l){
		check(s);
		s+=2;
		if (c==50) break;
	}
	return 0;
}
