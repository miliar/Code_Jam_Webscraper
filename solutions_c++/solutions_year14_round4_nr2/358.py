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

int a[1004];

int main(){
    freopen("B-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    scanf(" %d",&T);
    for(int t=0,N;t<T && scanf(" %d",&N)==1;t++){
        for(int i=0;i<N;i++)
            scanf(" %d",&a[i]);
        int ans = 0,l=0,r=N-1;
        for(int tt=0;tt<N;tt++){
            int pos,MIN = 1000000009;
            for(int i=l;i<=r;i++)
                if(a[i]<MIN){
                    MIN = a[i];
                    pos = i;
                }
            int left = pos-l, right = r-pos;
            if(left<right){
                ans += left;
                if(pos!=l){
                    for(int j=pos;j>l;j--){
                        swap(a[j],a[j-1]);
                    }
                }
                l++;
            }else{
                ans += right;
                if(pos!=r){
                    for(int j=pos;j<r;j++){
                        swap(a[j],a[j+1]);
                    }
                }
                r--;
            }
        }
        printf("Case #%d: %d\n",t+1,ans);
    }

    return 0;
}
