#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;


const int mod = 1e9+7;
const int N = 500200000;
const int M = 5e5+30;
char s[M],tmp[M];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t,n,cas=1;
    scanf("%d",&t);
    while(t--){
        scanf("%s",s);
        printf("Case #%d: ",cas++);
        int n = strlen(s);
        int cnt = 1;
        tmp[0] = s[0];
        for(int i=1;i<n;i++){
            if(tmp[cnt-1]!=s[i]){
                tmp[cnt++] = s[i];
            }
        }
        if(tmp[0] == '-'){
            if(cnt%2)printf("%d\n",cnt);
            else printf("%d\n",cnt-1);
        }else {
            if(cnt%2)printf("%d\n",cnt-1);
            else printf("%d\n",cnt);
        }
    }
    return 0;
}
