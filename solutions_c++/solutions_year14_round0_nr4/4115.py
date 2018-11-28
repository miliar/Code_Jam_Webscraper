#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
using namespace std;

int n,m,t,j,wyn1,wyn2;
double tab1[10000],tab2[10000];

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%lf",&tab1[i]);
        for(int i=0;i<n;i++) scanf("%lf",&tab2[i]);
        sort(tab1,tab1+n);
        sort(tab2,tab2+n);
        j=0;
        for(int i=0;i<n && j<n;i++){
            while(j<n && tab2[j]<tab1[i]) j++;
            if(j==n){
                wyn1=n-i;
                break;
            }
            if(j==n-1){
                wyn1=n-i-1;
                break;
            }
            j++;
        }
        j=0;
        j=0;
        for(int i=0;i<n && j<n;i++){
            while(j<n && tab1[j]<tab2[i]) j++;
            if(j==n){
                wyn2=i;
                break;
            }
            if(j==n-1){
                wyn2=i+1;
                break;
            }
            j++;
        }
        printf("Case #%d: %d %d\n",ttt,wyn2,wyn1);
    }
}

