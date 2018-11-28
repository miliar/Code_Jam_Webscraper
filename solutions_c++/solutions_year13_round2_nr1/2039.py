#include <iostream>
#include<stdlib.h>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include<limits.h>
#include <string.h>
#define ll long long
using namespace std;
int compare(const void *a,const void *b)    {    return *(int *)a - *(int *)b;  }
  int t,ans,tt,n,i,a,m[100],curr;
int recur(int sz,int minm,int i,int last)
{
    if(i==last) return minm;
    if(m[i]>=sz)
    {
        int curr=sz,add=0;
        while(curr<=m[i])
        {
            curr+=curr-1;
            ++add;
        }
        //printf("minm=%d i=%d sz=%d add=%d\n",minm,i,sz,add);
        minm=min(minm+last-i,recur(curr,minm+add,i,last));
        //printf("minm=%d i=%d sz=%d add=%d\n",minm,i,sz,add);

    }
    else
    {
        minm=recur(sz+m[i],minm,i+1,last);
    }
    return minm;
}
int main() {
    freopen("A-large.in","r",stdin); freopen("outputl.txt","w",stdout);
    scanf("%d",&t);
    tt=t;
    while(t--){
            ans=0;
            scanf("%d %d",&a,&n);
            curr=a;
            for(i=0;i<n;++i){
                    scanf("%d",&m[i]);
            }
            qsort(m,n,sizeof(int),compare);
            /*for(i=0;i<n;++i)
            {
                int local=0;
                if(curr==1)
                {
                    ans=n;
                    break;
                }
                if(m[i]>=curr)
                    {
                        a=curr;
                    while(curr<=m[i]){
                        curr+=curr-1;
                        ++local;
                    }
                    if(local>=n-i-1)
                    {
                        n=n-1;
                        curr=a;
                        ++ans;
                    }
                    else
                    {
                        ans+=local;
                    }
                }
                else{
                    curr+=m[i];
                }
            }*/

        printf("Case #%d: %d\n",tt-t,a>1?recur(a,0,0,n):n);
    }
  return 0;
}

