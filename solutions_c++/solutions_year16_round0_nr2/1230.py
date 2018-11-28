#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 200100;
int const MAX_CH = 100100;
int const INT_INF = 1000000000;

char st[MAX_CH];
int d[1<<15],och[1<<15],unpa[2000],ms[2000];

int slow_solve(char *st, int n) {
	int g = 1<<n;
	for (int i=0; i<g; i++) d[i] = INT_INF;

	int init_v = 0;
	for (int i=0; i<n; i++)
		init_v = init_v*2 + (st[i]=='+');

	d[init_v] = 0;
	int p_read = 0, p_write = 1;
	och[p_read] = init_v;

	while (p_read < p_write) {
		int v = och[p_read++];

		int ind = n-1;
		for (int i=0; i<n; i++)
			unpa[ind--] = (v>>i)&1;

		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) ms[j] = unpa[j];

			for (int j=0; j<=i; j++) ms[j] = 1-ms[j];
			for (int j=0; j<(i+1)/2; j++)
				swap(ms[j],ms[i-j]);

			int new_v = 0;
			for (int j=0; j<n; j++)
				new_v = new_v*2 + ms[j];

			if (d[new_v] > d[v] + 1) {
				d[new_v] = d[v] + 1;
				och[p_write++] = new_v;
			}
		}
	}

	return d[(1<<n)-1];
}

int greedy_solve(char *st, int n) {
	int ans = 0;
	for (int i=0; i<n; i++) ms[i] = st[i]=='+';

	while (1) {
		int tp_0 = ms[0];
		int r = 1;
		while (r < n && ms[r] == tp_0) r++;

		if (r >= n) {
			if (tp_0 == 1) break;
			ans++;
			break;
		}

		ans++;
		for (int i=0; i<r; i++) ms[i] = 1-ms[i];
	}

	return ans;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	/*for (int n=1; n<=10; n++)
		for (int code=0; code<(1<<n); code++) {
			for (int j=0; j<n; j++)
				if ((code>>j)&1) st[j] = '+';
				else st[j] = '-';
			st[n] = 0;

			if (slow_solve(st,n) != greedy_solve(st,n)) {
				cout<<"Error!  ";
				printf("%s",st);
				cout<<"   Slow = "<<slow_solve(st,n)<<"   Greedy = "<<greedy_solve(st,n)<<"\n";
				return 0;
			}
		}
	cout<<"Ok";
	return 0;*/

	int t;
	gets(st);
	sscanf(st,"%d",&t);
	int ind = 0;
	while (t-->0) {
		ind++;
		printf("Case #%d: ",ind);
		
		gets(st);
		int n = (int) strlen(st);

		cout<<greedy_solve(st, n)<<"\n";
	}
	return 0;
}