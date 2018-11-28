#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

double nao[1001], ken[1001];
int n, y, z;

void calcY(){
    int startN = 0, startK = 0;
    y = 0;
    while(1){
        if(startN == n) break;
        if(startK == n) break;
        if(ken[startK] < nao[startN]){
            y++;
            startK++;
            startN++;
        }
        else{
            startN++;
        }
    }
}

void calcZ(){
    int startN = 0, startK = 0;
    z = n;
    while(1){
        if(startN == n) break;
        if(startK == n) break;
        if(ken[startK] > nao[startN]){
            z--;
            startK++;
            startN++;
        }
        else startK++;
    }
}

int main(){

    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        scanf("%d",&n);
        for(int i=0; i<n; i++) scanf("%lf",&nao[i]);
        for(int i=0; i<n; i++) scanf("%lf",&ken[i]);
        sort(nao, nao+n);
        sort(ken, ken+n);
        calcY();
        calcZ();
        printf("Case #%d: %d %d\n",t,y,z);
    }


return 0;
}
