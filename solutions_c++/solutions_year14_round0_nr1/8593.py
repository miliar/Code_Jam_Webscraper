#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXLEN 500

#define GETNEXT(buf,index)  {if(index==-1){index++}else{bool flag = true; \
		                    while(buf[index] == ' ' || flag)\
		                    { index++; flag &= buf[index] != ' ';}}} 

#define GETNEXTI(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
		                         while(buf[index] == ' ' || flag)\
		                         { index++; flag &= buf[index] != ' ';}}val=atoi(&buf[index]);} 
								 
#define GETNEXTD(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
		                         while(buf[index] == ' ' || flag)\
		                         { index++; flag &= buf[index] != ' ';}}val=atof(&buf[index]);} 

using namespace std;
typedef unsigned int UINT;
FILE* fp;

int ProcessTestCase()
{
	char buf[MAXLEN];

	// 1st question
	fgets(buf, MAXLEN, fp);
	int r1 = atoi(buf);
	for (int i = 1; i <= 4; i++){
	   if (i == r1){
	       fgets(buf, MAXLEN, fp);
	   } else {
	   	char buf1[MAXLEN];
		fgets(buf1, MAXLEN, fp);
	   }
	}
    
	int map[17];
	for (int i=1; i <= 16; i++) map[i] = 0;
	
	char* pEnd;
	map[(int)strtod(buf, &pEnd)] = 1;
	map[(int)strtod(pEnd, &pEnd)] = 1;
    map[(int)strtod(pEnd, &pEnd)] = 1;
	map[(int)strtod(pEnd, NULL)] = 1;

	// 2nd question
	fgets(buf, MAXLEN, fp);
	int r2 = atoi(buf);
	for (int i = 1; i <= 4; i++){
	   if (i == r2){
	       fgets(buf, MAXLEN, fp);
	   } else {
	   	char buf1[MAXLEN];
		fgets(buf1, MAXLEN, fp);
	   }
	}

	bool found = false;
	int val;
	int card;
	
	val = (int)strtod(buf, &pEnd);
	if ( map[val] == 1) {
	    found = true;
		card = val;
	}
	
	val = (int)strtod(pEnd, &pEnd);
	if ( map[val] == 1) {
	    if (found) return -1;
		found = true;
		card = val;
	}
	
	val = (int)strtod(pEnd, &pEnd);
	if ( map[val] == 1) {
	    if (found) return -1;
		found = true;
		card = val;
	}

	val = (int)strtod(pEnd, NULL);
	if ( map[val] == 1) {
	    if (found) return -1;
		found = true;
		card = val;
	}

	if (!found) return 0;
	
    return card;
}

int main()
{
  fp = fopen("A-small-attempt0.in", "r");
  char buf[MAXLEN];
  fgets(buf, MAXLEN, fp);

  int T = atoi(buf);
  for(int i=1; i<=T; i++){
    cout << "Case #" << i << ": ";
	int j = ProcessTestCase();
	if (j >= 1 && j <= 16) cout << j;
	else if (j == -1) cout << "Bad magician!";
	else cout << "Volunteer cheated!";
	cout << endl;
  }
  fclose(fp);

  return 0;
}
