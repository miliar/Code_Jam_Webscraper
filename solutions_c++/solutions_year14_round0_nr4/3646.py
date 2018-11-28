//
//  main.cpp
//  Verizon
//
//  Created by bcstyle on 14-2-26.
//  Copyright (c) 2014年 bcstyle. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <iomanip>      // std::setprecision
#include <algorithm>
using namespace std;

int main()
{
    int numCases, n;
    double naomi[1001], ken[1001];
    bool ken_used[1001];
    int naomiscore, kenscore;
    int naominewscore, kennewscore;
    scanf("%d\n", &numCases);
    for(int curCase = 1; curCase <= numCases; curCase++) {
        cin >> n;
        memset(ken_used, 0, sizeof(ken_used));
        naomiscore = kenscore = naominewscore = kennewscore =  0;
        for(int i = 0; i < n; i++) {
            cin>>naomi[i];
        }
        for(int i = 0; i < n; i++) {
            cin>>ken[i];
        }
        sort(ken, ken+n);
        for(int i = 0; i < n; i++) {
            double curNaomi = naomi[i];
            double *p = lower_bound(ken, ken+n, curNaomi);
            while(p != ken+n) {
                if(ken_used[p-ken]) p++;
                else break;
            }
            if(p!=ken+n)
            {
                kenscore ++;
                ken_used[p-ken] = 1;
            }
            else {
                naomiscore ++;
                int ken_head = 0;
                while(ken_used[ken_head]) ken_head ++;
                ken_used[ken_head] = 1;
            }
            
        }
        memset(ken_used, 0, sizeof(ken_used));
        sort(naomi, naomi+n);
        int ken_head_ind = 0;
        int ken_tail_ind = n-1;
        for(int i = 0; i < n; i++) {
            double curNaomi = naomi[i];
            if(curNaomi < ken[ken_head_ind]) {
                ken_tail_ind--;
            }
            else {
                ken_head_ind++;
                naominewscore++;
            }
            
        }
        cout << "Case #" << curCase << ": " << naominewscore << ' ' << naomiscore << endl;
    }
}

