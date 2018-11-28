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
#define N 10101
using namespace std;

int t,n,x,tab[N],l,p,k;

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++) scanf("%d",&tab[i]);
        sort(tab,tab+n);
        p=0;k=n-1;l=0;
        while(p<k){
            while(k>p && tab[p]+tab[k]>x){
                k--;
                l++;
            }
            l++;
            p++;
            k--;
        }
        if(p==k) l++;
        printf("Case #%d: %d\n",ttt,l);
    }
    
}

