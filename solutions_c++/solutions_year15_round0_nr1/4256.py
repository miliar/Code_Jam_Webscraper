

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	FILE* f;
	FILE* g;
	int tests,n;
	char shy[1200];
	int val;
	int standing;
	int needed;
	
	f = fopen("input.txt","r");
	g = fopen("output.txt","w");
	
	fscanf(f,"%d",&tests);
	for (int t=1;t<=tests;t++) {
		fscanf(f,"%d",&n);
		fscanf(f,"%s",shy);
		standing = 0;
		needed = 0;
		
		for (int k=0;k<=n;k++) {
			val = shy[k]-48;
			
			if (k>standing) {
				needed+=k-standing;
				standing+=k-standing;
			}
			
			standing+=val;
		}
		
		fprintf(g,"Case #%d: %d\n",t,needed);
	}
	return 0;
}

