#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <fstream>
using namespace std;

int T;
int m[101];
int A, N;
int minn = 10000000;
ifstream fin("t.in");
ofstream fout("t.out");


int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void dfs(int curmote, int curi, int curmin)
{
    if(curi <= N)
    {
        if(curmote > m[curi])
            dfs(curmote+m[curi],curi+1,curmin);
        else
        {
            dfs(curmote*2-1,curi,curmin+1); //add
            dfs(curmote,curi+1,curmin+1);   //delete
        }

    }
    else if(curi == N+1)
        minn = (curmin<minn)?curmin:minn;
}

int main()
{
    fin >> T;
    for(int r=1; r<=T; r++)
    {
        minn = 10000000;
        fin >> A;
        fin >> N;
        for(int i=1; i<=N; i++)
            fin >> m[i];
        if(A==1){
            fout << "Case #" << r << ": " << N << endl;
            continue;
        }
       //     printf("Case #%d: %d\n",r,N);

        qsort(m+1,N,sizeof(int),compare);

        dfs(A,1,0);
        fout << "Case #" << r << ": " << minn << endl;
        //printf("Case #%d: %d\n",r,minn);
    }

    return 0;
}
