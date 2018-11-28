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

int t;
double tab1[10000],tab2[10000],wyn,c,f,x;

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        scanf("%lf%lf%lf",&c,&f,&x);
        wyn=x/2;
        for(int i=1;;i++){
            if(wyn-x/(2+(i-1)*f)+x/(2+i*f)+c/(2+(i-1)*f)<wyn) wyn=wyn-x/(2+(i-1)*f)+x/(2+i*f)+c/(2+(i-1)*f);
            else break;
        }
        printf("Case #%d: %lf\n",ttt,wyn);
    }
}

