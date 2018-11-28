/*
 * nc.cpp
 *
 *  Created on: 2013. 2. 13.
 *      Author: freetskim
 */

#include <vector>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define U32	unsigned int
#define U64	unsigned long long

//#define FILE_DBG
#ifdef FILE_DBG
#define TSSCANF(X)	fscanf(g_fp,"%d",X);
#define TSSCANFU(X)	fscanf(g_fp,"%u",X);
#define TSSCANFS(X)	fscanf(g_fp,"%s",X);
#else
#define TSSCANF(X)	scanf("%d",X);
#define TSSCANFU(X)	scanf("%u",X);
#define TSSCANFS(X)	scanf("%s",X);
#endif

#define MAXVAL	(1<<18)
using namespace std;

////general
int g_nTotalCases = 0;
FILE * g_fp = NULL;
////specific
U32 g_arrForSmallSet[6] = {1,2,3,11,22,33};

int getLog(U32 nVal)
{
	int nCnt;
	nCnt = 0;
	while(1) {
		nVal = nVal/10;
		if(nVal==0)
			break;
		nCnt++;
	}
	return nCnt;
}

U32 getSqrt(U32 nV,  U32 nInput, int nIsLower)
{
	int nCnt;
	if(nV<=0)
		nV=1;
	for(nCnt=0; nCnt<50; nCnt++) {
	 nV= (nV + (nInput / nV)) / 2;
	 if(nV==0)
		 break;
	}
	if(nIsLower) {
		while(nV*nV>nInput)
			nV--;
	}else {
		while(nV*nV<nInput)
			nV++;
	}
	return nV;
}

int doSpecificJob(int nTestCase)
{
	U32 nA;
	U32 nB;
	U32 nSA;
	U32 nSB;
	int nlA;
	int nlB;
	int nPDR = 0;

	TSSCANFU(&nA);
	TSSCANFU(&nB);
	nSA = getSqrt(nA/2,  nA ,0);
	nSB = getSqrt(nA/2,  nB ,1);
	nlA = getLog(nSA);
	nlB = getLog(nSB);
	if(nlA<3 && nlB<3) {
		int nACnt;
		int nBCnt;
		for(nACnt=0; nACnt<6; nACnt++) {
			if(nSA<=g_arrForSmallSet[nACnt])
				break;
		}
		for(nBCnt=5; nBCnt>=0; nBCnt--) {
			if(g_arrForSmallSet[nBCnt]<=nSB)
				break;
		}
		nPDR = nBCnt-nACnt+1;
	}
	printf("Case #%d: %d\n",nTestCase,nPDR);
	return 0;
}

int main(int nArgc, char * argv[])
{
	int nCnt;
#ifdef FILE_DBG
	g_fp = fopen("C:\\input.txt","r");
#endif
	TSSCANF(&g_nTotalCases);
	for(nCnt=0; nCnt<g_nTotalCases; nCnt++) {
		doSpecificJob(nCnt+1);
	}
#ifdef FILE_DBG
	fclose(g_fp);
#endif
	return 0;
}
