//
//  main.cpp
//  Revenge of pancakes
//
//  Created by VIVEK GANGWAR on 09/04/16.
//  Copyright © 2016 VIVEK GANGWAR. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <climits>
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

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
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
int count_minus(string s)
{
    int count = 0 ;
    for (int i = 0; i < s.size(); i++) {
        if(s[i] == '-')
            count+=1;
    }
    return count;
}
int last_minus_index(string s)
{
    int index = -1;
    for (int i = 0; i < s.size(); i++) {
        if(s[i] == '-')
            index = i;
    }
    return index;
}
int main()
{
    int test;
    S(test);
    for (int i = 1; i <= test; i++) {
        string s;
        cin >> s;
        //cout << s.size()<<endl;
        int counter = 0;
        bool flag = true;
        while (flag) {
            int last_min = last_minus_index(s);
            if (last_min == -1) {
                cout <<"Case #"<< i <<": "<< counter << endl;
                flag = false;
                break;
            }
            // flipping upto last -
            for (int i = 0; i <= last_min; i++) {
                if(s[i] == '-')
                    s[i] = '+';
                else if(s[i] == '+')
                    s[i] = '-';
            }
            counter += 1;
            int check = count_minus(s);
            if (check == 0) {
                cout <<"Case #"<< i <<": "<< counter << endl;
                flag = false;
            }
        }
    }
}
