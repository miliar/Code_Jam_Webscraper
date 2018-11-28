#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <list>
#include <algorithm> 
#include <vector>
#include <bitset>
#include <map>

#define MAXLEN 200

#define GETNEXT(buf,index)  {if(index==-1){index++;}else{bool flag = true; \
                            while(buf[index] == ' ' || flag)\
                            { index++; flag &= buf[index] != ' ';}}} 

#define GETNEXTI(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
                                 while(buf[index] == ' ' || flag)\
                                 { index++; flag &= buf[index] != ' ';}}val=atoi(&buf[index]);} 

#define GETNEXTIB(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
                                 while(buf[index] == ' ' || flag)\
                                 { index++; flag &= buf[index] != ' ';}}val=atoib(&buf[index]);} 
                                 
#define GETNEXTD(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
                                 while(buf[index] == ' ' || flag)\
                                 { index++; flag &= buf[index] != ' ';}}val=atof(&buf[index]);} 

using namespace std;
typedef unsigned int UINT;
FILE* fp;

int ProcessTestCase()
{
    char buf[MAXLEN];
    fgets(buf, MAXLEN, fp);
    int N = atoi(buf);
    
    char strList[MAXLEN][MAXLEN];
    int  strCnt[MAXLEN][MAXLEN];
    int  strMetaLen[MAXLEN];
    
    for (int i=0; i<N; i++){
        fgets(buf, MAXLEN, fp);
        int j,k;
        for (j=0,k=-1; buf[j] != '\n'; j++){
            if (j == 0 || buf[j] != buf[j-1]){
                k++;
                strList[i][k] = buf[j];
                strCnt[i][k] = 1;
            } else {
                strCnt[i][k]++;
            }
        }
        strMetaLen[i] = k+1;
    }
    
    // length check
    for (int i=1; i<N; i++){
        if (strMetaLen[i] != strMetaLen[0]) return -1;
    }
    
    int M = strMetaLen[0];
    // char check
    for (int i=0; i<M; i++){
        for(int j=1; j<N; j++){
            if (strList[j][i] != strList[0][i]) return -1;
        }
    }
    
    // catculate
    int result = 0;
    for (int i=0; i <M; i++){
      // total cnt of ith char
      int totalCnt = 0;
      for (int j=0; j<N; j++) { totalCnt += strCnt[j][i]; }
      
      int avgCnt = (totalCnt / N);
      
      int totalSD = 0;
      for (int k=0; k <N; k++){
         totalSD += abs(avgCnt - strCnt[k][i]);
      }
      
      result += totalSD;
    }
    
    return result;
}

int main()
{
  fp = fopen("input.txt", "r");
  char buf[MAXLEN];
  fgets(buf, MAXLEN, fp);

  int T = atoi(buf);
  cout << endl;
  for(int i=1; i<=T; i++){
    cout << "Case #" << i << ": ";
    int ret = ProcessTestCase();
    if (ret < 0) cout << "Fegla Won" << endl;
    else cout << ret << endl;
  }
  fclose(fp);

  return 0;
}
