//
//  main.cpp
//  GoogleCodeJam2015
//
//  Created by chenren02 on 4/12/15.
//  Copyright (c) 2015 chenrren. All rights reserved.
//

#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
//#include <fstream>
//freopen("az_in.txt","r",stdin);
//freopen("out.txt","w",stdout);

using namespace std;

int main(int argc, const char * argv[]) {
    FILE *f1 = freopen("/Users/chenren02/WorkSpace/GoogleCodeJam2015/GoogleCodeJam2015/A-large.in","r",stdin);
    FILE *f2 = freopen("/Users/chenren02/WorkSpace/GoogleCodeJam2015/GoogleCodeJam2015/out.txt","w",stdout);
    int t;
    int num;
    string str;
    cin >> t;
    
    for (int tcase = 1; tcase <= t; ++tcase) {
        cin >> num;
        cin >> str;
        int sum = 0;
        int value = 0;
        
        for (int i = 0; i <= num; ++i) {
            if (sum < i) {
                value += (i - sum);
                sum = i;
            }
            
            sum += (str[i] - '0');
        }
        
        printf("Case #%d: ", tcase);
        cout << value <<endl;
        
    }
    
    return 0;
}
