#include <bits/stdc++.h>
using namespace std;

string gen(string x) {
	string t,u;
	if (x.length() == 1) return x;
	t = gen(x.substr(0,x.length()/2));
	u = gen(x.substr(x.length()/2,x.length()/2));
	if (t < u) return (t + u);
	else {
		return (u + t);
	}
}

int main() {
	int tc,n;
	scanf("%d",&tc);
	string ans = "RPS";
	string res[3];
	int p,r,s;
	int a[4096];
	int c[3]; 
	for (int zz = 1;zz<=tc;zz++) {
		res[0] = "T";
		res[1] = "T";
		res[2] = "T";
		scanf("%d %d %d %d",&n,&p,&r,&s);
		printf("Case #%d: ",zz);
		for (int i=0;i<3;i++) {
			a[1] = i;
			for (int j=2;j<(1<<(n+1));j++) {
				if (j&1) a[j] = (a[j/2]+2) % 3;
				else a[j] = a[j/2];
			}
			
			c[0] = 0; c[1] = 0; c[2] = 0;
			for (int j=1<<n;j<(1<<(n+1));j++) {
				c[a[j]]++;
			}
			if ((c[0] == p) && (c[1] == r) && (c[2] == s)) {
				string temp = "";
				for (int j=1<<n;j<(1<<(n+1));j++) temp = temp + ans[a[j]];
				res[i] = gen(temp);
			}
		}
		if ((res[0] == "T") && (res[1] == "T") && (res[2] == "T")) printf("IMPOSSIBLE\n");
		else if ((res[0] < res[1]) && (res[0] < res[2])) cout << res[0] << endl;
		else if (res[1] < res[2]) cout << res[1] << endl;
		else cout << res[2] << endl;
	}
	return 0;
}