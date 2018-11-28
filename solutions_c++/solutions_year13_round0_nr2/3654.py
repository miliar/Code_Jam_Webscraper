#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    int t, i, j, cas_no;
    int max_x, max_y, n, m;
    int lawn[100][100];

    bool columns[100][100];
    bool rows[100][100];

    bool answer;

    scanf("%d", &t);
    cas_no = 0;

    while(t--)
    {
        cas_no++;

        scanf("%d%d", &n, &m);

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d", &lawn[i][j]);
            }
        }

        for(i=0;i<n;i++)
        {
            max_x = lawn[i][0];

            for(j=1;j<m;j++)
            {
                if(max_x < lawn[i][j])
                    max_x = lawn[i][j];
            }

            for(j=0;j<m;j++)
            {
                if(lawn[i][j] < max_x)
                    rows[i][j] = false;
                else
                    rows[i][j] = true;
            }
        }

        for(j=0;j<m;j++)
        {
            max_y = lawn[0][j];

            for(i=1;i<n;i++)
            {
                if(max_y < lawn[i][j])
                    max_y = lawn[i][j];
            }

            for(i=0;i<n;i++)
            {
                if(lawn[i][j] < max_y)
                    columns[i][j] = false;
                else
                    columns[i][j] = true;
            }
        }

        answer = true;

        for(i=0; (i<n) && (answer == true) ;i++)
        {
            for(j=0;j<m;j++)
            {
                if( (rows[i][j] == false) && (columns[i][j] == false) )
                {
                    answer = false;
                    break;
                }
            }
        }

        if(answer == true)
            printf("Case #%d: YES\n", cas_no);
        else
            printf("Case #%d: NO\n", cas_no);
    }

	return 0;
}
