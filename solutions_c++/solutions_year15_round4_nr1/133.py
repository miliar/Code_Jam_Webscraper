/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define clr(a) memset(a,0,sizeof a)
#define clr1(a) memset(a,-1,sizeof a)
#define dbg(a) printf("%d\n",a)
typedef pair<int,int> pp;
const double eps=1e-9;
const double pi=acos(-1.0);
const int INF=0x3f3f3f3f;
const LL inf=(((LL)1)<<61)+5;
char s[106][105];
int main()
{
    //freopen("A-small-attempt0 (2).in" , "r" , stdin);
    //freopen("A-small-attempt0 (2).out" , "w" , stdout);
    int t,cnt=0;
    scanf("%d",&t);
    while(t--){
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",s[i]);
        int flag=0,ans=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='.'){
                    int f1=1,f2=1;
                    for(int k=0;k<r;k++){
                        if(k!=i){
                            if(s[k][j]!='.')
                            {
                                f1=0;
                                break;
                            }
                        }
                    }
                    for(int k=0;k<c;k++){
                        if(k!=j){
                            if(s[i][k]!='.'){
                                f2=0;
                                break;
                            }
                        }
                    }
                    if(f1&&f2) {
                        flag=1;
                        break;
                    }
                }
            }
            if(flag) break;
        }
        if(flag){
            printf("Case #%d: IMPOSSIBLE\n",++cnt);
            continue;
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]=='^'){
                    if(i==0||s[i-1][j]=='.')
                        ans++;
                }
                if(s[i][j]=='v'){
                    if(i==r-1||s[i+1][j]=='.')
                        ans++;
                }
                if(s[i][j]=='<'){
                    if(j==0||s[i][j-1]=='.')
                        ans++;
                }
                if(s[i][j]=='>'){
                    if(j==c-1||s[i][j+1]=='.')
                        ans++;
                }
                //printf("%d %d %d\n",i,j,ans);
            }
        }
        printf("Case #%d: %d\n",++cnt,ans);
    }
    return 0;
}
