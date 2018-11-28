#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;
int po[10],chk[10];
int getStart(int now){
	int s=9;
	while(now/po[s]==0){
		--s;
	}
	return s;
}
int main () {
	FILE* fp=fopen("A-large.in","r");
	FILE* fp2=fopen("A.txt","w");
	int n,now;
	po[0]=1;
	for(int i=1;i<10;++i) po[i]=po[i-1]*10;
	fscanf(fp,"%d",&n);
	for(int i=1;i<=n;++i){
		fscanf(fp,"%d",&now);
		if(now==0){
			fprintf(fp2,"Case #%d: %s\n",i,"INSOMNIA");
			continue;
		}
		fill(chk,chk+10,0);
		int ck=0;
		int temp=now;
		while(ck<10){
			int s=getStart(now);
			for(int i=s;i>=0;--i) {
				if(chk[now/po[i]%10]) continue;
				chk[now/po[i]%10]=1,ck++;
			}
			now+=temp;
		}
		fprintf(fp2,"Case #%d: %d\n",i,now-temp);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}