/*
   Sonakshi Nathani
   IIIT-HYD
information: 
#tags: 
date: Sun Apr 13 04:49:49 IST 2014
 */
#include<bits/stdc++.h>
using namespace std;
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define sii(a,b) scanf("%d %d",&a,&b)
#define si(a) scanf("%d",&a)
#define pii(a,b) printf("%d %d\n",a,b)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,1,sizeof(a))
int main(){
    int n;
    si(n);
    //int a[4][4];
    int a[30];
    int t=0;
    while(n--){
        CLR(a);
        t++;
        int val1,val2;
        si(val1);
        FOR(i,0,4){
            FOR(j,0,4){
                int inp;
                si(inp);

                if(i==val1-1){
                    a[inp]=1;
                }
            }
        }
        int flag=0,result=0;
        si(val2);
        FOR(i,0,4){
            FOR(j,0,4){
                int inp;
                si(inp);

                if(i==val2-1){
                    if(a[inp]==1){
                        flag++;
                        result=inp;
                    }
                    a[inp]=1;
                }
            }
        }
        printf("Case #%d:",t);
        if(flag==0){
            printf(" Volunteer cheated!\n");
        }
        else if(flag==1){
            printf(" %d\n",result);
        }
        else{
            printf(" Bad magician!\n");
        }

    }
    return 0;
}

