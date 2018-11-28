//
//  main.cpp
//  beautyofcode
//
//  Created by 甄晓磊 on 14-4-11.
//  Copyright (c) 2014年 甄晓磊. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, const char * argv[])
{
    // insert code here..
    FILE *fp;
    fp = freopen("data.txt", "r", stdin);
    FILE *fp1;
    fp1 = freopen("out.txt", "w", stdout);
    int T;
    int a[5][5];
    cin>>T;
    for(int i=1;i<=T;i++){
        int s;
        cin>>s;
        for (int j=1; j<=4; j++) {
            for (int k=1; k<=4; k++) {
                cin>>a[j][k];
            }
        }
        unsigned int x=0;
        for (int j=1; j<=4; j++) {
            x|= 1<<a[s][j];
        }
        cin>>s;
        for (int j=1; j<=4; j++) {
            for (int k=1; k<=4; k++) {
                cin>>a[j][k];
            }
        }
        unsigned int y=0;
        for (int j=1; j<=4; j++) {
            y|= 1<<a[s][j];
        }
        x&=y;
        if (x==0) {
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        }
        else if((x&(x-1))==0){
            x=log(x)/log(2);
            cout<<"Case #"<<i<<": "<<x<<endl;
        }
        else{
            cout<<"Case #"<<i<<": Bad magician!"<<endl;
        }
    }
    return 0;
}



