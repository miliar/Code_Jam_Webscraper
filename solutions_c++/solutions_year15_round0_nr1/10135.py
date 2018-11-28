/* 
 * File:   GCJ2015_QR_PA_StandingOvation.cpp
 * Author: JuanM
 *
 * Created on April 10, 2015, 11:27 PM
 */


#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cfloat>
#define smx 1010
using namespace std;

char pers[smx];
int main() {
    
    FILE *pW;
    FILE *pR;
    pR=fopen("QR1A.in","r");
    pW=fopen("QR1Aout.txt","w");
    
    int t,n,ct,pTot;
    fscanf(pR,"%d",&t);
    
    for(int cse=1;cse<=t;cse++){
        fscanf(pR,"%d",&n);
        fscanf(pR,"%s",pers);
        pTot=0;ct=0;
        for(int i=0;i<=n;i++){
            if(pTot<i && (pers[i]-'0')!=0){
                ct+=(i-pTot);
                pTot+=ct;
            }
            pTot+=(pers[i]-'0');
        }
        fprintf(pW,"Case #%d: %d\n",cse,ct);
    }
    return 0;
}

