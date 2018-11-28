#include <iostream>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;

struct ans {
	int x,y,z;
} b[2000], c[2000], fans[2000];

int j,p,s,k, a[5][20][20], cnt;



int main () {
	freopen("C-small-attempt1.in","r",stdin);
	freopen("c.out","w",stdout);
	srand(int(time(0)));
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		cin>>j>>p>>s>>k;
		int tot=0;
		for (int i=1; i<=j; ++i)
		  for (int ii=1; ii<=p; ++ii)
		    for (int iii=1; iii<=s; ++iii) {
		    	b[tot].x=i;
		    	b[tot].y=ii;
		    	b[tot].z=iii;
		    	++tot;
			}
		int cnt1=100, ret=0;
		while (cnt1--) {
			int t[1100];
			bool f[1100];
			memset(f,0,sizeof(f));
			for (int i=0; i<tot; ++i) {
				do {
					t[i]=rand()%tot;
				} while (f[t[i]]);
				f[t[i]]=1;
			}
			int cnt2=100;
			while (cnt2--) {
				memset(a,0,sizeof(a));
				int cnt3=5;
				while (cnt3--) {
					swap(t[rand()%tot], t[rand()%tot]);
				}
				int cur=0;
				for (int i=0; i<tot; ++i) {
					if (a[0][b[t[i]].x][b[t[i]].y]<k &&
					a[1][b[t[i]].x][b[t[i]].z]<k &&
					a[2][b[t[i]].y][b[t[i]].z]<k) {
						++a[0][b[t[i]].x][b[t[i]].y];
						++a[1][b[t[i]].x][b[t[i]].z];
						++a[2][b[t[i]].y][b[t[i]].z];
						c[cur].x=b[t[i]].x;
						c[cur].y=b[t[i]].y;
						c[cur].z=b[t[i]].z;
						++cur;
					}
				}
				if (cur>ret) {
					ret=cur;
					for (int i=0; i<ret; ++i) {
						fans[i].x=c[i].x;
						fans[i].y=c[i].y;
						fans[i].z=c[i].z;
					}
				}
			}
		}
		printf("Case #%d: %d\n", T, ret);
		for (int i=0; i<ret; ++i) {
			printf("%d %d %d\n",fans[i].x,fans[i].y,fans[i].z);
		}
	}
}
