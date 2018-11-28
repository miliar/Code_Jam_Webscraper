//
//  main.m
//  lalala
//
//  Created by Henry_at_IBM on 1/29/15.
//  Copyright (c) 2015 Henry_at_IBM. All rights reserved.
//

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

void solve()
{
    int level;
    cin>>level;
    
    vector<char> v(level+1);
    
    for(int i = 0; i <= level ; i++) {
        cin>>v[i];
        
        
    }
    
    int sum = 0;
    int need = 0;
    int need_s = 0;
    
    for(int i = 0; i <= level ; i++) {
        //cout<<v[i];
        if(sum >= i) {
            
        } else {
            need = (i - sum);
        }
        
        sum += (v[i] - '0' + need) ;
        
        need_s += need;
        
        need = 0;
    }
    

    
    
    
    
    cout<<need_s<<endl;
    
    v.clear();
}

int MAIN()
{

    int TestCase;
    cin>>TestCase;
    for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
    {
        cout << "Case #" << CaseID << ": ";
        solve();
    }
    return 0;
}

int main(int argc, const char * argv[]) {

        //srand((unsigned)time(NULL));
//#ifdef LOCAL_TEST
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
//#endif
        ios :: sync_with_stdio(false);
        cout << fixed << setprecision(16);
        return MAIN();
    
}
