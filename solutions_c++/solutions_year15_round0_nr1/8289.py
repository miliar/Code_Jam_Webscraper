#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[]){
	int nbpD, nbp, i, smax, nbT, nbTR, car, ch, min;
	FILE* input=NULL;
	FILE* output=NULL;
	input=fopen(argv[1],"r");
	if(input!=NULL){
		fscanf(input, "%d", &nbT);
		nbTR=0;
		min=0;
		output=fopen("output.txt", "w");
		while(nbTR!=nbT){
			car=fgetc(input);
			fscanf(input, "%d", &smax);
			car=fgetc(input);
			nbp=0;
			for(i=0;i<=smax;i++) nbp+=(fgetc(input)-48);
			nbpD=0; 
			fseek(input, -smax-1, SEEK_CUR);
			i=0;
			min=0;
			while(i<=smax){
				car=fgetc(input);
				if(nbpD>=i) nbpD+=(car-48);
				else if((car-48)!=0){
					min+=i-nbpD;
					nbpD=(i-nbpD)+nbpD+(car-48);
				}else;
				i++;
			}
			fprintf(output,"Case #%d: %d\n", nbTR+1, min);
			min=0;
			nbTR++;
			
		}
		fclose(output);
		fclose(input);
	}else{
		cout << "Error when oppening file \n" << argv[1] << endl;
	}
	
	return 0;
}
