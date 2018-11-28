#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <fstream>
#include <set>
#include <map>
#include <cmath>
#pragma comment(linker,"/STACK:116777216")
#define MAXN 100100

using namespace std;

int t,n,a[MAXN],x,cnt;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>t;
    for(int o=1;o<=t;o++){
        cnt=0;
        scanf("%d%d",&n,&x);
        for(int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        sort(a+1,a+1+n);

        int ptr=1;

        for(int i=n;i>=ptr;i--){
            if(i!=ptr){
            if(a[i]+a[ptr]<=x)
                ptr++,cnt++;
            else
                cnt++;}
            else
                cnt++;

        }
        printf("Case #%d: %d\n",o,cnt);

    }









    return 0;
}
