//
//  main.cpp
//  q2
//
//  Created by zhou on 13-4-12.
//  Copyright (c) 2013年 zhou. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream in("in.txt");
ofstream ou("out.txt");
int solve(){
    int m,n;
    in>>m>>n;
    int a[100][100];
    int f[100][100]={};
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            in>>a[i][j];
    for(int i=0;i<m;i++){
        int mx=0;
        for (int j=0;j<n;j++) {
            if(a[i][j]>mx)mx=a[i][j];
        }
        for(int j=0;j<n;j++){
            if(a[i][j]==mx)f[i][j]=1;
        }
        
    }
    for(int j=0;j<n;j++){
        int mx=0;
        for (int i=0;i<m;i++) {
            if(a[i][j]>mx)mx=a[i][j];
        }
        for(int i=0;i<m;i++){
            if(a[i][j]==mx)f[i][j]=1;
        }
        
    }
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            if(!f[i][j]) return 0;
    return 1;
    
}
int main(int argc, const char * argv[])
{

    // insert code here...
    int tc;
    in>>tc;
    for (int t=0; t<tc; t++) {
       ou<<"Case #"<<t+1<<": ";
        if (solve()) 
            ou<<"YES\n";
        else
            ou<<"NO\n";
    }
    return 0;
}

