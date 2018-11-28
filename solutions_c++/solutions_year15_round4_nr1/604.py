
/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//std::ios_base::sync_with_stdio (false);

#include <bits/stdc++.h>

#define endl '\n'
#define EPS (1e-9)
#define Pi 3.14159265358979
#define INF 1000000500
#define pb push_back
#define mp make_pair
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int , int >
#define VI vector < int >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()

using namespace std;

const int T = 1e2 + 5;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
char dz[4]={'v','^','>','<'};
int N,M;
int c[T][T];

int main(){
    freopen("pegman.in","r",stdin);
    freopen("pegman.out","w",stdout);

    int tests;
    scanf("%d",&tests);
    for (int t= 1; t<=tests;t++){
        scanf("%d %d\n",&N,&M);
        for (int i = 0; i < N;i++)
            {for (int j=0;j<M;j++)
            c[i][j]=getchar();getchar();}
        int ans = 0;

        for (int i = 0; i < N;i++)
        for (int j=0;j<M;j++)
        if (c[i][j]!='.')
        {
            bool carieli = true;
            for (int x = 0; x < N; x++)
                if (x != i && c[x][j]!='.')
                carieli = false;

            for (int x = 0; x < M; x++)
                if (x != j && c[i][x]!='.')
                carieli = false;

            if (carieli)
                ans = -1;
        }

        if (ans == -1){
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
            continue;
        }

        for (int i = 0; i < N;i++)
            for (int j=0;j<M;j++)
                for (int k=0;k<4;k++)
        if (c[i][j]==dz[k]){
            int x = i + dx[k];
            int y = j + dy[k];
            while (x>=0 && y>=0  && x<N && y<M && c[x][y] == '.')
            x += dx[k], y += dy[k];
            if (x < 0 || y < 0 || x>=N || y>=M)
                ans ++;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}







