/*
 * waiter.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: phinjirp
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count(char stack[100]){
	int n = strlen(stack);
	char state = stack[0];
	int i=1;
	int flip = 0;
	while(i < n){
		while(stack[i] == state && i < n)++i;

		if(i < n){
			++flip;
			if(state == '-')state = '+';
			else state = '-';
		}
	}
	if(state == '-') ++flip;
	return flip;
}

int main(){
	int t;
	FILE *fin,*fout;
	char stack[100];
	memset(stack,0,sizeof(stack));

	fin = fopen("input.txt","r");
	fout = fopen("output.txt","w+");
	fscanf(fin,"%d",&t);
	for(int i = 1 ; i <= t ; ++i)
	{
		fscanf(fin,"%s",stack);
		fprintf(fout,"Case #%d: %d\n",i,count(stack));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}



