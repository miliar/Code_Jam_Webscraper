#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#define true 1
#define false 0

using namespace std;

void add (int n, int *v) {
	int pot=0;
	int p,q;
	if (n<10) {
		v[n]=1;
		return;
	}
	for (int i=1;pot==0;i++) {
		p=1;
		for (int k=1;k<=i;k++) p=p*10;
		if (n-p<=0) pot=i; 		// pot recebe quantas casas o número tem
	}
	for (int i=pot;i>0;i--) {
		for (int j=0;j<=9;j++) {
			p=1;
			for (int k=1;k<=(i-1);k++) p=p*10;
			if (n==(p*10)) {
				v[0]=1;
				v[1]=1;
			}
			if ( (n!=p) && ((n-(j+1)*p)<0) ) {
				v[j]=1;
				n=n-j*p;
				break;
			}
		}
	}
}

bool check (int *v) {
	if (v[0]==1 && v[1]==1 && v[2]==1 && v[3]==1 && v[4]==1 && v[5]==1 && v[6]==1 && v[7]==1 && v[8]==1 && v[9]==1)
		return true;
	else return false;
}

int main () { 
	int t,n,test;
	int v[10]={0,0,0,0,0,0,0,0,0,0};
	int *r;
	bool acabou;
	FILE *in;
	FILE *out;
	in = fopen ("A-large.in","r");
	out = fopen ("Al.txt","w");
	fscanf (in,"%d",&t);
	if (t<101) r = (int*) malloc (t*sizeof(int));
	if (t>100) r = (int*) malloc (100*sizeof(int));
	for (int i=1;(i<=t)&&(i<101);i++){
		fscanf(in,"%d",&n);
		test=0;
		for (int j=0;j<10;j++) v[j]=0;
		acabou=false;
		for (int j=1;(n!=0) && (acabou==false);j++) {
			test=n*j;
			add (test,v);
			acabou=check(v);
		}
		if (n!=0) r[i-1]=test;
		if (n==0) r[i-1]=0;
	}
	for (int i=0;(i<t) && (i<100);i++) {
		if (r[i]!=0) fprintf(out,"Case #%d: %d",i+1,r[i]);
		if (r[i]==0) fprintf(out,"Case #%d: INSOMNIA",i+1);
		if ((i!=t-1) && (i!=99)) fprintf(out,"\n");
	}
	fclose(in);
	fclose(out);
	return 0;
}