#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

int a[10004],b[10004];

int main(){
    freopen("A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);

    int T;
    scanf(" %d",&T);
    for(int t=0,N,X;t<T && scanf(" %d %d",&N,&X)==2;t++){
        for(int i=0;i<N;i++){
            scanf(" %d",&a[i]);
            b[i] = 0;
        }
        sort(a,a+N);
        int ans = 0;
        for(int i=N-1;i>=0;i--){
            if(b[i]==1) continue;
            int now = a[i];
            b[i] = 1;
            int re = 0;
            for(int j=i-1;j>=0;j--){
                if(now+a[j]<=X && b[j]==0){
                    b[j] = 1;
                    ans++;
                    re = 1;
                    break;
                }
            }
            if(re==0){
                ans++;
            }
        }
        printf("Case #%d: %d\n",t+1,ans);
    }

    return 0;
}
