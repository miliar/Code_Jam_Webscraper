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

#define U32	unsigned long long

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
int g_nRow;
int g_nColumn;
int g_arrMatrix[200][200];
char g_arrStatus[2][32] = {"YES","NO"};
#define DEF_NO	1
#define DEF_YES	0

int checkRowOrColumn(int nVal, int nIsRow, int nFix) {
	int nCnt;
	int nMax;
	int nFlag = 1;
	if(nIsRow)
		nMax = g_nRow;
	else
		nMax = g_nColumn;
	for(nCnt=0; nCnt<nMax; nCnt++) {
		if(nIsRow && g_arrMatrix[nCnt][nFix]>nVal) {
			nFlag = 0;
			break;
		}else if(nIsRow==0 && g_arrMatrix[nFix][nCnt]>nVal) {
			nFlag = 0;
			break;
		}
	}
	return nFlag;
}

int doSpecificJob(int nTestCase)
{
	int nCnt;
	int nRow;
	int nStatus = DEF_YES;
	int nB1;
	int nB2;

	////read matrix
	TSSCANF(&g_nRow);
	TSSCANF(&g_nColumn);
	for(nRow=0; nRow<g_nRow; nRow++) {
		for(nCnt=0; nCnt<g_nColumn; nCnt++) {
			TSSCANF(&g_arrMatrix[nRow][nCnt]);
		}
	}
	////check conditions
	for(nRow=0; nRow<g_nRow; nRow++) {
		for(nCnt=0; nCnt<g_nColumn; nCnt++) {
			nB1 = checkRowOrColumn(g_arrMatrix[nRow][nCnt],1,nCnt);
			if(nB1==0) {
				nB2 = checkRowOrColumn(g_arrMatrix[nRow][nCnt],0,nRow);
				if(nB2==0) {
					nStatus = DEF_NO;
					goto LABEL_ENDOF_CHECK;
				}
			}
		}
	}

LABEL_ENDOF_CHECK:
	printf("Case #%d: %s\n",nTestCase,g_arrStatus[nStatus]);
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
