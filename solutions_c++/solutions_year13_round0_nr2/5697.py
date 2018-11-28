#include<cstdio>
FILE *fr, *fw;
int checkRow(int **arr, int M, int i)
{
    for(int j=0; j<M; j++)
    {
        if(arr[i][j]!=1) return 0;
    }
    return 1;
}

int checkCol(int **arr, int N, int j)
{
    for(int i=0; i<N; i++)
    {
        if(arr[i][j]!=1) return 0;
    }
    return 1;
}

void printResult(int **arr, int N, int M, int *Ai, int *Aj, int count, int c)
{
    int check=0;
    for(int p=0; p<count; p++)
    {
        if(checkRow(arr, M, Ai[p]) || checkCol(arr, N, Aj[p]))  check=0;
        else {
                check=1;
                break;
        }
    }
    if(check==0) fprintf(fw, "Case #%d: YES\n", c);
        else fprintf(fw, "Case #%d: NO\n", c);
}

int main()
{
    int tcase, N, M, count=0, status, c=1;
    fr = fopen ("B-small-attempt0.in", "rt");
    fw = fopen ("op3.txt", "w+");
    fscanf(fr, "%d", &tcase);
    while(tcase--)
    {
        fscanf(fr, "%d %d",&N,&M);
        count=0;
        int *Ai = new int[(N*M)+1];
        int *Aj = new int[(N*M)+1];
        int** arr = new int*[N];
        for(int i = 0; i < N; ++i)
            arr[i] = new int[M];
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<M; j++)
            {
                fscanf(fr, "%d", &arr[i][j]);
                if(arr[i][j]==1) {
                        Ai[count] = i;
                        Aj[count++] = j;
                }
            }
        }
        printResult(arr, N, M, Ai, Aj, count, c);
        c++;
        delete[] Ai;
        delete[] Aj;
        for(int i = 0; i < N; ++i)
            delete[] arr[i];
            delete[] arr;
    }
}
