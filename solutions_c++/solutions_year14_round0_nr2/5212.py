/* 
 * File:   GCJ2014_QR_PB_CookieClickerAlpha.cpp
 * Author: JuanM
 *
 * Created on April 12, 2014, 11:48 AM
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define maxN 100003

using namespace std;

double times[maxN],arr[maxN],sArr[maxN];
int t,cN=1;
double f0,c,f,x,ft,rst;

void printt(int a,double *aaa){
    for(int i=0;i<a;i++){
        printf("s %lf ",aaa[i]);
    }printf("\n\n");
}

int main() {
    
    FILE *pFile;
    pFile=fopen("PB_CCA.txt","w");
    
    scanf("%d",&t);
    
    while(t--){
        scanf("%lf %lf %lf",&c,&f,&x);
        memset(arr,0,sizeof(times));
        memset(sArr,0,sizeof(times));
        memset(times,0,sizeof(times));
        //printt(10);
        f0=2;
        ft=f0;
        arr[0]=c/ft;
        for(int i=1;i<maxN;i++){
            ft+=f;
            arr[i]=c/ft;
        }
        sArr[0]=arr[0];
        for(int i=1;i<maxN;i++){
            sArr[i]=sArr[i-1]+arr[i];
        }
        times[0]=x/2.;
        rst=0.;
        for(int i=1;;i++){
            times[i]=sArr[i-1]+x*arr[i]/c;
            if(times[i]>times[i-1]){
                rst=times[i-1];
                break;
            }
        }
        /*
        printf("\n\narr\n");
        printt(10,arr);
        printf("\nsARr\n");
        printt(10,sArr);
        printf("\ntimes\n");
        printt(10,times);
        */
        fprintf(pFile,"Case #%d: %.7lf\n",cN++,rst);
        //printf("Case #%d: %.7lf\n",cN++,rst);
    }
    
    return 0;
}

