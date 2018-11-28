//
//  main.cpp
//  cookie
//
//  Created by 皇甫 静静 on 14-4-12.
//  Copyright (c) 2014年 hfjj. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");

int main(int argc, const char * argv[])
{

    int group;
    fin>>group;
    
    double c;
    double f;
    double x;
    
    double time=0.0;
    double rate=2;
    
    double gap;
    int num=1;
    double time_no_buy=0;
    double time_buy=0;
    
    for (int t=0;t<group;++t){
        
        fin>>c>>f>>x;
        time=0;
        gap=x;
        rate=2;
        
        if (x<=c){
            time=x/2;
        }
        else{
            bool flag=1;
            while (flag){
                gap=x;
                time_no_buy=gap/rate;
                time_buy=c/rate+gap/(rate+f);
                //cout<<setprecision(3)<<time_buy<<"*";
                if (time_no_buy>time_buy){
                    time+=c/rate;
                    //cout<<setprecision(7)<<c/rate;
                    rate+=f;
                }
                else{
                    time+=time_no_buy;
                    flag=0;
                }
            }
        }
        fout<<"Case #"<<num<<": ";
        fout<<fixed<<setprecision(7)<<time<<'\n';
        ++num;
    }
    return 0;
}

