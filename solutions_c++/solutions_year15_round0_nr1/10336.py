/*
Rudradeep Mukherjee aka Aragorn aka Chandrian
*/
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;

int main()
{
int c,i,j,n,t,ans,K=1;
char ch,a[1001];
int Max;
//freopen("A-small-attempt0.in","r",stdin);
//freopen("A.out","w",stdout);
scanf("%d",&t);
while(t--) {
    scanf("%d%s",&n,a);
    c=a[0]-'0';ans=0;
    for(i=1;i<=n;i++) {
        if(c<i) ans+=i-c,c=i;
        c+=a[i]-'0';
    }
    printf("Case #%d: %d\n",K++,ans);
}
return 0;
}
