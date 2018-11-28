#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void virar (char *s,int tam) {
 	int menos;
 	char esq,dir;
 	menos=3000;
	for (int i=0;i<tam;i++) 
		if (s[i]=='-') menos=i;
	if (menos==0) s[0]='+';
	else if (s[0]=='+') {
		for (int i=0;i<tam;i++) {
			if (s[i]=='+') s[i]='-';
			else if (s[i]=='-') break;
		}
	}
	else if (s[0]=='-') {
		for (int i=0;i<((menos+2)/2);i++) {
			esq=s[i];
			dir=s[menos-i];
			if (esq=='+') s[menos-i]='-';
			if (esq=='-') s[menos-i]='+';
			if (dir=='+') s[i]='-';
			if (dir=='-') s[i]='+';
		}
	}
}

bool check (char *s,int tam) {
	for (int i=0;i<tam;i++)
		if (s[i]=='-') return false;
	return true;
}

int main () {

	char s[102];
	int *r,tam,res;
	FILE *in;
	FILE *out;
	int t;
	bool acabou=false;
	in = fopen ("B-large.in","r");
	out = fopen ("Bl.txt","w");

	fscanf(in,"%d",&t);
	if (t<101) r = (int*) malloc (t*sizeof(int));
	if (t>100) r = (int*) malloc (100*sizeof(int));	

	for (int i=0;i<t;i++) {
		fscanf (in,"%s",&s);
		res=0;
		acabou=false;
		tam=strlen(s);
		acabou = check (s,tam);
		if (acabou==true) r[i]=0;
		for (int j=1;(acabou==false) && (j<101);j++) {
			virar(s,tam);
			acabou = check (s,tam);
			res=j;
		}
		r[i]=res;
	}

	for (int i=0;(i<t) && (i<100);i++) {
		fprintf(out,"Case #%d: %d",i+1,r[i]);
		if ((i!=(t-1)) && (i!=99)) fprintf(out,"\n");
	}

	fclose(in);
	fclose (out);
	return 0;
}