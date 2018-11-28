#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

int vis[20];


int main() {
       freopen("A-small-attempt8.in","r",stdin);
        freopen("A-small-attempt8.out","w",stdout);
        int t,ca = 1;
        scanf("%d",&t);

        while(t--) {
                int x;
                scanf("%d",&x);
                memset(vis,0,sizeof(vis));
                for(int i = 1; i <= 4; ++i) {
                        for(int j = 1; j <= 4; ++j ) {
                                int ch;
                                scanf("%d",&ch);
                                if(i == x) vis[ch] = 1;
                        }
                }

                scanf("%d",&x);
                int flag = 0;
                int ans;
                for(int i = 1; i <= 4; ++i) {
                        for(int j = 1; j <= 4; ++j) {
                                int ch;
                                scanf("%d",&ch);
                                if(i == x) {
                                        if(vis[ch]) {
                                                flag++;
                                                ans = ch;

                                        }

                                }

                        }
                }
                printf("Case #%d: ",ca++);
                if(!flag) printf("Volunteer cheated!\n");
                else if(flag > 1) printf("Bad magician!\n");
                else if(flag == 1) printf("%d\n",ans);

        }
        return 0;
}

