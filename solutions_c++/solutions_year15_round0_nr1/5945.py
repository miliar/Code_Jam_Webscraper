#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cmath>
using namespace std;
#define PB push_back
#define PPB pop_back
#define MP make_pair
#define LL long long
#define ULL unsigned long long
#define fs first
#define sc second
#define pii pair<int,int>
#define pll pair<LL,LL>
#define ppii pair< pii,int >
#define BIG 2000000000
#define N 1010

int n,kasus,sum,ans,temp;
char s[N];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("a.out","w",stdout);
    
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++) {
        scanf("%d",&n);
        scanf("%s",s);
        ans = 0;
        sum = 0;
        for (int i=0;i<=n;i++) {
            temp = max(0,i-sum);
            ans += temp;
            sum += ((s[i]-'0') + temp);
        }
        printf("Case #%d: %d\n",z,ans);
    }
    
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
