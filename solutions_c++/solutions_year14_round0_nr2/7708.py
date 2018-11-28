// profile : sunnyLA4
 
// fundamentals headers
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
 
 
using namespace std;
 
#define SIZE 4000000
 
 
#define FOR(i,a,b)                  for(int i=a;i<b;i++)
#define REP(i,n)                    FOR(i,0,n)
#define s(n)                        scanf("%d",&n)
#define su(n)                       scanf("%u",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
 
typedef long long LL;
typedef unsigned int uI;
typedef unsigned long long uLL;

 
int main()
{
 
    freopen("B-large.in","r",stdin);
    freopen("out.in","w",stdout);
    int tc,p=0;
    s(tc);
    double C,F,X,prodC,TimeX,TimeC,ttime;
    
    while(tc--){
        sf(C);sf(F);sf(X);
        //printf("%f %f %f\n", C, F,X); *1.00000
        p++;
        printf("Case #%d: ",p);
        prodC = 2.0;

        TimeX = X/2;
        double temp = X/(2+F);
        TimeC = (C/2) + temp;

        if (TimeX <= TimeC)
        {
            printf("%.7lf\n",TimeX);
        }
        else
        {
            ttime = TimeC - temp;
            //printf("%.7f+\n", ttime);
            while(TimeX > TimeC){

                prodC = prodC + F;

                TimeX = (X/prodC) + ttime;
                double tempC = prodC+F;
                TimeC = (C/prodC) + (X/tempC) + ttime;

                if (TimeX > TimeC)
                {
                    ttime = (C/prodC) + ttime;
                    //printf("%.7f+\n",ttime);
                }
                else
                {
                    ttime = TimeX;
                    //printf("%.7f ->",X / prodC*1.);
                    //printf("%.7f.\n",ttime);
                }
            }
            printf("%.7lf\n",ttime);
        }
        
    }    

    return 0;
}
 