#include <stdio.h>
#include <string.h>

char str[120];



bool isok(int a[],int len) {
	for (int i = 0; i < len; ++i) {
		if (a[i] == 0) return false;
	}
	return true;
}

int f(int a[], int len) {
	int res = 0;
	while (true) {
		if ( isok(a,len) ) break;
		int i;
		for (i = 1; i < len; ++i) {
			if (a[i] == 1 &&  a[i-1] == 0) break;
		}
		if (a[0] == 0) {
			res++;
		}
		else {
			res += 2;
		}
		int tmp = 0;
		int b[110];
		for (int j = len-1; j >= i; --j) {
			if (a[j] == 0) b[tmp++] = 1;
			else b[tmp++] = 0;
		}
		len = len-i;
		for (int i = 0; i < len; ++i) {
			a[i] = b[i];
		}
		
	}
	return res;
}

int main() {
	int n, h = 1;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d", &n);
	while(n--) {
		scanf("%s", str);
		int a[110];
		int len = strlen(str);
		for (int i = 0; i < len; ++i) {
			if (str[i] == '+') a[i] = 1;
			else a[i] = 0;
		}
		for (int i = len-1; i >= 0; --i) {
			if (a[i] == 1) {
				len--;
			}
			else {
				break;
			}
		}
		printf("Case #%d: %d\n",h++, f(a,len));
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
