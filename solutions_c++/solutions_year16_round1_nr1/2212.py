//
//  main.cpp
//  google
//
//  Created by 張語航 on 2016/4/16.
//  Copyright © 2016年 張語航. All rights reserved.
//

#include<iostream>
#include<fstream>
using namespace std;

int main() {
    ifstream openfile;
    fstream outfile;
    openfile.open("/Users/yuhang/Desktop/a.in");
    outfile.open("/Users/yuhang/Desktop/1.out", ios::out);
    int T;
    openfile >> T;
    for (int cases = 1; cases <= T; cases++) {
        outfile << "Case #" << cases << ": ";
        string temp,a="",b="";
        openfile>>temp;
        for(int i=0;temp[i]!='\0';i++){

            if(temp[i]>=temp[0]&&temp[i]>=a[0]){
                a=temp[i]+a;
            }
            else b+=temp[i];
        }
        outfile<<a+b<<endl;
    }
    openfile.close();
    return 0;
}
