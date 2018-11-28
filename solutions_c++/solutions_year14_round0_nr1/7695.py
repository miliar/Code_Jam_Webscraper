//
//  main.cpp
//  magic
//
//  Created by 皇甫 静静 on 14-4-12.
//  Copyright (c) 2014年 hfjj. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");

int matrix[4][4]={0};
int line1[4]={0};
int line2[4]={0};
int num=1;

int main(int argc, const char * argv[])
{

    int group;
    int ans1;
    int ans2;
    fin>>group;
    for (int t=0;t<group;++t){
        fin>>ans1;
        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                fin>>matrix[i][j];
            }
        }
        for (int i=0;i<4;++i){
            line1[i]=matrix[ans1-1][i];
        }
        
        fin>>ans2;
        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                fin>>matrix[i][j];
            }
        }
        for (int i=0;i<4;++i){
            line2[i]=matrix[ans2-1][i];
        }
        
        int count=0;
        int ans=0;
        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                if (line1[i]==line2[j]){
                    count++;
                    ans=line1[i];
                }
                
            }
        }
        
        fout<<"Case #"<<num<<": ";
        if (count==0){
            fout<<"Volunteer cheated!"<<'\n';
            
        }
        if (count==1){
            fout<<ans<<'\n';
        }
        if (count>1){
            fout<<"Bad magician!"<<'\n';
        }
        
        
        ++num;
        
    }
    return 0;
}

