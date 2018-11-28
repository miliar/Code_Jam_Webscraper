#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;

	scanf("%d", &tc);

	for(int n = 1; n <= tc; n++){

		char str[101];
		int kount = 0;
		scanf("%s", str);

		int len = strlen(str);

		for(int i = 0; i < len-1; i++){
			if(str[i] == '+' && str[i+1] == '-') kount++;
		}

		if(str[0] == '-') printf("Case #%d: %d\n",n,(2*kount)+1);
		else printf("Case #%d: %d\n", n,(2*kount));


	}

	return 0;
}
