#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
using namespace std;
long long miList[9][16];
int resultCount=0;
int y=0;
vector< vector<long long> > anotherList;
vector<long long> resultList;
bool test(char numList[],int length){
    vector<long long> anotherResult(9,0);
    long long num=1;
    long long needadd;
    bool isprime;
    for (int k=0; k<9; k++) {
        num=1;
        isprime=false;
        for(int x=0;x<length-1;x++){
            if (numList[x]=='1'){
                needadd=miList[k][length-x-2];
                num+=needadd;
            }
        }
        for (long long x=2; x*x<num; x++) {
            if (num%x==0){
                anotherResult[k]=x;
                isprime=true;
                break;
            }
        }
        if (isprime==false)
            return false;
    }
    if(resultCount>0&&find(resultList.end()+resultCount-y,resultList.end(),num)==resultList.end()){
        resultCount--;
        anotherList.push_back(anotherResult);
        resultList.push_back(num);
    }
    return true;
}
//string largePath="/Users/lxq/Downloads/A-large-practice.in.txt";
void isprime(char numList[],int min,int max){
    numList[min]='1';
    if (resultCount>0) {
        test(numList,max+2);
        if (max>min)
            isprime(numList, min+1, max);
    }
    numList[min]='0';
    if (resultCount>0) {
        test(numList,max+2);
        if (max>min)
            isprime(numList, min+1, max);
    }
}
int main() {
    /**
     *   计算2到10为底的幂
     **/
    for (int mi=2; mi<=10; mi++) {
        for (int k=1; k<=16; k++) {
            miList[mi-2][k-1]=pow(mi,k);
        }
    }
    int sumCount;
    int x = 0;
    FILE *fp=fopen("/Users/lxq/Downloads/A-large.in.txt","r");
    FILE *fw=fopen("/Users/lxq/Downloads/A-large.out.txt","w");
    if (fp) {
        fscanf(fp,"%d",&sumCount);
        for (int j=0; j<sumCount; j++) {
            fscanf(fp,"%d %d\n",&x,&y);
            resultCount=y;
            char tempNum[17];
            tempNum[0]='1';
            tempNum[x-1]='1';
            for (int k=1; k<x-1; k++) {
                tempNum[k]='0';
            }
            tempNum[x]='\0';
            isprime(tempNum,1,x-2);
        }
    }
    for (int i=0; i<sumCount; i++){
        fprintf(fw,"Case #%d:\n",i+1);
        for (int j=0; j<y; j++) {
            fprintf(fw,"%lld ",resultList[i*y+j]);
            for (int k=0; k<8; k++)
                fprintf(fw,"%lld ", anotherList[i*y+j][k]);
            fprintf(fw,"%lld\n", anotherList[i*y+j][8]);
        }
    }
    return 0;
}