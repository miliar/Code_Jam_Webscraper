/* 
 * File:   main.cpp
 * Author: Rick
 *
 * Created on 11 April, 2015, 7:14 AM
 */

#include <cstdlib>
#include <string>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int t,j,i,smax,sum,total,fren,len;
    string str,s;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%d",&smax);
        getline(cin,s);
        str="";
        len=s.length();
        for(i=0;i<len;i++)
            if(s.at(i)!=' ')
                str.push_back(s.at(i));
        sum=0;total=0;fren=0;
        int arr[smax];
        /*if(str.at(0)==' ')
            str.erase(0,1);
        if(str.at(str.length()-1)==' ')
            str.erase(str.length()-1,1);*/
        
        for(i=0;i<smax;i++){
            arr[i]=(int)(str.at(i)-'0');
        }
        //printf("%s\n",str.c_str());
        /*for(i=0;i<len;i++){
            printf("%d",arr[i]);
        }*/
        if(smax==0)
            if(arr[0]<0)
                total=1;                
        for(i=0;i<smax;i++){
            sum+=arr[i];
            if(sum<(i+1)){
                fren=i+1-sum;
                sum+=fren;
                total+=fren;
            }
        }
        printf("Case #%d: %d\n",j,total);            
    }
    
    
    return 0;
}

