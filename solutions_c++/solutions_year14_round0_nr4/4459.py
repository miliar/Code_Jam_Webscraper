#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n;
int num1[1000], num2[1000];

int read_it() {
	char buf[100];
	scanf("%s", buf);
	for(int i = strlen(buf);i < 7;i ++) buf[i] = '0';
	
	int res = 0;
	for(int i = 2;i < 7;i ++) res = res*10 + (buf[i]-'0');

	return res;
}

void input() {
	scanf("%d", &n);
	for(int i = 0;i < n;i ++) num1[i] = read_it();
	for(int i = 0;i < n;i ++) num2[i] = read_it();
}

void output() {
	sort(num1, num1+n);
	sort(num2, num2+n);

	//printf("\n");
	//for(int i = 0;i < n;i ++) printf("%d ", num1[i]);
	//printf("\n");
	//for(int i = 0;i < n;i ++) printf("%d ", num2[i]);
	//printf("\n");

	int res = 0, b = 0, e = n-1;
	for(int i = 0;i < n;i ++) {
		if(num1[i] > num2[b]) {
			++ res;
			++ b;
		}
		else -- e;
	}

	int res1 = 0;
	int used[1000];
	for(int i = 0;i < n;i ++) used[i] = 0;
	for(int i = 0;i < n;i ++) {
		int ok = 1;
		for(int j = 0;j < n;j ++) if(!used[j]&&num1[i] < num2[j]) {
			used[j] = 1;
			ok = 0;
			break;
		}
		if(ok) ++ res1;
	}

	printf("%d %d\n", res, res1);
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		output();
	}
	return 0;
}