#include <stdio.h>
#include <algorithm>

using namespace std;

#define SIZE 101

bool check_row(int m, int x, int y, int lawn[][SIZE])
{
    for (int i = 0; i < m; ++i)
      if (lawn[x][i] > lawn[x][y])
      {
        return false;
      }

    return true;
}

bool check_column(int n, int x, int y, int lawn[][SIZE])
{
    for (int i = 0; i < n; ++i)
      if (lawn[i][y] > lawn[x][y])
      {
        return false;
      }

    return true;
}

void run(int n, int m, int lawn[][SIZE])
{
    int total = n * m;

    if (n == 1 || m == 1)
    {
      printf("YES\n");
      return;
    }

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        if (check_row(m, i, j, lawn) ||
            check_column(n, i, j, lawn))
        {
        }
        else
        {
          printf("NO\n");
          return;
        }

    printf("YES\n");
}

int main()    
{
    int num_case;
    int n, m;
    int lawn[SIZE][SIZE];

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        scanf("%d %d", &n, &m);

        for(int j = 0; j < n; ++j)
            for(int k = 0; k < m; ++k)
            {
                scanf("%d", &lawn[j][k]);
            }

        printf("Case #%d: ", i);
        run(n, m, lawn);
    }

    return 0;
}
