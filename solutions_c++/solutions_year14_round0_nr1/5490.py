#include <stdio.h>
#include <memory.h>

FILE *in=fopen("A-small-attempt0.in","rt");
FILE *out=fopen("output.txt","wt");

int check[20];

void input()
{
	for(int k=1; k<=2; k++)
	{
		int r;
		fscanf(in,"%d",&r);
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) {
				int x;
				fscanf(in,"%d",&x);
				if(i==r) check[x]++;
			}
		}
	}
}

void process()
{
	int card=0,cnt=0;
	for(int i=1; i<=16; i++) {
		if(check[i]==2) {
			card=i;
			cnt++;
		}
	}

	if(cnt>1) fprintf(out,"Bad magician!");
	else if(cnt==1) fprintf(out,"%d",card);
	else fprintf(out,"Volunteer cheated!");
}

int main()
{
	int t;
	fscanf(in,"%d",&t);
	for(int i=1; i<=t; i++) {
		memset(check,0,sizeof(check));
		fprintf(out,"Case #%d: ",i);
		input();
		process();
		fprintf(out,"\n");
	}
	return 0;
}