#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

bool all_found(bool arr[]) {
	for (int i=0; i<10; i++)
		if (!arr[i]) return false;
	return true;
}

int run() {
	int n;
	scanf("%d", &n);
	
	if (n == 0) return -1;
	
	bool found[10] = {false, };
	int n2 = n;
	
	while (true) {
		
		int n3 = n2, k;
		do {
			k = n3 % 10;
			n3 /= 10;
			
			found[k] = true;
			
		}while (n3 > 0);
		
		if (all_found(found)) return n2;
		n2 += n;
	}
}

int main() {
	int testCase;
	scanf("%d", &testCase);
	
	for (int t=1; t<=testCase; t++) {
		int ret = run();
		if (ret == -1)
			printf("Case #%d: INSOMNIA\n", t);
		else
			printf("Case #%d: %d\n", t, ret);
	}
}
