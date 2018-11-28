//
//  main.cpp
//  GoogleCode Jam#1
//
//  Created by Puneet Rawat on 09/04/16.
//  Copyright © 2016 Puneet Rawat. All rights reserved.
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

/**************************************/

/********** Main()  function *******/
int main()
{
    int p1=0,p2=0;
#ifndef GOOGLE_CODE_JAM
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int t,t1,n=1,backup,latest,n1;
    bool zero,one,two,three,four,five,six,seven,eight,nine;
    t=read(int);
    REP(k,t){
        n1=1;
        n=1;
        t1 = read(int);
        backup=t1;
        latest=t1;
        zero=one=two=three=four=five=six=seven=eight=nine=false;
        if(t1==0){
            printf("Case #%d: INSOMNIA\n",k+1);
        }
        else{
            /*while(t1%(10^n)!=t1){
                n++;
            }*/
            while(zero==false||one==false||two==false||three==false||four==false||five==false||six==false||seven==false||eight==false||nine==false){
                n1++;
                while(t1!=0){
                if(t1%(10)==0)
                {
                    zero=true;
                }
                else if(t1%(10)==1)
                {
                    one=true;
                }
                else if(t1%(10)==2)
                {
                    two=true;
                }
                else if(t1%(10)==3)
                {
                    three=true;
                }
                else if(t1%(10)==4)
                {
                    four=true;
                }
                else if(t1%(10)==5)
                {
                    five=true;
                }
                else if(t1%(10)==6)
                {
                    six=true;
                }
                else if(t1%(10)==7)
                {
                    seven=true;
                }
                else if(t1%(10)==8)
                {
                    eight=true;
                }
                else if(t1%(10)==9)
                {
                    nine=true;
                }
                    t1=t1/10;
                }
                latest=n1*backup;
                t1=latest;
                
            }
            latest=(n1-1)*backup;
          printf("Case #%d: %d\n",k+1,latest);
        }

    }
    return 0;
}
/********  Main() Ends Here *************/