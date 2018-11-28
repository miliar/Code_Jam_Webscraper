#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
using namespace std;

int cases, i, j, ans, l;
int a[105];
string st;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	ios::sync_with_stdio(false);
	cin >> cases;
	for (int T = 1; T <= cases; T++) {
		cout << "Case #" << T << ": ";
		cin >> st;
		l = st.length();
		
		for (i = 0; i < l; i++) {
			a[i + 1] = st[i] == '+' ? 1 : 0;
		}
		ans = 0;
		i = 1;
		while (i < l){
			while (a[i] == a[i + 1] && i < l) i++;
			if (i == l) break;
			ans++;
			i++;
		}
		if (a[l] == 0) ans++;
		cout << ans << endl;
	}
} 
