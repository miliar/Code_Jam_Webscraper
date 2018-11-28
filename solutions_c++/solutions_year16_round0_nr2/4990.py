#include <cstdio>
#include <cstring>

char s[101];

int sameind(char c[]){
	char mat = c[0];
	int ind = 0;
	for(int i=1;i<strlen(c);i++){
		if(mat==c[i]) ind++;
		else break;
	}
	return ind;
}

void swift(char c[],int b,int len){
	for(int i=b;i<b+len/2;i++){
		char tmp = c[i];
		c[i] = c[len+b-i-1];
		c[len+b-i-1] = tmp;
	}
	for(int i=b;i<b+len;i++){
		if(c[i]=='+') c[i] = '-';
		else c[i] = '+';
	}
}

int main()
{
	FILE* r = fopen("B-large.in","r");
	FILE* w = fopen("B.out","w");
	int T;
	fscanf(r,"%d",&T);
	for(int i=0;i<T;i++){
		fscanf(r,"%s",s);
		int si=sameind(s);
		int num=0;
		while(si!=strlen(s)-1||s[0]!='+'){
			swift(s,0,si+1);
			si=sameind(s);
			num++;
		}
		fprintf(w,"Case #%d: %d\n",i+1,num);
	}
	fclose(r);
	fclose(w);
	return 0;
}
