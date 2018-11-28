#include <cstdio>
#include <cstring>
#include <cstdlib>
int main () {
	int n;
	FILE* fp=fopen("B-large.in","r");
	FILE* fp2=fopen("B.txt","w");
	char str[111];
	fscanf(fp,"%d",&n);
	for(int i=0;i<n;++i){
		int s[111],cnt=0;
		fscanf(fp,"%s",&str);
		for(int i=0;i<strlen(str);i++){
			if(str[i]=='+') s[i]=1;
			else s[i]=0;
		}
		int now=strlen(str)-1;
		while(now>=0){
			if(s[now]){
				--now;
				continue;
			}
			for(int i=0;i<now;++i) s[i]^=1;
			cnt++,--now;
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,cnt);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}