#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stdlib.h>
#include <time.h>
using namespace std;

void arrange (string &str, int s, int e) {
	//cout << str << " " << s << " " << e << endl;
	if (s == e) {
		return;
	}

	int mid = (s+e)/2;
	arrange(str, s, mid);
	arrange(str, mid+1, e);

	bool small = true;

	for (int i = 0;i<(e-s+1)/2;i++) {
		if (str[s+i] == str[mid+1+i]) {
			continue;
		}
		if (str[s+i] > str[mid+1+i]) {
			small = false;
			break;
		}
	}

	if (!small)
	for (int i = 0;i<(e-s+1)/2;i++) {
		swap (str[s+i], str[mid+1+i]);
	}

	return;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);

	for (int it=1;it<=t;it++) {
		printf ("Case #%d: ", it);
		int n, a[3];

		scanf ("%d %d %d %d", &n, &a[0], &a[1], &a[2]);

		queue <int> q;
		queue <int> l;
		queue <int> ind;

		char str[] = "RPS";
		string res = "";

		for (int i=0;i<3;i++) {
			if (!a[i]) {
				continue;
			}
			q.push(i);
			l.push(0);
			ind.push(0);
			int c[3];
			c[0] = a[0], c[1] = a[1], c[2] = a[2];
			c[i] --;
			bool ok = true;
			int fin[1<<n];
			while (!q.empty()) {
				int cur = q.front();
				q.pop();
				int cl = l.front();
				l.pop();
				int ci = ind.front();
				ind.pop();

				//cout << cur << " " << cl << " " << ci << endl;

				if (cl == n) {
					fin[ci] = cur;
					continue;
				}

				if (!c[(cur+2)%3]) {
					ok = false;
					break;
				} else {
					c[(cur+2)%3] --;
					q.push(cur);
					l.push(cl+1);
					ind.push(ci<<1);
					q.push((cur+2)%3);
					l.push(cl+1);
					ind.push((ci<<1)+1);
				}
			}
			if (ok) {
				string ret = "";
				for (int j=0;j<(1<<n);j++) {
					ret += str[fin[j]];
				}
				arrange (ret, 0, ret.size()-1);
				if (res == "") {
					res = ret;
				} else {
					res = min (res, ret);
				}
			} else {
				while (!q.empty()) {
					q.pop();
					l.pop();
					ind.pop();
				}
				/*while (!l.empty()) {
					l.pop();
				}
				while (!ind.empty()) {
					ind.pop();
				}*/
			}
		}

		if (res == "") {
			printf ("IMPOSSIBLE\n");
		} else {
			printf ("%s\n", res.c_str());
		}

	}

	return 0;
}