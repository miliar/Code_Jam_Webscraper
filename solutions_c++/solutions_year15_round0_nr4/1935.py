

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	FILE* f;
	FILE* g;
	int tests;
	bool ok, ok2;
	int a,b;
	int dimin, dimax;
	int x,r,c;
	
	f = fopen("input.txt","r");
	g = fopen("output.txt","w");
	
	fscanf(f,"%d",&tests);
	for (int t=1;t<=tests;t++) {
		fscanf(f,"%d%d%d",&x,&r,&c);
		if (r>c) {
			dimax = r;
			dimin = c;
		} else {
			dimax = c;
			dimin = r;
		}
		
		if (r*c % x !=0) {
			fprintf(g,"Case #%d: RICHARD\n",t);
			continue;
		}
		if (x>c && x>r) {
			fprintf(g,"Case #%d: RICHARD\n",t);
			continue;
		}
		if (x>2*dimin-1 && x>=3) {
			fprintf(g,"Case #%d: RICHARD\n",t);
			continue;
		}
		if (dimin>3 && x>=7) {
			fprintf(g,"Case #%d: RICHARD\n",t);
			continue;
		}
		if (dimin==1) {
			fprintf(g,"Case #%d: GABRIEL\n",t);
			continue;
		}
		if (dimin==2 && x==3) {
			ok = true;
			for (int i=1; i<dimax; i++) {
				a = i*dimin;
				b = (dimax-i-1)*dimin;
				
				if ((a-1)%x==0 && b%x==0) {
					ok = false; break;
				}
				if (a%x==0 && (b-1)%x==0) {
					ok = false; break;
				}
			}
			if (ok) {
				fprintf(g,"Case #%d: RICHARD\n",t);
				continue;
			}
		}
		if (dimin==3 && x==5) {
			ok = true;
			ok2 = true;
			for (int i=1; i<dimax; i++) {
				a = i*dimin;
				b = (dimax-i-1)*dimin;
				
				if ((a-1)%x==0 && (b-1)%x==0) {
					ok = false;
				}
				if ((a-2)%x==0 && b%x==0) {
					ok2 = false;
				}
				
			}
			
			if (ok || ok2) {
				fprintf(g,"Case #%d: RICHARD\n",t);
				continue;
			} 
		}
		
		fprintf(g,"Case #%d: GABRIEL\n",t);
	}
	return 0;
}

