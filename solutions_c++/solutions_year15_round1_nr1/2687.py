#include<cstdio>
using namespace std;
int m[10005]={0},n;
int metodo1(){
	int hongos=0,ctd=n-1;
	for(int i=0;i<ctd;i++){
		if(m[i]>m[i+1]){
			hongos+= (m[i]-m[i+1]);
		}
	}
	return hongos;
}
int metodo2(){
	int maxI=0, hongos=0, ctd = n-1;
	for(int i=0;i<ctd;i++){
		if(m[i]>m[i+1]){
			int interv = m[i]-m[i+1];
			if(interv>maxI) maxI = interv;
		}
	}
	for(int i=0;i<ctd;i++){
		if(m[i]<maxI) hongos+=m[i];
		else hongos+=maxI;
	}
	return hongos;
}
int main(){
	//FILE * pFile;
	int t,iT,met1,met2;
	//pFile = fopen("output-b.txt","w");
	scanf("%d",&t);
	for(iT=1;iT<=t;iT++){
		scanf("%d",&n);
		for(int j=0;j<n;j++){
			scanf("%d",&m[j]);
		}
		met1 = metodo1();
		met2 = metodo2();
		printf("Case #%d: %d %d\n",iT,met1,met2);
		//fprintf(pFile,"Case #%d: %d %d\n",iT,met1,met2);
	}
	//fclose(pFile);
	return 0;
}
