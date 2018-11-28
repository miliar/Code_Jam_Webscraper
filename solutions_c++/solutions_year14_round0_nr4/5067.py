/* 
 * File:   GCJ2014_QR_PD_DeceitfulWar.cpp
 * Author: JuanM
 *
 * Created on April 12, 2014, 3:22 PM
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cfloat>
#define maxN 1003
using namespace std;
FILE *pFile;
int t,n,cN=1,NN,KK;
double nN[maxN],nK[maxN],ncN[maxN],ncK[maxN];

int winNdw(){
    int ct=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(ncN[i]>ncK[j]){
                ct++;
                ncK[j]=DBL_MAX;
                break;
            }
        }
    }
    return ct;
}

int winKw(){
    int ct=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(ncK[i]>ncN[j]){
                ct++;
                ncN[j]=DBL_MAX;
                break;
            }
        }
    }
    return ct;
}

void printt(double *aa, int a){
    for(int i=0;i<a;i++){
        printf("%.3lf ",aa[i]);
    }printf("\n");
}

int main() {
    pFile=fopen("PD_DW.txt","w");
    scanf("%d",&t);
    
    while(t--){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
           scanf("%lf",&nN[i]); 
        }
        for(int i=0;i<n;i++){
           scanf("%lf",&nK[i]); 
        }
        sort(nN,nN+n);
        sort(nK,nK+n);
        
        memcpy(ncN,nN,n*sizeof(double));
        memcpy(ncK,nK,n*sizeof(double));
        NN=winNdw();
        
        memcpy(ncN,nN,n*sizeof(double));
        memcpy(ncK,nK,n*sizeof(double));
        KK=winKw();
        
        fprintf(pFile,"Case #%d: %d %d\n",cN++,NN,n-KK);
        
        
    }
    
    return 0;
}

