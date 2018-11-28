//
//  main.cpp
//  03
//
//  Created by 呂弈臻 on 2016/4/9.
//  Copyright (c) 2016年 henry. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <set>
#include <time.h>
#include <math.h>
using namespace std;

int main(int argc, const char * argv[]) {
    vector<int> pos;
    vector<int> check;
    ofstream output;
    output.open("result32.txt");
    output << "Case #1:" << endl;
    int counter = 0;
    int all_counter = 0;
    while(true) {
        srand(all_counter);
        all_counter++;
        int po = pow(2,14);
        int n = rand()%po;
        if(find(check.begin(), check.end(), n) != check.end() ){
            continue;
        }
        else{
            check.push_back(n);
        }
        int hold = n;
        string a;
        a+='1';
        string b;
        while(true){
            b += to_string(n%2);
            n /= 2;
            if (n==0) {
                break;
            }
        }
        for(int w=0;w<b.length()/2;w++){
            
            char hold2 = b[w];
     
            b[w] = b[b.length()-1-w];

            b[b.length()-1-w] = hold2;
        }
        if(b.length()<14){
            
            string holder;
            int c = 14-b.length();
            
            for (int p=0; p<c; p++) {
                holder += '0';
            }
            holder += b;
            
            a += holder;
        }
        else
            a += b;
        a += '1';
        cout << counter << " " <<a << endl;
        if(a.length() == 16){
            for (int m=0; m<a.length(); m++) {
                if(a[m]=='1')
                    pos.push_back(a.length()-1-m);
            }
            a += a;
            output << a << " ";
            for (int k=2; k<=10; k++) {
                unsigned long t = 0;
                for(int l=pos.size()-1;l>=0;l--){
                    t += pow(k,pos[l]);
                }
                if(k!=10)
                    output << t << " ";
                else
                    output << t << endl;
            }
            cout << endl;
            counter++;
            
        }
        pos.clear();
        if(counter==500)
            break;
        
    }
    return 0;
}
