#include <iostream>
using namespace std;

int N, M;
int T;
#define MAX_NUM 105
int arr[MAX_NUM][MAX_NUM];
int r[MAX_NUM];
int c[MAX_NUM];

void build()
{
    int i, j;
    for (i=1; i<=N; i++)
    {
        for (j=1; j<=M; j++)
        {
            if (arr[i][j] == 2)
            {
                break;
            }
        }
        if (j==M+1)
        {
            r[i] = 1;
        }else{
            r[i] = 0;
        }
    }
    for (j=1; j<=M; j++)
    {
        for (i=1; i<=N; i++)
        {
            if (arr[i][j]==2)
            {
                break;
            }
        }
        if (i==N+1)
        {
            c[j] = 1;
        }else{
            c[j] = 0;
        }
    }
}
int main()
{
    int count = 0;
    cin>>T;
    while(T--)
    {
        count++;
        cin>>N>>M;
        int i, j;
        for(i=1; i<=N; i++)
        {
            for (j=1; j<=M; j++)
            {
                cin>>arr[i][j];
            }
        }
        build();
        bool legal = true;
        for (i=1; i<=N; i++)
        {
            for (j=1; j<=M; j++)
            {
                if (arr[i][j]==1 && r[i]!=1 && c[j]!=1)
                {
                    legal = false;
                    break;
                }
            }
            if (!legal)
            {
                break;
            }
        }
        cout<<"Case #"<<count<<": ";
        if (legal)
        {
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}

/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
*/
