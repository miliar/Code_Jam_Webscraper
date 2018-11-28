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


int t,n,a,tab[4],ile,wyn;

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        scanf("%d",&n);
        for(int i=1;i<=4;i++){
            if(i==n) for(int j=0;j<4;j++) scanf("%d",&tab[j]);
            else for(int j=0;j<4;j++) scanf("%d",&a);
        }
        ile=0;
        scanf("%d",&n);
        for(int i=1;i<=4;i++){
            if(i==n) for(int j=0;j<4;j++){
                scanf("%d",&a);
                for(int k=0;k<4;k++){
                    if(tab[k]==a){
                        wyn=a;
                        ile++;
                    }
                }
            }
            else for(int j=0;j<4;j++) scanf("%d",&a);
        }
        if(ile==1) printf("Case #%d: %d\n",ttt,wyn);
        if(ile==0) printf("Case #%d: Volunteer cheated!\n",ttt);
        if(ile>1) printf("Case #%d: Bad magician!\n",ttt);
    }
}

