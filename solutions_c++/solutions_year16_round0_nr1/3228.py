//
//  main.cpp
//  Counting Sheep
//
//  Created by Nabil SHF on 4/9/16.
//  Copyright © 2016 Nabil SHF. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int main(){
    int t, n;
    scanf ("%d",&t);
    for (int l=1;l<=t;++l){
        scanf ("%d",&n);
        printf ("Case #%d: ",l);
        if (n==0){
            printf ("INSOMNIA\n");
        }
        else{
            int Arr[10];
            memset(Arr, 0, sizeof(Arr));
            
            int sum = 0;
            int cnt = 2;
            int a = n, cpt;
            while (true){
                if (sum == 10) break;
                int nn = n;
                while (nn){
                    int r = nn%10;
                    if(Arr[r] == 0){
                        sum++;
                        Arr[r] = 1;
                    }
                    if (sum == 10) cpt = n;
                    nn /= 10;
                }
                n = cnt*a;
                cnt++;
            }
            cout<<cpt<<endl;
        }
    }
    
    return 0;
}