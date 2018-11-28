#include<iostream>
#include<stdlib.h>
#include<stdio.h>

bool checkFair(int number)
{
	char iNumber[1000];
	int iFirst, iEnd = 0;
	bool bCheck;

	sprintf(iNumber,"%d",number);
	iFirst = strlen(iNumber) - 1;
	bCheck = true;
	while(iFirst > iEnd) {
		if(iNumber[iFirst] != iNumber[iEnd]) {
			bCheck = false;
			break;
		}
		iFirst--;
		iEnd++;
	}
	if(bCheck) return true;
	else return false;
}

bool checkSquare(int number) 
{
	int iNumber = (int) sqrt((float) number);
	//printf("%d\n",iNumber);
	if(iNumber*iNumber == number) {
		if( checkFair(iNumber) ) return true;
	}
	return false;
}


int main()
{
	FILE* fp = fopen("input.txt","r");
	FILE* fop = fopen("output.txt", "w");
	int iCount, A, B, iNumber, iFirst;

	fscanf(fp,"%d\n",&iCount);
	for(int i=1;i<=iCount;i++) {
		fscanf(fp,"%d %d\n",&A,&B);
		iNumber = 0;

		for(int j=A;j<=B;j++) {
			iFirst = j % 10;
			if(iFirst==1 || iFirst==4 || iFirst==5 || iFirst==6 || iFirst==9) {
				if( !checkFair(j) ) {
					//printf("%d not fair!\n",j);
					continue;
				}
				if( !checkSquare(j) ) {
					//printf("%d not square!\n",j);
					continue;
				}
				iNumber++;
			}
		}
		fprintf(fop,"Case #%d: %d\n",i,iNumber);
	}

	fclose(fp);
	fclose(fop);
	return 0;
}