/* 
 * File:   GCJ2013_1B_PA.cpp
 * Author: JuanM
 *
 * Created on 4 de mayo de 2013, 10:56
 */

#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <stdio.h>
#include <algorithm>
using namespace std;
long int motes[110];
long int a;
void print(int d,int n){
    for(int i=d;i<n;i++){
        printf("%ld ",motes[i]);
    }printf("       %ld\n",a);
}

int main() {
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    int t,n,c,d,m,M;
    long int r;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%ld %d",&a,&n);
        for(int j=0;j<n;j++){
            scanf("%ld",&motes[j]);
        }
        sort(motes,motes+n);
        c=0;d=0;M=n;m=0;
        while(c<n&&d<n){
            if(a>motes[d]){
                a+=motes[d];
                d++;
                m=c+n-d;
                if(m<M)M=m;
            }else{
                a=2*a-1;
                c++;
            }
            //printf("%ld ",a);
            //print(d,n);
        }
        printf("Case #%d: %ld\n",i,c>M?M:c);
    }
    return 0;
}

