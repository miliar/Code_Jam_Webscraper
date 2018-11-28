#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std ;

int cases ;
int N,M;
int arr[105][105];
int record[105];

bool f(int id)
{
    int idmax = -100;
    for(int j = 0 ; j < M ; j++)
    {
        idmax = max(idmax,arr[id][j]);
    }

    for(int j = 0 ; j < M ; j++)
    {
        if(arr[id][j] < idmax || record[j] != -1 )
        {
            if(record[j] == -1 )
            {
                for(int k = 0 ; k < id ; k++)
                {
                    if(arr[k][j] <= arr[id][j] )
                    {
                         continue ;
                    }
                    else
                    {
                         return false ;
                    }
                }
                record[j] = arr[id][j];
            }

            else if(record[j] > arr[id][j] ) return false ;
            else if(record[j] < arr[id][j] ) return false ;
        }
    }
    return true ;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);


    scanf("%d",&cases);

    for(int c = 1 ; c <= cases ; c++)
    {
        bool ok = true;
        scanf("%d%d",&N,&M);
        for(int i = 0 ; i < N ; i++)
        for(int j = 0 ; j < M ; j++)
        scanf("%d",&arr[i][j]);

        for(int j = 0 ; j < M ; j++)
            record[j] = -1 ;

        for(int i = 0 ; i < N ; i++)
        {
            if(!f(i))
            {
                ok = false ;
                goto END_RESULT ;
            }
        }

        END_RESULT:
/*
        for(int i = 0 ; i < N ; i++)
        {
            for(int j = 0 ; j < M ; j++)
                printf(" %d",arr[i][j]);
            puts("");
        }
        puts("");
*/

            printf("Case #%d: ",c);
            (ok)?puts("YES"):puts("NO");
    }
    return 0 ;
}
