#include<cstdio>
#include<cmath>
using namespace std;
int r,c,rc,x;
bool esPosible(){
	if(x>6) return false;
	if(rc%x!=0) return false;
	if(x>r&&x>c) return false;
	int max =(int)round(x/2.0);
	if(max>r||max>c) return false;
	if(x==4&&(r==2||c==2)) return false;
	return true;
}
int main(){
	//FILE * pFile;
	//pFile = fopen("boutput3.txt","w");
	int iT,t;
	scanf("%d",&t);
	for(iT=1;iT<=t;iT++){
		scanf("%d%d%d",&x,&r,&c);
		rc = r*c;
		if(esPosible()){
			 printf("Case #%d: GABRIEL\n",iT);
			 //fprintf(pFile,"Case #%d: GABRIEL\n",iT);
		}
		else{
			 printf("Case #%d: RICHARD\n",iT);
			 //fprintf(pFile,"Case #%d: RICHARD\n",iT);
		}
	}
	//fclose(pFile);
	return 0;
}
