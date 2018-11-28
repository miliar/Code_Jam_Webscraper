#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int sum,n;
long long ans[10], a[40];

void mult(int *res, int p) {
	int i, tmp=0;
	for (i=1; i<=res[0]; i++) {
		tmp += res[i]*p;
		res[i] = tmp%10;
		tmp /= 10;
	}
	while (tmp>0) {
		res[0]++;
		res[res[0]] = tmp%10;
		tmp /= 10;
	}
}

void add(int *res, int *p) {
	int i, tmp=0;
	res[0] = max(res[0], p[0]);
	for (i=1; i<=res[0]; i++) {
		tmp += res[i]+p[i];
		res[i] = tmp%10;
		tmp /= 10;
	}
	while (tmp>0) {
		res[0]++;
		res[res[0]] = tmp%10;
		tmp /= 10;
	}
}

int candiv(int *res, long long p) {
	int i;
	long long tmp = 0;
	for (i=res[0]; i>0; i--) {
		tmp = tmp*10 + res[i];
		tmp %= p;
	}
	if (tmp) return 0; else return 1;
}

int test(int p) {
	int i;
	int tmp[40], tot[40];
	long long now = 2;

	memset(tmp, 0, sizeof(tmp));
	memset(tot, 0, sizeof(tot));
	tmp[0] = 1; tmp[1] = 1;
	for (i=0; i<n; i++) {
		if (a[i]) add(tot, tmp);
		mult(tmp, p);
	}
	cout<<p<<" ";
	for (i=tot[0]; i>0; i--) cout<<tot[i];
	cout<<"\n";
	
	long long maxn = 1 << (tot[0]/2+1);
	while (now <= maxn) {
		if (candiv(tot, now)) {
			sum++; ans[sum]=now; return 1;
		}
		now++;
	}
	return 0;
}

int main() {
	int i,T,num;

	FILE *fin, *fout;
	fin = fopen("1.in", "r");
	fout = fopen("1.txt", "w");
	fscanf(fin, "%d", &T);
	fscanf(fin, "%d %d", &n, &num);
	fprintf(fout, "Case #1:\n");
	int now = 1; int mid = 0;
	memset(a, 0, sizeof(a));
	a[n-1] = 1; a[0] = 1;
	while (num>0) {
		int tmp = mid, pos = 1;
		while (tmp>0) {
			a[pos] = tmp%2; tmp = tmp/2; pos++;
		}
		sum = 0;
		for (i=2; i<=10; i++) 
			if (!test(i)) break;
		for (i=n-1; i>=0; i--) cout<<a[i];
		cout<<" "<<sum<<"\n";
		if (sum==9) {
			for (i=n-1; i>=0; i--) fprintf(fout, "%d", a[i]);
			for (i=1; i<=sum; i++)
				fprintf(fout, " %d", ans[i]);
			fprintf(fout, "\n");
			num--;
		}
		mid++;
	}
	fclose(fin); fclose(fout);
	return 0;
}
