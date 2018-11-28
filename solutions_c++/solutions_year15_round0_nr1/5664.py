#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("myfile.txt","w",stdout);
	int T, co =1;
	cin >> T;
	while (T--) {
		int a,temp;
		cin >> a;
		int b[1500];
		scanf("%c", &temp);
		for (int i = 0; i <= a; i++) {
			scanf("%c", &temp);
			b[i] = temp - '0';
		}
		int count = b[0];
		int fc =0 ;
		for (int i = 1; i <= a; i++) {
			if (count < i) {
				fc += i-count;
				count = i;
			}
			count += b[i];
		}
		printf("Case #%d: %d\n", co, fc);
		scanf("%c", &temp);
		co++;
	}
	
	// your code goes here
	return 0;
}
