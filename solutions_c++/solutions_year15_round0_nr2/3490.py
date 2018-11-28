#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, d, a, maxa, ans, tmp;
	int p[1001];
	cin>>t;
	for(int i = 0; i < t; i++) {
		for(int j = 0; j <= 1000; j++)
			p[j] = 0;
		tmp = 0;
		ans = 1001;
		maxa = 0;
		
		cin>>d;
		for(int j = 0; j < d; j++) {
			cin>>a;
			if(a > maxa)
				maxa = a;
			p[a] += 1;
		}
			
		for(int j = 1; j <= maxa; j++) {
			tmp = 0;
			for(int k = j+1; k <= maxa; k++) {
				if(p[k] != 0) {
					if(k%j == 0)
						tmp += p[k]*((k/j)-1);
					else
						tmp += p[k]*(k/j);
				}
			}
			tmp = tmp+j;
			//~ cout<<j<<" "<<tmp<<" ";
			if(tmp < ans)
				ans = tmp;
		}
				
		printf("Case #%d: %d\n", i+1, ans);
	}
}
