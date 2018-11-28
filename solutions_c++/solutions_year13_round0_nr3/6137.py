#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

FILE * saida;
FILE * input;

bool isPerfectSquare(long a){
	double res = sqrt(a);
	long b = (long) res;	
}

bool isPalindrome(char * pal){
	bool result = true;
	int tam = strlen(pal);
	for(int i = 0; i < tam; i++){
		if(pal[tam -1 -i] != pal[i]){result = false;}
	}	
	return result;
}

bool isFairSquare(int num){
	bool result;
	char aux[200];
	char auxroot[200];
	itoa(num,aux,10);
	float rootf = sqrt(num);
	int rooti = (int) rootf;
	if(rootf - rooti != 0){
		result = false;
	}else{
		itoa(rooti,auxroot,10);
		if(isPalindrome(aux) && isPalindrome(auxroot)){result = true;}	
	}
	return result;
}

void splitOnce(char target, char * in, char * substring1, char * substring2){
	int tam = strlen(in);
	bool targetFound = false;
	int position;
	for(int i=0 ; i<tam ; i++){
		if(in[i] == target && !targetFound){
			substring1[i]='\0';
			targetFound = true;
			position = i;
		}else if(targetFound){
			substring2[i-1-position] = in[i];
		}else{
			substring1[i] = in[i];
		}
	}
	substring2[tam - position -2] = '\0';
}



int main(){
	saida = fopen("saida.txt","w");
	input = fopen("C-small-attempt0.in","r");
	int count =0;
	int intervalInic,intervalEnd;
	char line[200];
	char line1[200];
	char line2[200];
	int current;
	int numIntervals = atoi(fgets(line, 80, input));
	
	for(current=1; current <= numIntervals ; current++){
		fgets(line, 80, input);
		splitOnce(' ',line,line1,line2);
		intervalInic = atoi(line1);
		intervalEnd = atoi(line2);
		for(int i = intervalInic; i <= intervalEnd ; i++){
			if(isFairSquare(i)){
				count++;	
			}
		}
		fprintf(saida,"Case #%d: %d\n",current,count);
		count = 0;
	}
	getch();
	fclose(saida);
	return 0;	
}
