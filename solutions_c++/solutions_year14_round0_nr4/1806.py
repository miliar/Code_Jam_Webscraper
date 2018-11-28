//
//  main.cpp
//  war
//
//  Created by Lydia Yang on 14-4-12.
//  Copyright (c) 2014年 杨荔雅5110309443. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int comp(const void *a, const void *b){
    return *(double *)a > *(double *)b? 1:-1;
}


int main()
{
    ifstream in("/Users/apple/Desktop/in.txt");
    ofstream out("/Users/apple/Desktop/out.txt");
    
    int T = 0;
    in >> T;
    int num = 0;
    double n[2000];
    double k[2000];
    for (int j = 0; j < 2000; j++) {
        n[j] = k[j] = 0;
    }
    int ans1 = 0;
    int ans2 = 0;
    int count1 = 0;
    int count2 = 0;
    
    for (int i = 0; i < T; i++) {
        in >> num;
        for (int j = 0; j < num; j++) {
            in >> n[j];
        }
        for (int j = 0; j < num; j++) {
            in >> k[j];
        }
        
        qsort(n, num, sizeof(double), comp);
        qsort(k, num, sizeof(double), comp);
        
        ans1 = ans2 = 0;
        count1 = 0;
        count2 = 0;
        
        while (count1<num) {
            if (count2<num) {
                if (n[count1] > k[count2]) {
                    ans1++;
                    count1++;
                    count2++;
                }
                else count1++;
            }
            else break;
        }
        
        count1 = 0;
        count2 = 0;
        
        while (count2<num) {
            
            if (count1<num) {
                //cout<<n[count1]<<" "<<k[count2]<<endl;
                if (n[count1] < k[count2]) {
                    ans2++;
                    count1++;
                    count2++;
                }
                else count2++;
            }
            else break;
        }
        ans2 = num-ans2;
        
        out<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2<<endl;
        
    }
    
    in.close();
    out.close();
    return 0;
}

