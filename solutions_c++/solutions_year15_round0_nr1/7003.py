#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE* rfile, *wfile;
	
	int t,cases,max_level, s_level;
	int loop,num,store,needs;
	char ch;

	rfile=fopen("open.txt","r");
	wfile=fopen("write.txt","w");
	fscanf(rfile,"%d",&t);

	
	for(cases=1;cases<=t;cases++){
		fscanf(rfile,"%d ", &max_level);
		store=0; needs=0;
		for(s_level=0;s_level<=max_level;s_level++){
			fscanf(rfile,"%c",&ch);
			num=ch-'0';
			if(store<s_level && num > 0){
				needs+=s_level-store;
				store+=s_level-store;
			}
			store+=num;
		}
		fprintf(wfile,"Case #%d: %d\n",cases,needs);
	}

	fclose(wfile);
	fclose(rfile);
	return 0;
}