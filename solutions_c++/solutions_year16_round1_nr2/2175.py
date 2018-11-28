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
    int T,N;
    openfile >> T;
    for (int cases = 1; cases <= T; cases++) {
        outfile << "Case #" << cases << ": ";
        openfile >> N;
        int ans[2500]={0};
        for(int i=0;i<2500;i++)
            ans[i]=0;
        for(int i=0;i<N*(N*2-1);i++){
            int temp;
            openfile>>temp;
            ans[temp-1]++;
        }
        for(int i=0;i<2500;i++){
            if(ans[i]%2!=0)outfile<<i+1<<" ";
        }

        outfile<<endl;
    }
    openfile.close();
    return 0;
}