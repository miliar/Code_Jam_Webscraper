//
//  main.cpp
//  codejamRound1a
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
int main()
{
    LL test;
    Sl(test);
    for(int i = 1;i <= test;i++)
    {
        string a;
        cin >> a;
        string output[1005];
        output[1] = a[0];
        for(int j = 1 ;j < a.size(); ++j){
            string first = output[j];
            string previous = first;
            previous =a[j] + output[j];
            first = output[j] + a[j];
            output[j+1] = max(first,previous);
        }
        cout << "Case #" << i << ": " << output[(int)a.size()] << endl;
    }
}