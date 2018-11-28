#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

struct Line
{
    int max_;
    int diff;
};

int main()
{
    int T, cases = 0;
    cin >> T;
    int  a[100][100];
    int  mark[100][100];

    while(T--)
    {
        int N,M;
        cin >> N >> M;
        // load
        memset(mark, 0, sizeof mark);
        for(int i =0; i < N; i++)
        {
            int max = 0;
            for(int j =0; j < M; j++)
            {
                cin >> a[i][j];
                if(a[i][j] > max)
                {
                    max = a[i][j];
                }
            }
            for(int j =0; j < M; j++)
            {
                if(a[i][j] < max)
                {
                    mark[i][j] = 1;
                }
             }
        }
        for(int j =0; j < M; j++)
        {
            int max = 0;
            for(int i =0; i < N; i++)
            {
                if(a[i][j] > max)
                {
                    max = a[i][j];
                }
            }
            for(int i =0; i < N; i++)
            {
                if(a[i][j] < max && mark[i][j] == 1) goto FAIL;
            }
        }
            printf("Case #%d: YES\n", ++cases);
            continue;
        FAIL:
            printf("Case #%d: NO\n", ++cases);
            continue;
        //

    }
}
