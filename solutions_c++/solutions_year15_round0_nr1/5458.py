#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main(){
	
	FILE *p1,*p2;
	p1=fopen("A-large.in","r");
	p2=fopen("Output.txt","w");
	
	if(p1!=NULL){
		int T,i,n,j;
		fscanf(p1,"%d\n",&T);
		for(i=0;i<T;i++){
			fscanf(p1,"%d ",&n);
			int count=0;
			char s[n+1];
			fscanf(p1,"%s",s);
			int counter=0;
			for(j=0;j<=n;j++){
				if(counter>=j){
					counter+=(int)(s[j]-48);
				}
				else {
					count=count+j-counter;
					counter=j+(int)(s[j]-48);
				}
			}
			fprintf(p2,"Case #%d: %d\n",i+1,count);
		}
	}
	
	
	fclose(p1);
	fclose(p2);
	
	//system("PAUSE");
	return 0;
}
