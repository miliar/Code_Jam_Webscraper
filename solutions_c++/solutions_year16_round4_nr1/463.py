#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

map<char,char> beat;

struct node {
	char l;
	node *left, *right;
	node(char _l) {
		l=_l;
		left=right=NULL;
	}
	void del() {
		if(left) {
			left->del();
			delete left;
		}
		if(right) {
			right->del();
			delete right;
		}
	}
	void con(int d) {
		if(d==0) return;
		left=new node(l);
		right=new node(beat[l]);
		left->con(d-1);
		right->con(d-1);
	}
	void sort(int d) {
		if(d==0) return;
		char s1[12345], s2[12345];
		left->sort(d-1);
		right->sort(d-1);
		left->toString(s1, d-1);
		right->toString(s1+(1<<(d-1)), d-1);
		right->toString(s2, d-1);
		left->toString(s2+(1<<(d-1)), d-1);
		if(strcmp(s1, s2)>0) {
			swap(left, right);
		}
	}
	void toString(char *s, int d) {
		if(d==0) {
			(*s)=l;
			return;
		}
		left->toString(s, d-1);
		right->toString(s+(1<<(d-1)), d-1);
	}
};

int q;
int n;
int r, p, s;
char cur[12345];
char ans[12345];

int main()
{
	beat['R']='S';
	beat['S']='P';
	beat['P']='R';

	scanf("%d\n", &q);

	for(int x=1; x<=q; x++) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		const char let[3]={'P', 'R', 'S'};
		ans[0]=0;
		for(int id=0; id<3; id++) {
			node *root=new node(let[id]);
			root->con(n);
			root->sort(n);
			root->toString(cur, n);
			cur[(1<<n)]=0;
			int nr=0, np=0, ns=0;
			for(int i=0; i<(1<<n); i++) {
				if(cur[i]=='R') nr++;
				else if(cur[i]=='P') np++;
				else ns++;
			}
			if(!(nr==r && np==p && ns==s)) {
				root->del();
				continue;
			}
			root->del();
			if(ans[0]==0 || strcmp(cur, ans)<0) {
				strcpy(ans, cur);
			}
		}
		printf("Case #%d: ", x);
		if(ans[0]==0) printf("IMPOSSIBLE\n");
		else printf("%s\n", ans);
	}

	return 0;
}
