#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;


const int maxn = 5;

int a[maxn][maxn], b[maxn][maxn];

int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas, n, m;
    scanf("%d",&cas);

    for(int t = 1 ;t <= cas; ++t)
    {
        scanf("%d",&n);
        for(int i = 1 ; i<= 4; ++ i)
            for(int j =1 ;j <= 4; ++ j)
                cin>>a[i][j];
        cin>>m;
        for(int i = 1 ;i <= 4; ++ i)
            for(int j = 1 ;j <= 4; ++ j)
            cin>>b[i][j];
        int cnt =0, ans;
        for(int i = 1 ; i<= 4;++ i)
            for(int j = 1 ; j<= 4;++ j)
                if(a[n][i] == b[m][j]) ++cnt, ans = a[n][i];
        if(1 == cnt )printf("Case #%d: %d\n",t,ans);
        if(cnt > 1) printf("Case #%d: Bad magician!\n",t);
        if(0 == cnt) printf("Case #%d: Volunteer cheated!\n",t);
    }
    return 0;
}
