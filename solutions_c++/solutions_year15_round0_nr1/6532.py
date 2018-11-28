#include<cstdio>
using namespace std;
char string[1050];
int sMax;
int ctdPersonas(){
	int ctd=0,total = string[0]-'0';
	for(int i=1;i<=sMax;i++){
		int tmp = string[i]-'0',inv=0;
		if(tmp==0) continue;
		if(total<i){
			inv = i-total;
			ctd+=inv;
		}
		total += (tmp+inv);
	}
	return ctd;
}
int main(){
	int t,iT;
	//FILE * pFile;
	//pFile = fopen("output2.txt","w");
	scanf("%d",&t);
	for(iT=1;iT<=t;iT++){
		scanf("%d",&sMax);
		scanf("%s",string);
		printf("Case #%d: %d\n",iT,ctdPersonas());
		//fprintf(pFile,"Case #%d: %d\n",iT,ctdPersonas());
	}
	//fclose(pFile);
	return 0;
}
