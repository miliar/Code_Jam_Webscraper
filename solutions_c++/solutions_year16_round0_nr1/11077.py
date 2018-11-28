//
//  main.cpp
//  practice
//
//  Created by Nima Aghli on 4/9/16.
//  Copyright © 2016 Nima Aghli. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <climits>
#include "main.h"
using namespace std;
long long int calc(long long int value){
    if(value==0){return 0;}
    long long int temp;
    string temp_str,str2;
    uint16_t counter=0;
    uint16_t num;
    int array[10];
    array[0]=-1;
    temp=value;
    for(long long int i=2;i<LLONG_MAX;i++){
        if((value*i)>=LLONG_MAX){
            printf("Insomniya");
            return 0;}
        temp_str=to_string(temp);
        printf("value is=%s\n",temp_str.c_str());
        for(int j=0;j<temp_str.length();j++){
            str2=temp_str[j];
            printf("char[%d]=%s\n",j,str2.c_str());
            num=atoi(str2.c_str());
            if(array[num]!=num){
                array[num]=num;
                counter++;
                printf("Counter=%d\n",counter);
            }
            if(counter==10){
              printf("%s\n",temp_str.c_str());
                return temp;
            }
          
       
        }
        temp=value*i;
    }
    
    return 0;
}


int main(int argc, const char * argv[]) {
    ifstream myfile;
    ofstream output;
    output.open ("output.txt");
    myfile.open ("data.in");
    string data;
    long long int cases;
    long long int case_count=0;
    long long int temp;
    long long int res;
    getline(myfile, data);
    cases=atoi(data.c_str());
    printf("test cases =%lld\n",cases);
    if (myfile.is_open()) {
        while (std::getline(myfile, data))
        {
            case_count++;
            printf("%s\n",data.c_str());
            temp=atoll(data.c_str());
            res=calc(temp);
            if(res==0){output<<"Case #"<<case_count<<": "<<"INSOMNIA"<<endl;}
            else{output<<"Case #"<<case_count<<": "<<res<<endl;}
            
            
            
        }
    }
    myfile.close();
    
    return 0;
}
