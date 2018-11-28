#include <cstdio>
#include <cstring>
int main() {
	FILE * in = fopen("input.in","r");
	FILE * out = fopen("ouput.out","w");
	char a[1005];
	int test,s;
	fscanf(in,"%d",&test);
	for(int t=1;t<=test;t++) {
		fscanf(in,"%d %s",&s,a);
		int size = strlen(a);
		int friends = 0;
		int p = (a[0] - '0');
		for(int i=1;i<size;i++) {
			if((a[i] - '0') == 0) continue;
			if(i > p) { 
				friends += (i - p);
				p += friends;
				p += (a[i] - '0');
			} 
			else p += (a[i] - '0');
		}
		fprintf(out,"Case #%d: %d",t,friends);
		if(t != test) fprintf(out,"\n");
	}
	return 0;
}