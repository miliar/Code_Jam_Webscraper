//
//  main.cpp
//  CodeJam2014
//
//  Created by Ahmed M. Abd Elmeguid on 4/11/14.
//  Copyright (c) 2014 Cocoa Ninjas. All rights reserved.
//

#include <iostream>

using namespace std;
int main(int argc, const char * argv[])
{
    int TestNum;
    scanf("%d", &TestNum);
    
    int test=1;
    while (test <= TestNum) {
        
        int array1[16];
        int array2[16];
        int small[4];
        int small2[4];
        int input1;
        int input2;

        scanf("%d", &input1);

        for (int i=0; i<16; i++) {
            scanf("%d", &array1[i]);

        }
        
    
        int x=(input1-1)*4;
        for (int i=0; i<4; i++) {
            small[i]=array1[x+i];
        }
        
        scanf("%d", &input2);

        for (int i=0; i<16; i++) {
            scanf("%d", &array2[i]);

        }

        int y=(input2-1)*4;
        for (int i=0; i<4; i++) {
            small2[i]=array2[y+i];
        }
        
        int counte=0;
        int num;
        
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if (small[i] == small2[j]) {
                    counte++;
                    num=small[i];
                }
            }
        }
        
        if (counte == 1) {
            cout<<"Case #"<<test<<": "<<num<<"\n";
           
        }else if(counte > 1){
            cout<<"Case #"<<test<<": "<<"Bad magician!"<<"\n";


        
        }else{
        
            cout<<"Case #"<<test<<": "<<"Volunteer cheated!"<<"\n";

            
        }
        
               test++;
        
    }
        return 0;
}



