
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int T;
int R,C,M;
char a[64][64];

void print() {
	for (int i=1;i<=R;i++) {
		for (int j=1;j<=C;j++)
			printf("%c",a[i][j]);
		printf("\n");
	}
}

void nos() {
	printf("Impossible\n");
}

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		memset(a,'*',sizeof(a));
		printf("Case #%d:\n",ww);
		scanf("%d%d%d",&R,&C,&M);
		M=R*C-M;
		if (R==1 || C==1) {
			for (int i=1;i<=R;i++) {
				for (int j=1;j<=C;j++) {
					if (M) {
						a[i][j]='.';
						M--;
					}
					else a[i][j]='*';
				}
			}
			a[1][1]='c';
			print();
		}
		else if (R==2 || C==2) {
			if ((M%2==1 || M<4) && M!=1) nos();
			else {
				if (R==2) {
					for (int j=1;j<=C;j++)
						for (int i=1;i<=R;i++) {
							if (M) {
								a[i][j]='.';
								M--;
							}
							else a[i][j]='*';
						}
				}
				else {
					for (int i=1;i<=R;i++)
						for (int j=1;j<=C;j++) {
							if (M) {
								a[i][j]='.';
								M--;
							}
							else a[i][j]='*';
						}
				}
				a[1][1]='c';
				print();
			}
		}
		else {
			if (M==2 || M==3 || M==5 || M==7) nos();
			else {
				if (M==1) {
					a[1][1]='c';
					print();
					continue;
				}
				if (M==4) {
					a[1][1]=a[1][2]=a[2][1]=a[2][2]='.';
					a[1][1]='c';
					print();
					continue;
				}
				M-=2;
				a[3][1]=a[3][2]='.';
				for (int j=1;j<=C;j++)
					if (M>=2) a[1][j]=a[2][j]='.',M-=2;
				for (int i=4;i<=R;i++)
					if (M>=2) a[i][1]=a[i][2]='.',M-=2;
				for (int i=3;i<=R;i++)
					for (int j=3;j<=C;j++) {
						if (M) {
							a[i][j]='.';
							M--;
						}
						else a[i][j]='*';
					}
				a[1][1]='c';
				print();
			}
		}
	}
	return 0;
}
