//
//  main.cpp
//  test
//
//  Created by xanxus on 14-3-10.
//  Copyright (c) 2014年 xanxus. All rights reserved.
//

#include <map>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <stdlib.h>
#include "BinaryTree.h"

using namespace std;
void swap(vector<int>&array,int i,int j){
    int tmp=array[i];
    array[i]=array[j];
    array[j]=tmp;
}
vector<string> split(string& str,const char* sep){
    char* splitstr=new char[str.length()+1];
    strcpy(splitstr, str.c_str());
    splitstr[str.length()]='\0';
    vector<string> result;
    char* p=strtok(splitstr, sep);
    while (p) {
        result.push_back(p);
        p=strtok(NULL, sep);
    }
	if (splitstr) {
		delete splitstr;
	}
    return result;
}

void quickSort(vector<int>& array,int from,int to){
    if(to<=from)
    return;
    if(from+1==to)
    {
        swap(array, from,to);
        return;
    }
    int i=from+1,j=to;
    while(i!=j){
        while(array[i]<=array[from]&&i<j){
            i++;
        }
        while(array[j]>array[from]&&i<j){
            j--;
        }
        if(i!=j){
            swap(array, i,j);
        }
    }
    if(array[from]<array[i])
    {
        swap(array, from,i-1);
        quickSort(array, from, i-2);
        quickSort(array, i, to);
    }
    else
    {
        swap(array, from,i);
        quickSort(array, from, i-1);
        quickSort(array, i+1, to);
    }
    
}

long ip2ulong(const char* ip){
    unsigned u1,u2,u3,u4;
    if(sscanf(ip, "%u.%u.%u.%u",&u1,&u2,&u3,&u4)==4&&u1<=255&&u2<=255&&u3<=255&&u4<=255)
    return (u1<<24)+(u2<<16)+(u3<<8)+u4;
    else
    return 0;
}
int prefixcmp(long ip1,long ip2,int prefixLen){
    if(prefixLen>32)
    return -1;
    int offset=32-prefixLen;
    return (ip1>>offset)&~(ip2>>offset);
}

int partition(vector<int>& array,int m,int n){
    if (m>n) {
        return -1;
    }
    else if (m==n) {
        return m;
    }else if(m+1==n){
        if (array[m]<array[n]) {
            return m;
        }else{
            swap(array,m,n);
            return n;
        }
    }else{
        int i=m+1;
        int j=n;
        while (i<j)
        {
            while (array[i]<array[m]&&i<j) {
                i++;
            }
            while (array[j]>=array[m]&&i<j) {
                j--;
            }
            if (i!=j) {
                swap(array, i,j);
            }
        }
        if (array[i]<array[m]) {
            swap(array, m,i);
            return i;
        }else{
            swap(array, m,i-1);
            return i-1;
        }
    }
    
}
int selectNum(vector<int>& array,int from,int to,int loc){
    int firstLoc=partition(array, from, to);
    if (loc==firstLoc+1) {
        return array[firstLoc];
    }else if(loc<firstLoc+1){
        return selectNum(array, from, firstLoc-1, loc);
    }else{
        return selectNum(array, firstLoc+1, to, loc);
    }
}
int main(int argc, const char * argv[])
{
    //   int main(int argc,char** argv){
    int testCount=0;
    FILE* inputFile=fopen(argv[1], "r");
    fscanf(inputFile, "%d",&testCount);
    string* testCase=new string[testCount];
    for (int i=0; i<testCount; i++) {
        int p,q;
        fscanf(inputFile, "%d/%d",&p,&q);
        bool flag=(int)(log2(q))==log2(q);
        char resultString[50]="impossible";
        if(flag){
            double reverse=(double)q/(double)p;
            int result=ceil(log2(reverse));
            if(result<=40){
                sprintf(resultString, "%d",result);
            }
        }
        testCase[i]=resultString;
    }
    fclose(inputFile);
    FILE* outputFile=fopen("./output", "w");
    for (int i=0; i<testCount; i++) {
        fprintf(outputFile, "Case #%d: %s\n",i+1,testCase[i].c_str());
    }
    fclose(outputFile);
}

