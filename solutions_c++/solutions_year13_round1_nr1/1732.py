//
//  main.cpp
//  round 1A1
//
//  Created by Zulkarnine Mahmud on 4/27/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <sstream>

int T;
int cas;
long long r ,t;

using namespace std;


void printResult();
void solveCase(){
    long long count=0;
    while (t>=0) {
        t-=(2*r+1);
        count++;
        r+=2;
        
    }
    cout<<count-1;
};

int main(){
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    
    
    cin>>T;
    for (int cas=1; cas<=T; cas++) {
        cin>>r;
        cin>>t;
        
        cout<<"Case #"<<cas<<": ";
        solveCase();
        cout<<endl;
        
            }
    fclose(stdin);
    fclose(stdout);
    return 0;
    
}

