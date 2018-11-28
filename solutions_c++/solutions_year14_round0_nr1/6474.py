#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<queue>
#include<cmath>

#define For(i,n) for(int i=0;i<(n);i++)
#define Fori(i,si,n) for( int i=(si);i<(n);i++)
#define clr(x,y)    memset(x,y,sizeof(x))
#define sf  scanf
#define pf  printf
#define mp  make_pair

using namespace std;

const int Maxn=110;
int mat[2][4][4];
int ans[2];
int cnt[4*4];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int cas;    cin>>cas;
    int _=1;
    while(cas--)
    {
        clr(cnt,0);
        For(k,2)
        {
            sf("%d",&ans[k]);   ans[k]--;
            For(i,4)For(j,4)    sf("%d",&mat[k][i][j]);
            For(j,4)    cnt[mat[k][ans[k]][j] - 1]++;
        }
        int res = -1,rescnt=0;
        For(i,16){
            if(cnt[i] == 2){
                rescnt++;
                res = i+1;
            }
        }
        pf("Case #%d: ",_++);
        if(rescnt==0){
            puts("Volunteer cheated!");
        }else if(rescnt>1){
            puts("Bad magician!");
        }else{
            pf("%d\n",res);
        }

    }
    return 0;
}
