#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
//#define MYDEBUG

//pix max  and simu

using namespace std;

int map[100][100];
int simu[100][100];
int rowmax[100], colmax[100];
int N,M;



bool theequal(int n, int m)
{
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
        {
            if(map[i][j]!=simu[i][j])
                return false;
        }

    return true;
}

bool judge(int n, int m)
{
    for(int i=0; i<n; i++)
        rowmax[i]=1;
    for(int i=0; i<m; i++)
        colmax[i]=1;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
        {
            rowmax[i]=max(rowmax[i],map[i][j]);
            colmax[j]=max(colmax[j],map[i][j]);
            simu[i][j]=100;
        }


    for(int s=0; s<n; s++)
        for(int j=0;j<m;j++)
            simu[s][j]=min(simu[s][j],rowmax[s]);

    for(int s=0; s<m; s++)
        for(int i=0; i<n; i++)
            simu[i][s]=min(simu[i][s],colmax[s]);



    return theequal(n,m);//
}

int main()
{
    freopen("B.in.txt","r",stdin);
    freopen("B.out.txt","w",stdout);


    int T;
    cin >> T;
    int r=0;
    while(r<T)
    {
        r++;

        cin >> N >> M;

        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                cin >> map[i][j];

        bool ans = judge(N,M);



        printf("Case #%d: ",r);
        if(ans)
            printf("YES\n");
        else
            printf("NO\n");
    }


}
