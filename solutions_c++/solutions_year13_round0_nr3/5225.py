#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
using namespace std;
char c[101];
int ita(int num){
	int i;
	for(i=0;;i++){
		if(num==0)	break;
		c[i]=(num%10)+48;
		num/=10;
	}
	c[i]='\0';
	return i;
}
int pel(int num){
	int i,x,y;
	int len=ita(num);
	if(len%2==0){
		len/=2;
		x=len;
		y=(x-1);
	}
	else{
		len/=2;
		x=len+1;
		y=(x-2);
	}
	for(i=0;i<len;i++)
		if(c[x+i]!=c[y-i])	break;
	if(len==i)	return 1;
	else	return 0;
}
int main(){
	int t;
	FILE *f1=fopen("C-small-attempt0.in","r");
	FILE *f2=fopen("C-small-attempt0.out","w");
	fscanf(f1,"%d",&t);
	for(int i=0;i<t;i++){
		int c1,c2,cnt=0;
		long long s,e,j;
		fscanf(f1,"%lld %lld",&s,&e);
		long long d1=(long long)sqrt((double)s),d2=(long long)sqrt((double)e);
		if((d1*d1)==s)	j=s;
		else{	j=(d1+1)*(d1+1);d1++;}
		for(;j<=(d2*d2);){
			c1=pel(d1);
			c2=pel(j);
			if(c1==1 && c2==1)	cnt++;
			d1++;
			j=d1*d1;
		}
		fprintf(f2,"Case #%d: %d\n",i+1,cnt);
	}
	fclose(f1);
	fclose(f2);
}