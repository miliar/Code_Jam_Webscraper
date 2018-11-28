#include<cstdio>
#include<iostream>

using namespace std;

int A[1010];

int main() {
	int tc, n;
	string s;
	
	freopen("F:\\Dev C++\\inputCJ.txt", "r", stdin);
	freopen("F:\\Dev C++\\outputCJ.txt", "w", stdout);
	
	scanf("%d", &tc);
	
	for(int k = 1; k <= tc; k++) {
		scanf("%d", &n);
		cin >> s;
		int total = 0;
		int invite = 0;
		
		for(int i=0; i<=n; i++) {
			if (i > total) {
				invite += (i - total);
				total = i;
			}
			
			total += (s[i] - '0');
		} 
		
		printf("Case #%d: %d\n", k, invite);
	}
}
