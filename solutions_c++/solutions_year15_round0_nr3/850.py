#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

long long L,X;
char str[100100];
long long lef,rig;
bool flag;
bool id;
int res;
int s[6][6];
bool sol()
{
    res = 1;
    id = false;
    int tmp;
    for(int i=0;i<L;i++)
    {
        tmp = str[i] - 'i' + 2;
        res = s[res][tmp];
        if(res < 0) id ^= 1;
        res = max(res,-res);
       // printf("%d %d ?\n",id, res);
    }
    int t = X%4LL;
    int b;
    bool a;
    a = id;
    b = res;
    res = 1;
    id = false;
   // printf("%d %d.\n",a,b);
    for(int i=0;i<t;i++)
    {
        res = s[res][b];
        if(res<0) id ^= 1;
        res = max(res,-res);
        id ^= a;
    }
   // printf("%d %d...\n",id,res);
    if(id && (res==1)) return true;
    return false;
}
void check()
{
    lef = rig = L*X;
    res = 1;
    id= false;
    int tmp;
    bool flag_i = false;
    bool flag_k = false;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<L;j++)
        {
            tmp = str[j] - 'i' + 2;
            res = s[res][tmp];
            if(res < 0) id ^= 1;
            res = max(res,-res);
            if((!id)&&(res==2)){
                flag_i = true;
                lef = i*L + j+1;
                break;
            }
        }
        if(flag_i) break;
    }
    res = 1;
    id = false;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<L;j++)
        {
            tmp = str[L-1-j] -'i' + 2;
            res=s[tmp][res];
            if(res < 0) id ^= 1;
            res = max(res,-res);
            if((!id)&&(res==4))
            {
                flag_k = true;
                rig = i*L +  j+1;
                break;
            }
        }
        if(flag_k) break;
    }
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    s[1][2]=s[2][1]=2;
    s[1][3]=s[3][1]=3;
    s[1][4]=s[4][1]=4;
    s[1][1]=1;s[2][2]=s[3][3]=s[4][4]=-1;
    s[2][3]=4;s[3][2]=-4;
    s[2][4]=-3;s[4][2]=3;
    s[3][4]=2;s[4][3]=-2;
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld%lld",&L,&X);
        scanf("%s",str);
        flag=true;
        if(sol())
        {
            check();
          //  printf("%lld %lld\n",lef,rig);
            if(lef + rig > L*X) flag = false;
        }else flag = false;
        printf("Case #%d: ",++cas);
        if(flag) puts("YES");
        else puts("NO");
    }

    return 0;
}
