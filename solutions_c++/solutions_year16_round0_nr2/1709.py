/*
 * pancake.cpp
 *
 *  Created on: 09-Apr-2016
 *      Author: abhishek
 */


#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;
#define OUTPUT_CASE "Case #%d: %d\n"

#define INPUT_FILE "B-large.in"
#define OUTPUT_FILE "output_Blarge.txt"

void read_and_solve(int case_no, FILE *fp, FILE *fout){

	char porder[101];
	int len = 0;

	fscanf(fp,"%s",porder);
	len = strlen(porder);

	//cout << "case:" << case_no << " len:" << len << " str:" << porder <<endl;

	int nInflection = 0;
	char prevChar, currChar;
	char bottomChar;

	int swaps = 0;

	int i;

	prevChar = porder[0];
	for(i = 1; i< len ; i++){
		currChar = porder[i];
		if(currChar == prevChar){
			continue;
		}
		//inflection point found
		nInflection++;
		prevChar = currChar;
	}

	bottomChar = prevChar;
	swaps = nInflection;
	if(bottomChar == '-'){
		swaps++;
	}

//	for(i=0;i<s_max+1;i++){
//		fscanf(fp,"%c",&shyness_char);
//		n_shyness = shyness_char - '0';
//
//		if(runningCount>=i){
//			// we have required no of people
//			runningCount += n_shyness;
//		}else{
//			// need to invite
//			int invite = i - runningCount;
//			invitedCount += invite;
//			runningCount += n_shyness;
//			runningCount += invite;
//		}
//	}

	fprintf(fout,OUTPUT_CASE,case_no,swaps);
}

int main(){
	int no_test;
	FILE *fp;
	FILE *fout;
	int i;
	fp = fopen(INPUT_FILE,"r");
	fout = fopen(OUTPUT_FILE,"w");

	if(fp == NULL || fout == NULL)
		return 1;



	fscanf(fp,"%d\n",&no_test);
	//fscanf(fp,"%*[^\n]");
	//fscanf(fp); // consume new line

	for(i=1;i<=no_test;i++){
		read_and_solve(i,fp, fout);
		//char temp[20];
		//fgets(temp, 20, fp); //comsume empty line
	}

	fflush(fout);
	fclose(fp);
	fclose(fout);
	return 0;

}

