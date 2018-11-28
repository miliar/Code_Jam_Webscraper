#include <iostream>

int main(void)
{
    int runs;
    std::cin >> runs;

    for(int r = 1; r <= runs; ++r)
    {
        int N,M;
        std::cin >> N;
        std::cin >> M;

        int lawn[N][M];

        for(int i = 0; i < N; ++i)
        {
            for(int j = 0; j < M; ++j)
            {
                std::cin >> lawn[i][j];
            }
        }

        int maxRow[N];
        int maxCol[M];

        for(int i =0; i < N; ++i)
        {
            int max = 0;
            for(int j = 0; j < M; ++j)
            {
                if(lawn[i][j] > max)
                    max = lawn[i][j];
            }
            maxRow[i] = max;
        }

        for(int j =0; j < M; ++j)
        {
            int max = 0;
            for(int i = 0; i < N; ++i)
            {
                if(lawn[i][j] > max)
                    max = lawn[i][j];
            }
            maxCol[j] = max;
        }

        bool possible = true;

        for(int i = 0; i < N; ++i)
        {
            for(int j = 0; j < M; ++j)
            {
                if(lawn[i][j] < maxRow[i] && lawn[i][j] < maxCol[j])
                {
                    possible = false;
                    break;
                }
                if(!possible)
                    break;
            }
        }
        
        std::cout << "Case #" << r << ": ";
        if(possible)
            std::cout << "YES" << std::endl;
        else
            std::cout << "NO" << std::endl;
    }
}
