#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int test, counter =0;
	scanf("%d\n", &test);
	char c[111];
	string s;

	for (int i=0; i < test; i++){
		scanf("%s", &c);
		counter = 0;
		string s(c);
		for (int j = 0; j < s.length() -1 ; j ++){
			if (s[j] != s[j+1]){
				counter ++;
			}
		}
		if (s[s.length()-1] == '-')
			counter ++;
		printf("Case #%d: %d\n", i+1, counter);
	}

}