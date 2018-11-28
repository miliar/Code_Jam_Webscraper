/* 
 * File:   main.cpp
 * Author: devu
 *
 * Created on April 13, 2013, 1:12 PM
 */

#include <cstdlib>
#include<stdio.h>
#include<iostream>

using namespace std;

/*
 * 
 */
int validBase[7]={0,1,4,9,121,484,1024};
bool testPalin(char *arr,int len){
    int lind,hind;
    hind=len-1;
    lind=0;
    while(hind>lind){
        if(arr[hind]!=arr[lind])
            return false;
        hind--;
        lind++;
    }
    return true;
}
int findNextSquare(){
    
}
void countPalinSquare(int iter){
    int x,y;
    scanf("%d%d",&x,&y);
    int xin,yin;
    xin=0;
    yin=0;
    int i=0;
    while(validBase[i]<x&&i<7){i++;}  
    xin=i-1;
    i=6;
    while(validBase[i]>y){i--;}        
    yin=i+1;    
    int count=0;
    if(validBase[xin]==x)
        count++;
    if(validBase[yin]==y)
        count++;
    //cout<<xin<<endl;
    //cout<<yin<<endl;
    if(yin!=xin)
    count+=yin-xin-1;
    cout<<"Case #"<<iter<<": "<<count<<endl;
}
int main(int argc, char** argv) {
    int iter=0;
    int maxiter;
    scanf("%d",&maxiter);
    while(iter<maxiter){
        iter++;
        countPalinSquare(iter);
    }
    return 0;
}

