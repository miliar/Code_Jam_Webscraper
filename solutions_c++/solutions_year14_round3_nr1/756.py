//
//  main.cpp
//  Problem A
//
//  Created by Umair Akhtar on 11/05/2014.
//  Copyright (c) 2014 Umair Ahmad. All rights reserved.
//

#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>

#define ForA(i, a, b) for(i =(a); i <=(b); ++i)
#define ForD(i, a, b) for(i = (a); i >= (b); --i)
#define For(i, b) for(i=0; i<(b); ++i)
#define pb push_back
#define peeks top()
#define peekq front()
#define peek(v) v[0]
#define last(v) v[v.size()-1]
#define SQR(a) ((a)*(a))
#define ulld unsigned long long int
#define lld long long int

using namespace std;

int main(){
    ifstream fin("Data.in");
    ofstream fout("Data.out");
    
    
    int tt;
    fin>>tt;
    int cc = 0;
    while(tt--) {
        cc++;
        fout<<"Case #"<<cc<<": ";
        long double a, b;
        char g;
        fin>>a>>g>>b;
        long double ans = a/b;
        int count = 0;
        bool t = false;
        int first = 0;
        while(count <= 40) {
            
            if(ans == 1) break;
            if(ans > 1) {
                ans = ans - 1;
                if(!t){ first = count; t = true; }
            }
            ans *= 2;
            count++;
        }
        if(!t) first = count;
        if(count <= 40) fout<<first<<endl;
        else fout<<"impossible"<<endl;
    }
    fin.close();
    fout.close();
    
    return 0;
}

