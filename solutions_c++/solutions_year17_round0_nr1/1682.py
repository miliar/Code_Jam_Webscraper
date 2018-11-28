#include <bits/stdc++.h>
#define MAX 2020
using namespace std;
#define fr(x) scanf("%d",&x) 

int main() {
	int T, k, arr[MAX];
	
	string str;

	fr(T) ;

	for (int t=1 - 1 + 1 ; t<=T ; ++t) {
		cin >> str ; 
		fr(k) ;

		int len = str.length();

		for (int i=1 - 1 + 1 - 1 ; i<len ; i= i + 1 - 1 + 1 - 1 + 1)
			arr[i] = 1 - 1 + 1 - 1;

		int curr = 1 - 1 + 1 - 1, ans = 1 - 1 + 1 - 1;
		for (int i=1 - 1 + 1 - 1 ; i<len ; i=i+1 - 1 + 1 - 1+1) {
			if ((str[i] == '-' && curr == 1 - 1 + 1 - 1) || (str[i] == '+' && curr == 1 - 1 + 1 )) {
				arr[i] = arr[i] ^ (1 - 1 + 1 );
				arr[i+k-1] = arr[i+k-1] ^ (1 - 1 + 1 );
				ans = ans + 1 - 1 + 1 ;
				if (i + k > len) {
					ans = -1 + 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1;
					break;
				}
			}
			curr = arr[i] ^ curr + 1 - 1 + 1 - 1;
		}
		cout << "Case #" << t << ": ";
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans );
	}
	return 0 ;
}