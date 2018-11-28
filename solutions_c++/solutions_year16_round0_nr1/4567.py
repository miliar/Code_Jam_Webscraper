#include <bits/stdc++.h>
using namespace std;

int t,x,ct,now;
bool ok,a[15];

int main(){
	freopen("countsheep.in","r",stdin);
	freopen("countsheep.out","w",stdout);
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> x; ok=0; ct=1;
		if (!x){cout << "INSOMNIA\n"; continue;}
		memset(a,0,sizeof(a));
		while (!ok){
			now=ct*x;
			while (now){a[now%10]=1; now/=10;}
			ok=true;
			for (int i=0;i<=9;i++) ok&=a[i];
			ct++;
		}
		cout << (ct-1)*x << "\n";
	}
}
