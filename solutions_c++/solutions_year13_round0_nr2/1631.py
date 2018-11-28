#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[200][200],p[200][200];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        int n, m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)    
            for(int j=0;j<m;j++)
                scanf("%d", &s[i][j]);
        memset(p,0,sizeof(p));
        bool ans = true;
        for(int i,j,k=1;k<=100 && ans;k++){
            for(i=0;i<n;i++){
                for(j=0;j<m;j++){
                    if(s[i][j] < k && p[i][j] == 0)
                        ans = false;
                    if(s[i][j] > k) break;
                }
                if(j == m){
                    for(j=0;j<m;j++)
                        p[i][j] = 1;
                }
            }
            for(j=0;j<m;j++){
                for(i=0;i<n;i++){
                    if(s[i][j] < k && p[i][j] == 0)
                        ans = false;
                    if(s[i][j] > k) break;
                }
                if(i == n){
                    for(i=0;i<n;i++)
                        p[i][j] = 1;
                }
            }
        }
        
        printf("Case #%d: %s\n", tt, ans?"YES":"NO");
    }
    return 0;
}

