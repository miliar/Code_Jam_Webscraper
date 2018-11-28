//============================================================================
// Name        : codeJAM1.cpp
// Author      : Francesco Antoniazzi
// Version     :
// Copyright   : This is my source code, not yours
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int isordered(char * audience_shyness) {
	int l,i,count=0,friends=0;
	l=strlen(audience_shyness);
	//printf("l=%d\n",l);
	for (i=0; i<l-1; i++) {
		count=count+audience_shyness[i]-'0';
		if (count+friends<i+1) {
			friends=i+1-count;
		}
	}
	return friends;
}

int main() {
	FILE * input;
	FILE * output;
	int i=0, test_cases, max_shyness, j;
	char audience_shyness[1100];
	int friends[120];
	input=fopen("C:\\Users\\Francesco\\eclipse_workspace\\codeJAM1\\A-large.in","r");
	do {
		if (!i) {
			fscanf(input,"%d\n",&test_cases);
			//printf("test_cases=%d\n",test_cases);
		}
		else {
			fscanf(input,"%d %s\n",&max_shyness,audience_shyness);
			//printf("max_shyness=%d, audience_shyness=%s\n",max_shyness,audience_shyness);
			friends[i-1]=isordered(audience_shyness);
		}
		i++;
	} while (!feof(input));
	output=fopen("C:\\Users\\Francesco\\eclipse_workspace\\codeJAM1\\output.txt","w");
	for (j=1; j<=test_cases; j++) {
		fprintf(output,"Case #%d: %d\n",j,friends[j-1]);
	}
	fclose(input);
	fclose(output);
	return 0;
}
