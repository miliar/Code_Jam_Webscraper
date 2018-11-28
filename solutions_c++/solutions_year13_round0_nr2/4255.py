#include <iostream>

int row(int array[][100], int N, int M, int i, int j);


int main()
{
    int tot = 0;
    int N;
    int M;
    int array[100][100];
    int counter = 0;
    int i = 0;
    int j = 0;

    std::cin >> tot;

    for(i=0;i<100;i++)
        for(j=0;j<100; j++)
            array[i][j] == 0;

    while(counter < tot)
    {
        i = 0;
        j = 0;
        std::cin >> N;
        std::cin >> M;
        for(i=0;i<N; i++)
            for(j=0;j<M; j++)
                std::cin >> array[i][j];

        i = 0;
        j = 0;
        for(i=0;i<N;i++)
        {
            for(j = 0; j<M; j++)
            {
                if(row(array, N,M,i,j) == 0)
                {
                    std::cout << "Case #" << counter+1 << ": NO\n";
                    i = N+1;
                    break;
                }
            }
        }
        if(i == N && j == M)
            std::cout << "Case #" << counter+1 << ": YES\n";
        counter++;
    }


    return 0;

}

int row(int array[][100], int N, int M, int i, int j)
{
    int k = 0;
    int l = 0;
    int constant = array[i][j];

    while(k<M)
    {
        if(array[i][k] <= constant)
            k++;
        else
            break;
    }
    if(k==M)
        return 1;

    while(l<N)
    {
        if(array[l][j] <= constant)
            l++;
        else
            break;
    }
    if(l==N)
        return 1;

    return 0;
}

