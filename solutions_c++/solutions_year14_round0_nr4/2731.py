//
//  main.cpp
//  testalgo
//
//  Created by William Hutama on 12/4/14.
//  Copyright (c) 2014 William Hutama. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <deque>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
        deque<double> blocks[2]; // 0 = naomi, 1 = ken.
        
        int a = 0, b = 0;
        int m;
        scanf("%d", &m);
    
        for (int k = 0; k < 2; ++k) {
            for (int j = 0; j < m; ++j) {
                double v;
                scanf("%lf", &v);
                blocks[k].push_back(v);
            }
        }
        sort(blocks[0].begin(), blocks[0].end());
        sort(blocks[1].begin(), blocks[1].end());
        
        deque<double> nao = blocks[0];
        deque<double> ken = blocks[1];
        
        {
            // naomi plays War optimally.
            deque<double>::iterator r = nao.begin();
            for ( ; r != nao.end(); ++r) {
                deque<double>::iterator p = lower_bound(ken.begin(), ken.end(), *r);
                
                double kw = 0;
                
                if (p == ken.end())
                {
                    // throw away smallest element
                    kw = ken.front();
                    ken.pop_front();
                }
                else
                {
                    kw = *p;
                    ken.erase(p);
                }
                
                if (kw < *r)
                {
                    b++;
                }
            }
        }
        {
            nao = blocks[0];
            ken = blocks[1];
            // naomi plays Deceitful War optimally.
            deque<double>::iterator r = ken.begin();
            for ( ; r != ken.end(); ++r)
            {
                deque<double>::iterator p = lower_bound(nao.begin(), nao.end(), *r);

                double kw = *r;
                double nw = 0;
                
                if (p == nao.end())
                {
                    // throw away smallest element
                    nw = nao.front();
                    nao.pop_front();
                }
                else
                {
                    nw = *p;
                    nao.erase(p);
                }

                if (kw < nw)
                {
                    a++;
                }
            }
        }
        
        printf("Case #%d: %d %d\n", i, a, b);
    }
    
    return 0;
}

