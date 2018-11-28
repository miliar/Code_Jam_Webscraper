#include<stdio.h>
#include<cstring>
#include<cstdlib>

using namespace std;

FILE *in, *out;
int main(void){
	in = fopen("A-large.in","r");
	out = fopen("A-large.out","w");
	int t;
	fscanf(in,"%d",&t);
	for(int i=1;i<=t;++i){
		int k;
		fscanf(in,"%d",&k);
		char g;
		fscanf(in,"%c",&g);
		char cad[1001];
		fscanf(in,"%s",cad);
		int st = 0;
		int tot = 0;
		for(int j=0;j<=k;++j){
			int x = cad[j]-'0';
			if(st<j){
				tot+=(j-st);
				st = j;
			}
			st+=x;
		}
		fprintf(out,"Case #%d: %d\n",i,tot);		
	}
	return 0;
}
