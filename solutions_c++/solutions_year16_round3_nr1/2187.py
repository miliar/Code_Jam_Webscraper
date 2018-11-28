//
//  main.cpp
//  ps2016
//
//  Created by 강태진 on 2016. 5. 7..
//  Copyright © 2016년 강태진. All rights reserved.
//

#include <iostream>
#include <vector>
#include <deque>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <queue>

using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d",&t);
    for(int i =1; i <=t ; i++)
    {
        printf("Case #%d: ",i);
        int n;
        scanf("%d",&n);
        priority_queue<pair<int,char>, vector<pair<int, char> > > pq;
        
        for(int i = 0; i < n ; i++){
            int t;
            scanf("%d",&t);
            pq.push(make_pair(t, 'A'+i));
        }
        
        while(!pq.empty())
        {
            pair<int, char> t1, t2;
            t1 = pq.top();
            pq.pop();
            
            if(!pq.empty())
            {
                t2 = pq.top();
                pq.pop();
                
                
                if(t1.first == t2.first && t1.first == 1 && pq.size() == 1)
                {
                    printf("%c ",t1.second);
                    t1.first--;
                    if(t1.first > 0)
                    {
                        pq.push(t1);
                    }
                    pq.push(t2);
                }
                else
                {
                    printf("%c%c ",t1.second, t2.second);
                    t1.first--;
                    t2.first--;
                    if(t1.first > 0)
                    {
                        pq.push(t1);
                    }
                    if(t2.first > 0)
                    {
                        pq.push(t2);
                    }

                }
            }
            else
            {
                printf("%c ",t1.second);
                t1.first--;
                if(t1.first > 0)
                {
                    pq.push(t1);
                }
            }
        }
        printf("\n");
    }
    return 0;
}

/*
 *
 *
 *
 *
 */