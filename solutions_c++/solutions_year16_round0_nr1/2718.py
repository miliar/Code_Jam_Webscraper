//
//  main.cpp
//  Qualification Round Africa 2010
//
//  Created by 林昱呈 on 2016/2/21.
//  Copyright (c) 2016年 林昱呈. All rights reserved.
//

/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*******  All Required define Pre-Processors and typedef Constants *******/
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define read(type) readInt<type>()
const double pi=acos(-1.0);
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

/****** Template of some basic operations *****/
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }
/**********************************************/

/****** Template of Fast I/O Methods *********/
template <typename T> inline void write(T x)
{
    int i = 20;
    char buf[21];
    // buf[10] = 0;
    buf[20] = '\n';
    
    do
    {
        buf[--i] = x % 10 + '0';
        x/= 10;
    }while(x);
    do
    {
        putchar(buf[i]);
    } while (buf[i++] != '\n');
}

template <typename T> inline T readInt()
{
    T n=0,s=1;
    char p=getchar();
    if(p=='-')
        s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
        p=getchar();
    if(p=='-')
        s=-1,p=getchar();
    while(p>='0'&&p<='9') {
        n = (n<< 3) + (n<< 1) + (p - '0');
        p=getchar();
    }
    
    return n*s;
}
/************************************/


/******** User-defined Function *******/

// write here your code
int count(int n){
    bool test[10] = {false};
    bool res = false;
    int t=1;
    while(res == false){
        int n2=n*t;
        int residul=n2%10;
        while(n2!=0){
            test[residul] = true;
            //printf("loop%d: %d %d\n",t,n2,residul);
            n2/=10;
            residul=n2%10;
        }
        /*
        res = true;
        REP(i,10){
            res &= test[i];            
        }
        */
        res = test[0] && test[1] && test[2] && test[3] && test[4] && test[5] && test[6] && test[7] && test[8] && test[9];        
        //printf("loop%d: %d\n",t,res);
        t++;
    }
    return n*(t-1);
}

/**************************************/

/********** Main()  function *******/
int main(int argc, const char * argv[]) {
    if (argc == 2 && strcmp(argv[1], "small") == 0) {
        freopen("small.in","r",stdin);
        freopen("small.out","w",stdout);
    }
    else if (argc == 2 && strcmp(argv[1], "large") == 0) {
        freopen("large.in","r",stdin);
        freopen("large.out","w",stdout);
    }
    else{
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    
    int t;
    SCD(t);
    //printf("loop: %d\n", t);
    
    REP(k,t){
        // write here your code
        int n;        

        SCD(n);
        if(n==0)    printf("Case #%d: %s\n",k+1,"INSOMNIA");
        else{
            int ans=count(n);
            printf("Case #%d: %d\n",k+1,ans);
        }        
/*
        REP(i,n){
            //printf("%d:",k+1);
            cout << mush[i] << '\t';
        }
        cout << endl;
*/
    }
    return 0;
}
