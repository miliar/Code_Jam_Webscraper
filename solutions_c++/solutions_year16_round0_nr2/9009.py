#include<iostream>
using namespace std;
int allFliped(char* stack);
main(void){

	int t;
	FILE *fpin, *fpout;
	
	fpin = fopen ("sin2.txt", "r");
	fpout = fopen ("sout2.txt", "w");
	
	//cin>>t;
	fscanf(fpin,"%d",&t);
	for(int i=0;i<t;i++){
		char stack[100]={'-',};
		int j=0;

		//cin>>stack;
		fscanf(fpin,"%s",stack);
		int a=0;
		while(!allFliped(stack)){
		
		
			if('-'==stack[j]){
			
				while('+'!=stack[j]&&j<100){
					j++;
				}
				for(int k=0;k<j;k++){
					if(stack[k]=='+')
						stack[k]='-';
					else
						stack[k]='+';
					
				}
				a++;
				j=0;
			}
			else
				j++;		
		}
		//cout<<a<<"\n";	
		fprintf(fpout,"Case #%d: %d\n",i+1,a);
	}
	
	fclose(fpin);
	fclose(fpout);
}
int allFliped(char* stack){
	int b=0;
	while(b<100){
		if(stack[b]=='-'){
			return 0;
		}
		b++;
	}
	return 1;
	
}
