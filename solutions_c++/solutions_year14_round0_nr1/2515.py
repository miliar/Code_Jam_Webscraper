//
//  main.cpp
//  prac
//
//  Created by Deshmukh  on 17/03/14.
//  Copyright (c) 2014 Deshmukh . All rights reserved.
//

#include <iostream>
#include<string>
#include<ctime>
#include<fstream>

int main(int argc, const char * argv[])
{   using namespace std;
    ofstream output;
    ifstream input;
    int a[5][5],b[5][5],t,row1,row2,i,j,num,d1[5],d2[5],val,t1=1;
    input.open("/Users/deshmukh/Desktop/c/Udit/codejam/input/sample");
    output.open("/Users/deshmukh/Desktop/c/Udit/codejam/output/output1.txt");
    input>>t;
    while(t1<=t){
        num=0;
        input>>row1;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                input>>a[i][j];
            }
        }
        input>>row2;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                input>>b[i][j];
            }
        }
        for(i=1;i<=4;i++){
            d1[i]=a[row1][i];
            d2[i]=b[row2][i];
        }
        
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                if(d1[i]==d2[j]){
                    num++;
                    val=d1[i];
                    break;
                }
            }
            if(num>1)
                break;
        }
        if(num==0)
            output<<"Case #"<<t1<<": Volunteer cheated!\n";
        if(num==1)
            output<<"Case #"<<t1<<": "<<val<<"\n";
        if(num>1)
            output<<"Case #"<<t1<<": Bad magician!\n";
        t1++;
        
    }
    
    
    
    
    
   
    return 0;
}

