#include <cstring>
#include <iostream>
#include <iomanip>
#include <stack>
//#include <hash_map>
//#include <hash_set>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <queue>
#include <stack>
#include <string>
#include <ctime>
#include <bitset>
using namespace std;
//using namespace stdext;

FILE *inFile, *outFile;
int A[5][5], B[5][5], ans1, ans2;
int main(){
	inFile=fopen("A-small-attempt0.in", "r");
	outFile=fopen("out.txt", "w");
	int T;
	fscanf(inFile, "%d", &T);
	for(int k=1; k<=T; ++k){
		fscanf(inFile, "%d", &ans1);
		for(int i=1; i<5; ++i)
			for(int j=1; j<5; ++j)
				fscanf(inFile, "%d", *(A+i)+j);
		fscanf(inFile, "%d", &ans2);
		for(int i=1; i<5; ++i)
			for(int j=1; j<5; ++j)
				fscanf(inFile, "%d", *(B+i)+j);
		int count=0, val;
		for(int i=1; i<5; ++i)
			for(int j=1; j<5; ++j)
				if(A[ans1][i]==B[ans2][j]){
					++count;
					val=A[ans1][i];
				}
		if(count==0) fprintf(outFile, "Case #%d: Volunteer cheated!\n", k);
		else if(count>1) fprintf(outFile, "Case #%d: Bad magician!\n", k);
		else fprintf(outFile, "Case #%d: %d\n", k, val);
	}
	fclose(inFile);
	fclose(outFile);
	return 0;
}