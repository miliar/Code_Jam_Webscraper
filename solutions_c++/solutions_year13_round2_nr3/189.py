#include<stdio.h>
#include<iostream>
#include<queue>
#include<algorithm>
#include<map>
using namespace std;
const int TSIZE = 4000000; //状态个数上限=单词总数*单词长度
const int CN = 26; //可选择字符数
struct Trie //Trie 结构
{
	int c[CN];
	int fail; //fail指针
	bool flag; //状态标志(有时需要int类型)
	void init() //节点初始化
	{
		memset(c, 0, sizeof(c));
		fail = -1;
		flag = false;
	}
};
Trie trie[TSIZE];
int len; //当前长度
void PreProcess() {
	trie[0].init();
	len = 1;
}
int Get(char ch) //根据具体题目修改
{
	return ch - 'a';
}
void Insert(char *str, bool id) //插入单词,标志
{
	int r, no;
	int i;
	r = 0;
	for (i = 0; str[i]; i++) {
		no = Get(str[i]);
		if (!trie[r].c[no]) {
			trie[len].init();
			trie[r].c[no] = len++;
		}
		r = trie[r].c[no];
	}
	trie[r].flag = id;
}
struct node {
	int i, j, pre;
} tt, nt;
queue<node> q;
char s[40000];
map<__int64, int> mm;

void ii(node a, int num) {
	if (a.i - a.pre > 5)
		a.pre = a.i - 5;
	__int64 t = (__int64) ((__int64) (a.pre+10) * 4001LL + (__int64) a.i) * 4000000LL + (__int64) a.j;
	int p;
//	printf("%d %I64d\n",a.i,t);
	p = mm[t];
	if (p == 0 || p > num) {
		mm[t] = num;
	}
	if (p == 0)
		q.push(a);
}
int ff(node a) {
	__int64 t = (__int64) ((__int64) (a.pre+10) * 4001LL + (__int64) a.i) * 4000000LL + (__int64) a.j;
	return mm[t];
}
int main() {
	int t, cas = 0;
	int i, ans, l;
	int nnum, tnum;
	FILE *f;
	f = fopen("D:\\garbled_email_dictionary.txt", "r");
	PreProcess();
	while (fscanf(f, "%s", s) != EOF)
		Insert(s, true);
	scanf("%d", &t);
	while (t--) {
		cas++;
		mm.clear();
		scanf("%s", s);
		l = strlen(s);
		nt.i = 0;
		nt.j = 0;
		nt.pre = -10;
		ii(nt, 1);
		ans = 30000;
		while (!q.empty()) {
			tt = q.front();
			q.pop();
			tnum = ff(tt);
			if (tt.i == l) {
				if (trie[tt.j].flag) {
					ans = min(ans, tnum);
				}
				continue;
			}
			if (trie[tt.j].c[s[tt.i] - 'a'] != 0) {
				nt.i = tt.i + 1;
				nt.j = trie[tt.j].c[s[tt.i] - 'a'];
				nnum = tnum;
				nt.pre = tt.pre;
				ii(nt, nnum);
			}
			if (trie[tt.j].flag && trie[0].c[s[tt.i] - 'a'] != 0) {
				nt.i = tt.i + 1;
				nt.j = trie[0].c[s[tt.i] - 'a'];
				nnum = tnum;
				nt.pre = tt.pre;
				ii(nt, nnum);
			}
			if (tt.i - tt.pre >= 5) {
				for (i = 0; i < 26; ++i) {
					if (i == s[tt.i] - 'a')
						continue;
					if (trie[tt.j].c[i] != 0) {
						nt.i = tt.i + 1;
						nt.j = trie[tt.j].c[i];
						nnum = tnum + 1;
						nt.pre = tt.i;
						ii(nt, nnum);
					}
					if (trie[tt.j].flag) {
						if (trie[0].c[i] != 0) {
							nt.i = tt.i + 1;
							nt.j = trie[0].c[i];
							nnum = tnum + 1;
							nt.pre = tt.i;
							ii(nt, nnum);
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", cas, ans - 1);
	}
}
/*
loxmuxrlumukmuulqxmuxmuxxuvllllkmullwuuvlflluvomua
 */
