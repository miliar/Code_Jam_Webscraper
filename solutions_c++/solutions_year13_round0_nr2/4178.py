#include <iostream>
using namespace std;

#if 0
#define INPUT_FILE  "B-small.in.txt"
#define OUTPUT_FILE "B-small.out.txt"
#define LAWN_MAX 10
#else
#define INPUT_FILE  "B-large.in.txt"
#define OUTPUT_FILE "B-large.out.txt"
#define LAWN_MAX 100
#endif

int lawn [LAWN_MAX][LAWN_MAX];

int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    int T, N, M;
    
    scanf("%i\n", &T);
    
    // For each test case
    for (int t = 0; t < T; t++)
    {
        scanf("%i %i\n", &N, &M);
        for (int n = 0; n < N; n++)
        {
            for (int m = 0; m < M; m++)
            {
                scanf("%i\n", &lawn[n][m]);
            }
        }
        
        cout << "Case #" << t+1 << ": ";
        
        if (N == 1 || M == 1)
        {
            cout << "YES" << endl;
            continue;
        }
        
        bool invalidPattern = false;
        
        for (int n = 0; n < N; n++)
        {
            for (int m = 0; m < M; m++)
            {
                int h = lawn[n][m];
                bool pathBlocked = false;
                
                // Check horitzontal
                for (int y = 0; y < M; y++)
                {
                    if ( h < lawn[n][y] )
                    {
                        pathBlocked = true;
                        break;
                    }
                }
                
                if (!pathBlocked) continue;
                
                // Check vertical
                pathBlocked = false;
                for (int x = 0; x < N; x++)
                {
                    if ( h < lawn[x][m] )
                    {
                        pathBlocked = true;
                        break;
                    }
                }
                
                if (pathBlocked)
                {
                    invalidPattern = true;
                    break;
                }
            }
            if (invalidPattern) break;
        }
        
        if (invalidPattern)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
    return 0;
}