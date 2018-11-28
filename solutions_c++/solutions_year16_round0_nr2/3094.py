#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h> 
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

const int N=1e6+100;

char s[1234];
int main () {
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        scanf("%s",s+1);
        int n=strlen(s+1);
        int cnt=0;
        for (int i=2;i<=n;i++) {
            if (s[i]!=s[i-1]) cnt++;
        }
        if (s[n]=='-') cnt++;
        printf("Case #%d: %d\n",cas,cnt);
    }
    return 0;
}
