#include <iostream>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <list>
#define MOD 1000000007
#define MAXN 25
using namespace std;
int n ,m,t;

void pt(int* ca,int winner){
    if(winner)
        printf("Case #%d: GABRIEL\n",*ca);
    else
        printf("Case #%d: RICHARD\n",*ca);
    (*ca)++;
}
int main (){
    freopen("/Users/Masoud/Desktop/in.txt", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int ca=1;
    scanf("%d",&t);
    while(t--){
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
            pt(&ca, 1);
        else if(x==2)
            pt(&ca, (r*c)&1?0:1);
        else if(x==3)
            pt(&ca, ((r*c)==6||(r*c)==12||(r*c)==9)?1:0);
        else
            pt(&ca,((r*c)==16||(r*c)==12)?1:0);
    }
    
    return 0;
}
