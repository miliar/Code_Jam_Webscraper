#include <cstdio>

using namespace std;

bool digit[10];

bool full() {
	for (int i=0;i<10;i++) {
		if (!digit[i]) return false;
	}
	return true;
}

int main () {
	int n;
	scanf("%d",&n);
	for (int i=0;i<n;i++) {
		int x;
		scanf("%d",&x);
		if (x==0) {
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		long long cur=x;
		long long tmp;
		while (true) {
			tmp = cur;
			while (tmp>0) {
				digit[tmp%10]=true;
				tmp/=10;
			}
			if (full()) {
				printf("Case #%d: %d\n",i+1,cur);
				break;
			}
			cur+=x;
		}
		for (int j=0;j<10;j++) {
			digit[j]=false;
		}
	}

	return 0;
}
