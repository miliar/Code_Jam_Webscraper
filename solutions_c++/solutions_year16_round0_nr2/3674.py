#include<iostream>
#include<algorithm>
#include<cstring>
#include<string.h>
using namespace std;
char arr [105];
char flip(char w){
	if (w == '-'){
		return '+';
	} else {
		return '-';
	}
}
int main() {
	int ts; cin >> ts;
	int tt = 1;
	while (ts--) {
		memset( arr, 0, sizeof arr);
		scanf("%s", arr);
		int n = strlen(arr);
		int res = 0;
		char w = '+';
		for (int i = n-1; i >=0; i--){
			if (arr[i] == w) continue;
			res++;
			w = flip(w);
		}
		cout << "Case #" << tt++ << ": "; 
		cout << res << "\n";
	}

}
