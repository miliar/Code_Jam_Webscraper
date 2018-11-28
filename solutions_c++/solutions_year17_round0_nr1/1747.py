//
//  main.cpp
//  A-Oversized-Pancake-Flipper
//
//  Created by Volodymyr Polosukhin on 08/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//

#include <cstdio>
#include <set>
#include <queue>

using namespace std;

int encode(char s[])
{
    int result = 0;
    
    for (char *pointer = s; *pointer; ++pointer)
    {
        result = (result << 1) + (*pointer == '-');
    }
    
    return result;
}

int solveSmall(char s[], int k)
{
    const int flipper = (1<<k) - 1;
    
    set < int > used;
    queue < pair < int, int > > q;
    
    int intial = encode(s);
    used.insert(intial);
    q.emplace(intial, 0);
    
    while (!q.empty())
    {
        int current = q.front().first;
        int flips = q.front().second;
        q.pop();
        
        if (!current)
        {
            return flips;
        }
        
        for (int offset = 0; s[offset + k - 1]; ++offset)
        {
            int next = current ^ (flipper << offset);
            
            if (!used.count(next))
            {
                used.insert(next);
                q.emplace(next, flips+1);
            }
        }
    }
    
    return -1;
}

int solveLarge(char s[], int k)
{
    int answer = 0;
    int i;
    
    for (i = 0; s[i + k - 1]; ++i)
    {
        if ('-' == s[i])
        {
            for (int j = 0; j < k; ++j)
            {
                s[i + j] = '-' == s[i + j] ? '+' : '-';
            }
            
            ++answer;
        }
    }
    
    for (; s[i]; ++i)
    {
        if ('-' == s[i])
        {
            return -1;
        }
    }
    
    return answer;
}

int main(int argc, const char * argv[]) {
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int t;
    
    scanf("%d", &t);
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        static char s[1001];
        int k;
        
        scanf("%s%d", s, &k);
        
        int flips = solveLarge(s, k);
        
        printf("Case #%d: ", testcase);
        
        if (-1 == flips)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", flips);
        }
    }
    
    return 0;
}
