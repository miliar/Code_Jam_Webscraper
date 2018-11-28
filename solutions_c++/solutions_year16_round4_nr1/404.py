#include<bits/stdc++.h>

using namespace std;

const int MAXN = 10000 + 10;

int a[20][MAXN]; 
char b[MAXN];

int n, R, P, S;
int f[100], g[100];
string s;

void Deal(int l, int r){
	if (r - l == 2){
		if (b[l] > b[l+1])
			swap(b[l], b[l+1]);
		return;
	}
	else{
		Deal(l, (l+r)>>1);
		Deal((l+r)>>1, r);
		int flag = 0;
		for(int i = l, j = (l + r) >> 1; j < r; i++, j++)
			if (b[i] != b[j]){
				if (b[i] > b[j])
					flag = 1;
				break;
			}
		if (flag){
			for(int i = l, j = (l + r) >> 1; j < r; i++, j++)
				swap(b[i], b[j]);
		}
	}
}

string Calc(int x){
	a[0][0] = x;
	for(int i = 1; i <= n; i++){
		int tt = 1 << i;
		for(int j = 0; j < tt; j++)
			a[i][j] = (a[i-1][j / 2] + j % 2) % 3;
	}
	int tt = 1 << n;
	for(int i = 0; i < 3; i++)
		g[i] = 0;
	for(int j = 0; j < tt; j++)
		g[a[n][j]]++;
	for(int i = 0; i < 3; i++)
		if (g[i] != f[i])
			return "miaomiaomiao?";
	for(int i = 0; i < tt; i++)
		if (a[n][i] == 0) b[i] = 'R';
		else if (a[n][i] == 1) b[i] = 'P';
		else b[i] = 'S';
	b[tt] = 0;
	Deal(0, tt);
	return string(b, b + tt);
}

int main(){
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);
	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		printf("Case #%d: ", o);
		cin>>n>>f[0]>>f[1]>>f[2];
		s = min(min(Calc(0), Calc(1)), Calc(2)); 
		if (s == "miaomiaomiao?")
			puts("IMPOSSIBLE");
		else
			cout<<s<<endl;
	}
	return 0;
}
