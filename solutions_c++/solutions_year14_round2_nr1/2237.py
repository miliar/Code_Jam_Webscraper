#include <iostream>
#include <cstdio>

using namespace std;

struct node {
	char c;
	int v;
};

int abs(int a)
{
	if (a > 0) return a;
	return -a;
}

int len(struct node a[])
{
	int ctr = 0;
	for (int i = 0; a[i].c != 0; i++) {
		ctr++;
	}
	
	return ctr;
}

int main()
{
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	
	cin >> t;
	for (int ct = 1; ct <= t; ct++) {
		char s1[1000], s2[1000];
		struct node a1[1000], a2[1000];
		
		bool flag = true;
		
		int h1 = 0, h2 = 0;
		int n;
		
		cin >>  n;
		scanf("%s", s1);
		scanf("%s", s2);
		
		for (int i = 0; i < 1000; i++) {
			a1[i].c = a2[i].c = 0;
			a1[i].v = a2[i].v = 0;
		}
		
		a1[0].c = s1[0];
		a2[0].c = s2[0];
		
		a1[0].v = a2[0].v = 1;
		
		for (int i = 1; s1[i] != 0; i++) {
			if (s1[i] == s1[i - 1]) {
				a1[h1].v++;
			} else {
				a1[++h1].c = s1[i];
				a1[h1].v = 1;
			}
		}
		for (int i = 1; s2[i] != 0; i++) {
			if (s2[i] == s2[i - 1]) {
				a2[h2].v++;
			} else {
				a2[++h2].c = s2[i];
				a2[h2].v = 1;
			}
		}
		
		/*for (int i = 0; i <= h1; i++) {
			printf("%c %d\n", a1[i].c, a1[i].v);
		}
		cout << endl;
		for (int i = 0; i <= h2; i++) {
			printf("%c %d\n", a2[i].c, a2[i].v);
		}*/
		
		if (h1 != h2) {
			flag = false;
		} else {
			for (int i = 0; i <= h1; i++) {
				if (a1[i].c != a2[i].c) {
					flag = false;
					//printf("%d %c %c", 1, a1[i].c, a2[i].c);
					break;
				}
			}
		}
		
		int ctr = 0;
		if (flag == true) {
			for (int i = 0; i <= h1; i++) {
				ctr += abs(a1[i].v - a2[i].v);
			}
			printf("Case #%d: %d\n", ct, ctr);
		} else {
			printf("Case #%d: Fegla Won\n", ct);
		}
	}
}
