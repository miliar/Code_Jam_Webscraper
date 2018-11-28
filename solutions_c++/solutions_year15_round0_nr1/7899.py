#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	FILE *fp1,*fp2;
	fp1 = fopen("A-large.in","r");
	fp2 = fopen("solution.txt","w");
	int t,h=1;
	fscanf(fp1,"%d",&t);
	while(t--){
		int smax,req=0,aud=0;
		char s[1101];
		fscanf(fp1,"%d %s",&smax,s);
		if(s[0]-'0'== 0){
			req++;
			aud++;
		}
		else
			aud += s[0]-'0';
		for(int i=1;i<strlen(s);i++){
			if(s[i]-'0' > 0 && aud >= i){
				aud += (s[i]-'0');
			}
			else if(s[i]-'0' > 0 && aud < i){
				req += (i-aud);
				aud += (i - aud + s[i]-'0');
			}
		}
		fprintf(fp2,"Case #%d: %d\n",h,req);
		h++;
	}
}