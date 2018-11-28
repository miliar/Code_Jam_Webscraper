#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;


int map[101][101];
int main(int argc, char** argv) {
	int i,tmp1,tmp2;
	int a,b,c,d,e;
	int fail;
	int n,m;
	int round;
	FILE *in, *out;
	if (argc!=3) {
		printf("no\n");
		return 0;
	}
	in=fopen(argv[1],"r+");
	out=fopen(argv[2],"w+");
	if (in==NULL || out==NULL) {
		printf("no\n");
		return 0;
	}
	fscanf(in,"%d",&round);
	for (i=1;i<=round;i++) {
		fscanf(in,"%d%d",&m,&n);
		for (tmp1=0;tmp1<m;tmp1++) {
			for (tmp2=0;tmp2<n;tmp2++) {
				fscanf(in,"%d",&(map[tmp1][tmp2]));
			}
		}
		fail=0;
		for (a=0;a<m;a++) {
			for (b=0;b<n;b++) {
				for (c=0;c<n;c++) {
					if (map[a][c]>map[a][b]) {
						for (d=0;d<m;d++) {
							if (map[d][b]>map[a][b]) {
								fail=1;
								break;
							}
						}
						if (fail==1) {
							break;
						}
					}
				}
				if (fail==1) {
					break;
				}
			}
			if (fail==1) {
				break;
			}
		}
		if (fail==1) {
			fprintf(out,"Case #%d: NO\n",i);
		}
		else {
			fprintf(out,"Case #%d: YES\n",i);
		}
	
	}
	fclose(in);
	fclose(out);
	return 0;
}
