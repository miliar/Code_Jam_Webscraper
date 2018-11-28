#include <bits/stdc++.h>
using namespace std;

int t,n,a[25][15],x[2505];
bool o[15],ok;

void rec(int pos, int sisa){
	if (ok) return;
	if (pos==2*n){
		if (sisa) return;
		memset(x,0,sizeof(x));
		for (int i=1;i<2*n;i++){
			for (int j=1;j<=n;j++)
			x[a[i][j]]+=o[i]?1:-1;
		}
		vector<int> v;
		for (int i=1;i<=2500;i++){
			if (x[i]){
				if (x[i]<0) return;
				for (int j=1;j<=x[i];j++) v.push_back(i);
			}
		}
		if ((int)v.size()==n){
			sort(v.begin(),v.end());
			for (int i=0;i<n;i++)
			cout << v[i] << (i==n-1 ? "\n" : " ");
			ok=true;
		}
	}else{
		o[pos]=false; rec(pos+1,sisa);
		if (sisa){
			o[pos]=true; rec(pos+1,sisa-1);
		}
	}
}

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	freopen("rankfile.in","r",stdin);
	freopen("rankfile.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> n; ok=false;
		for (int i=1;i<2*n;i++){
			for (int j=1;j<=n;j++){
				cin >> a[i][j];
			}
		}
		rec(1,n);
	}
}
