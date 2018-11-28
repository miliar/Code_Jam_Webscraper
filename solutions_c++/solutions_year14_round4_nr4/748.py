#include <cstdio>
#include <iostream>
#include <string.h>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 10;
class Tire;
class node {
public:
	char a;
	node* next;
	Tire* point;
};
class Tire {
public:
	int num;
	node* a;
	
};
int n, m, testnum;
char sa[maxn][20];
Tire* b[5];
int c[10];
using namespace std;
int ans;
int len[maxn];
int ans_num = 0;


void dfs(int i, int tans) {

	//printf("%d %d\n", i, tans);


	if (i > m) {
		if (tans == ans) ans_num++;
		else
		if (tans > ans) {
			/*for (int i = 1; i <= 5; i++)
				printf("%d %d", c[i],len[i]);*/
			ans = tans;
			ans_num = 1;
		}
		return;
	}
	
	int tt = 0;
	for (int j = 1; j <= n; j++) {
		c[i] = j;
		int tmp = -1;
		bool u = false;
		for (int k = 1; k < i; k++) {
			if (c[k] == j) {
				u = true;
				for (int jj = 0; jj < len[i]; jj++) {
					if (jj >= len[k]) break;
					if (sa[k][jj] == sa[i][jj]) {
						if (jj > tmp)
							tmp = jj;
					} else break;
				}
				
			}
		}
		if (!u) tt= 1; else tt =0 ;
		dfs(i + 1, tans + len[i] + tt- tmp - 1);

	/*	Tire* s = b[i];
		
		for (int k = 0; k < len[i]; k++) {
			bool u = false;
			if (s->num == 0) tans++;
			s->num++;
			node* tmp = s->a;
			while (tmp->next != NULL) {
				if (tmp->a == sa[i][k]) {
					s = tmp->point;
					u = true;
					break;
				}
				tmp = tmp->next;
			}
			if (tmp->a == sa[i][k]) {
				s = tmp->point;
				u = true;
			}
			if (!u) {
				tmp->next = new node();
				tmp = tmp->next;
				tmp->a = sa[i][k];
				tmp->next = NULL;
				tmp->point = new Tire();
				s = tmp->point;
				s->num = 0;
				s->a = new node();
				s->a->a = '!';
				s->a->next = NULL;
			}
		}
		s->num++;

		dfs(i + 1, tans);
		s = b[i];
		for (int k = 0; k < len[i]; k++) {
			bool u = false;
			if (s->num == 0) tans++;
			s->num--;
			
			node* tmp = s->a;
			while (tmp->next != NULL) {
				if (tmp->a == sa[i][k]) {
					s = tmp->point;
					u = true;
					break;
				}
				tmp = tmp->next;
			}
			if (tmp->a == sa[i][k]) {
				s = tmp->point;
				u = true;
			}
		}
		s->num--;*/


		
		//for (int k = 0; k < len)

	}

}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		ans = 0;
		/*for (int i = 1; i <= 4; i++) {
			b[i] = new Tire();
			b[i]->num = 0;
			b[i]->a = new node();
			b[i]->a->a = '!';
			b[i]->a->next = NULL;
		}*/
		scanf("%d%d\n", &m, &n);
		for (int i = 1; i <= m; i++) {
			scanf("%s", sa[i]);
			len[i] = strlen(sa[i]);
		}
		/*for (int i = 1; i <= m; i++)
			printf("%s\n", sa[i]);*/

		dfs(1, 0);
		printf("Case #%d: %d %d\n", test, ans, ans_num);
	}
}