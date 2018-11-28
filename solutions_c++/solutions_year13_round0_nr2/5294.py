#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <fstream>



int main (void)
{
    long T;
    std::cin >> T;

    std::ofstream f("out.txt");

    for (long i = 1; i <= T; i++)
    {
        int N;
        int M;

        std::cin >> N;
        std::cin >> M;

        int grid[N][M];

        int boolGrid[N][M];

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                std::cin >> grid[j][k];
                boolGrid[j][k] = true;
            }
        }
    
        bool canCut = true;

        long count = 0;

        while (true)
        {
            bool canCut1 = true;
            bool canCut2 = true;

            int iMax = 0;
            int jMax = 0;
            int maxVal = 0;

            if (count == N * M)
                break;

            for (int j = 0; j < N; j++)
            {
                for (int k = 0; k < M; k++)
                {
                    if (!boolGrid[j][k])
                        continue;

                    if (grid[j][k] > maxVal)
                    {
                        maxVal = grid[j][k];
                        iMax = j;
                        jMax = k;
                    }
                }
            }

            std::cout << "iMax: " << iMax << std::endl;
            std::cout << "jMax: " << jMax << std::endl;
            std::cout << "maxVal: " << maxVal << std::endl;

            for (int j = 0; j < M; j++)
            {
                if (boolGrid[iMax][j] == false && grid[iMax][j] != maxVal)
                {
                    canCut1 = false;
                    break;
                }

                if (grid[iMax][j] == maxVal && boolGrid[iMax][j])
                {
                    count++;
                    boolGrid[iMax][j] = false;
                }
            }

            for (int j = 0; j < N; j++)
            {
                std::cout << "i: " << j << " j: " << jMax << std::endl;
                if (boolGrid[j][jMax] == false && grid[j][jMax] != maxVal)
                {
                    canCut2 = false;
                    break;
                }

               if (grid[j][jMax] == maxVal && boolGrid[j][jMax])
                {
                    count++;
                    boolGrid[j][jMax] = false;
                }
            }

            if (canCut1 == false && canCut2 == false)
            {
                canCut = false;
                break;
            }

            for (int j = 0; j < N; j++)
            {
                for (int k = 0; k < M; k++)
                {
                    std::cout << boolGrid[j][k];
                }
                std::cout << std::endl;
            }
        }
        
        if (canCut)
            f << "Case #" << i << ": YES" << std::endl;
        else
            f << "Case #" << i << ": NO" << std::endl;
       
    }

    return 0;
}
