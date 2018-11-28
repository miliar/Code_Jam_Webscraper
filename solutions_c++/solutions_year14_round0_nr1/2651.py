#include <cstdio>
#define RI(a) scanf("%d", &(a))
using namespace std;
int n,a[16], b[4], c[4],d;
int check(){
	int dd=0;
	if (b[0]==c[0] || b[0]==c[1] || b[0]==c[2] || b[0]==c[3]) dd=dd*17+b[0];
	if (b[1]==c[0] || b[1]==c[1] || b[1]==c[2] || b[1]==c[3]) dd=dd*17+b[1];
	if (b[2]==c[0] || b[2]==c[1] || b[2]==c[2] || b[2]==c[3]) dd=dd*17+b[2];
	if (b[3]==c[0] || b[3]==c[1] || b[3]==c[2] || b[3]==c[3]) dd=dd*17+b[3];
	return dd;
}
int main() {
	int tt, ttt=0;
	RI(tt);
	while (ttt++ < tt) {
		printf("Case #%d: ", ttt);

		RI(n);
		for (int i = 0; i < 16; i++)
			RI(a[i]);
		d=4*(n-1);
		b[0]=a[d];
		b[1]=a[d+1];
		b[2]=a[d+2];
		b[3]=a[d+3];
		RI(n);
		for (int i = 0; i < 16; i++)
			RI(a[i]);
		d=4*(n-1);
		c[0]=a[d];
		c[1]=a[d+1];
		c[2]=a[d+2];
		c[3]=a[d+3];
		int dd=check();
		if (dd==0) printf("Volunteer cheated!\n");
		else if (dd>16) printf("Bad magician!\n");
		else printf("%d\n",dd);
	}
}
