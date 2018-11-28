//
//  main.cpp
//  Rank and file
//
//  Created by VIVEK GANGWAR on 16/04/16.
//  Copyright © 2016 VIVEK GANGWAR. All rights reserved.
//
#include <iostream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <assert.h>
#include <deque>
#include <ctime>

#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;
int main(int argc, const char * argv[])
{
        int test,n,var,end1;
        S(test);
        for (int t = 1; t <= test; t++)
        {
            int arr[2600];
            CLR(arr);
            S(n);
            end1 = n;
            n = ((n*2) - 1);
            for(int i = 1; i <= n; i++)
            {
                for(int j = 0; j < end1; j++)
                {
                    S(var);    arr[var]++;
                }
                
            }
            cout<< "Case #" << t << ":";
            for(int output = 1; output < 2501; output++)
            {
                if(arr[output]%2!=0)
                    cout << " " << output;
            }
            cout<<"\n";
            
        }
    return 0;
}
