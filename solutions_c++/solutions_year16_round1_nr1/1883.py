#include <cstdio>
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <vector>
using std::vector;

char S[1024], tmp[1024];
int main()
{
	int T;	scanf("%d", &T);
	for(int i = 0; i < T; ++i) {
		scanf("%s", tmp);
		S[0] = tmp[0];
		if(tmp[1] == '\0') {
			printf("Case #%d: %s\n", i + 1, tmp);
			continue;
		}
		for(int j = 1; tmp[j] != '\0'; ++j) {
			if(tmp[j] >= S[0]) {
				// for(int k = 0; k < j; ++k)
				for(int k = j; k > 0; --k)
					S[k] = S[k - 1];
				S[0] = tmp[j];
				S[j + 1] = '\0';
			} else {	// tmp[j] < S[0]
				S[j] = tmp[j];
				S[j + 1] = '\0';
			}
		}
		printf("Case #%d: %s\n", i + 1, S);
	}
	return 0;
}