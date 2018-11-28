//Bismillahir Rahmanir Rahmeem

#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<math.h>
#include<string.h>
#include <stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string>
#include<set>
#include<iomanip>
#define INF 1e9
#define lld long long int
#define CLR(a) memset(a,0,sizeof(a))
#define RESET(a) memset(a,-1,sizeof(a))
#define act(a) memset(a,1,sizeof(a))
#define setinf(a) memset(a,0b01111111,sizeof(a));
#define FRO freopen("input.txt","r",stdin);
#define FROut freopen("output.txt","w",stdout);
#define ui unsigned int
#define came "came"
#define pii pair<int,int>
#define plii pair<long long int, int>
#define pll pair<long long,long long>
#define pic pair<int,char>
#define ninf (-1e9)-2
#define inf (1e9)+2
#include<fstream>
#include <assert.h>
#include <bitset>

#define foreach(x) for(__typeof(x.begin()) it=x.begin(); it!=x.end();it++)

using namespace std;
#define pid pair<int,double>
#define pdi pair<double,int>

#define PB push_back
#define MP make_pair
#define pri(x) printf("%d\n",x)
#define pi 3.14159265359
#define F first
#define S second
#define vit vector<int>::iterator
//copy A to X
#define CPY(A,X) memcpy(X,A,sizeof(A))

int a[1005];

char ln[1005];

int main()
{
    FRO
    FROut
    int t,ca;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",ca);
        if(r<c)
        {
            swap(r,c);
        }
        if(r<x)
        {
            printf("RICHARD\n");
        }
        else
        {
            if(x==1)
            {
                printf("GABRIEL\n");
            }
            else if(x==2)
            {
                if(r%2==0 || c%2==0)
                {
                    printf("GABRIEL\n");
                }
                else
                {
                    printf("RICHARD\n");
                }
            }
            else if(c==1)
            {
                printf("RICHARD\n");
            }
            else if(x==3)
            {
                if(r%3==0 || c%3==0)
                {
                    printf("GABRIEL\n");
                }
                else
                {
                    printf("RICHARD\n");
                }
            }
            else
            {
                if(c<=2)
                {
                    printf("RICHARD\n");
                }
                else
                {
                    printf("GABRIEL\n");
                }
            }
        }
    }
    return 0;
}

