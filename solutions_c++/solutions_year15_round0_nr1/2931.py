#include <cstdio>
using namespace std;
char buf[1100];
int main()
{
	FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int I=1;I<=T;I++) {
			int x;
			fscanf(fin,"%d%s",&x,buf);
			int cur=0,ret=0;
			cur+=buf[0]-'0';
			for(int j=1;j<=x;j++) {
				while(buf[j]!='0'&&cur<j) {
					cur++;
					ret++;
				}
				cur+=buf[j]-'0';
			}
			fprintf(fout,"Case #%d: %d\n",I,ret);
	}
	fclose(fin);fclose(fout);
	return 0;
}
