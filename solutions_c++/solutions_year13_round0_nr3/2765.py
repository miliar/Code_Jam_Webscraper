#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;


int map[1005];
int main(int argc, char** argv) {
	int i,tmp1,tmp2;
	int j,k,l;
	int num;
	int a,b;
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
	for (i=0;i<1005;i++) {
		map[i]=0;
	}
	for (i=1;i<10;i++) {
		j=i*i;
		if ((j<10) || ((j%10)==(j/10))) {
			map[j]=1;
		}
	}
	for (i=11;(i*i)<1001;i+=11) {
		j=i*i;
		if ((j/100)==(j%10)) {
			map[j]=1;
		}
	}
	for (i=1;i<=round;i++) {
		fscanf(in,"%d",&a);
		fscanf(in,"%d",&b);
		num=0;
		for (tmp1=a;tmp1<=b;tmp1++) {
			if (map[tmp1]==1) {
				num++;
			}
		}
		fprintf(out,"Case #%d: %d\n",i,num);
	}
	
	
	fclose(in);
	fclose(out);
	return 0;
}
