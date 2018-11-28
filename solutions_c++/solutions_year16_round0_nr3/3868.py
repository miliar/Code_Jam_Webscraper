#include <bits/stdc++.h>
using namespace std;

long long a[15];
int ct=0,ar[20],b[15];

bool prim(long long x,int base){
	int sq=(int)sqrt(x);
	for (int i=2;i<=sq;i++){
		if (!(x%i)){b[base]=i; return false;}
	}
	return true;
}

void rec(int pos){
	if (ct==50) return;
	if (pos>14){
		bool ok=true;
		for (int i=2;i<=10;i++){
			long long now=0;
			for (int j=1;j<=14;j++){
				now*=i; now+=ar[j];
			}
			ok&=(!prim(now*i+a[i]+1,i));
			if (!ok) break;
		}
		if (ok){
			cout << 1;
			for (int i=1;i<=14;i++) cout << ar[i];
			cout << "1 ";
			for (int i=2;i<=10;i++){
				cout << b[i] << (i==10 ? "\n" : " ");
			}
			ct++;
		}
	}else{
		ar[pos]=0; rec(pos+1); ar[pos]=1; rec(pos+1);
	}
}

int main(){
	freopen("jamcoin.out","w",stdout);
	ios::sync_with_stdio(0); cin.tie(0);
	for (int i=2;i<=10;i++){
		a[i]=1;
		for (int j=1;j<=15;j++) a[i]*=i;
	}
	cout << "Case #1:\n";
	rec(1);
}
