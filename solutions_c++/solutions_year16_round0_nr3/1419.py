#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
void nk7(int n, int k) {
	n -= 4;
	for (int i = 0;i < k ;++i) {
		printf("11");
		for (int j = 0;j < n / 2;++j) {
			if (i & (1 << j))
				printf("11");
			else printf("00");
		}
		printf("11 ");
		for (int j = 3;j <= 11;j++) cout << j << ' ';
		puts("");
	}

}
int main() {
	
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d", &t);
	int cc = 1;
	int n, k;
	while (t--) {
		printf("Case #%d:\n", cc++);
	
		scanf("%d%d", &n, &k);
		nk7(n, k);
	}

}