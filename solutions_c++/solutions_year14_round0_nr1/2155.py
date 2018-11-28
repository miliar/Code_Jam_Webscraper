#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;
int a[5][5];
int hash[20];
int main() {
    int T,tc = 0;
    #ifndef ONLINE_JUDGE
    //freopen("A-small-attempt0.in", "r" , stdin);
    //freopen("output.txt" , "w" , stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&T);
    while(T--) {
        int n,m;
        scanf("%d",&n);
        memset(hash,0,sizeof(hash));
        for(int i = 1; i <= 4 ; ++i)
            for(int j = 1; j <= 4; ++j)
                scanf("%d",&a[i][j]);
        for(int i = 1; i <= 4; ++i)
            ++hash[a[n][i]];
        scanf("%d",&m);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                scanf("%d",&a[i][j]);
        for(int i = 1; i <= 4; ++i)
            ++hash[a[m][i]];
        int x = 0, y = -1;
        for(int i = 1; i <= 16; ++i)
            if(hash[i] == 2) ++x,y = i;
        printf("Case #%d: ",++tc);
        if(x == 0) printf("Volunteer cheated!\n");
        else if(x == 1) printf("%d\n",y);
        else printf("Bad magician!\n");
    }
    return 0;
}
