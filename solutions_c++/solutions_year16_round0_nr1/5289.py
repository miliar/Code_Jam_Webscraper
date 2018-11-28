#include "cstdio"
#include "iostream"

using namespace std;

int mask = 1023;

int parse(int num) {
	int res = 0;
	while(num != 0) {
		res |= 1 << (num % 10);
		num /= 10;
	}

	return res;
}

bool insom[1000005];
int ans[1000005];

int main(void) {
	insom[0] = true;
	for(int i=1;i<=1000000;i++) {
		insom[i] = true;
		int masked = 0;

		for(int j=1;j<=75;j++) {
			masked |= parse(j * i);
			if(masked == mask) {
				insom[i] = false;
				ans[i] = j * i;
				break;
			}			
		}
	
		if(insom[i]) {
			cout << i << endl;
		}
	}

	// cout << "Done" << endl;

	int t;
	scanf("%d", &t);
	for(int test = 1;test<=t;test++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", test);
		if(insom[n])
			cout << "INSOMNIA" << endl;
		else
			cout << ans[n] << endl;
	}

	return 0;
}
