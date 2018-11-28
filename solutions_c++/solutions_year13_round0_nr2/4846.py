// for small input
#include <iostream>

using namespace std;

#define MAXD 100
int dst[MAXD][MAXD];

int main(int argc, char** argv)
{
    int T;
    cin >> T;

    for (int i = 0 ; i < T; i++)
    {
        memset(dst, 0, sizeof(dst));
        int n, m;
        cin >> n >> m;
        bool flag = true;

        for (int nn = 0; nn < n; nn++)
        {
            for (int mm = 0; mm < m; mm++)
            {
                cin >> dst[nn][mm];
                //cout << dst[nn][mm] << " ";
            }
            //cout << endl;
        }

       for (int x = 0; x < n; x++)
        {
            if (flag == false)
                break;

            for (int y = 0; y < m; y++)
            {
                if (dst[x][y] < 100)
                {
                    // check horizontal
                    bool h2 = false;
                    for (int k = 0; k < m; k++)
                        if (dst[x][k] > dst[x][y])
                            h2 = true;

                    bool v2 = false;
                    for (int k = 0; k < n; k++)
                        if (dst[k][y] > dst[x][y])
                            v2 = true;

                    if (h2 && v2)
                    {
                        flag = false;
                        break;
                    }
                    /*
                    // check up, down, left and right
                    bool has2[4];
                    memset(has2, 0, sizeof(has2));
                    if (x > 0)  // up
                        has2[0] = (dst[x-1][y] == 2);
                    if (x < n-1)
                        has2[1] = (dst[x+1][y] == 2);
                    if (y > 0)
                        has2[2] = (dst[x][y-1] == 2);
                    if (y < m-1)
                        has2[3] = (dst[x][y+1] == 2);

                    // set flag to false if (up || down) && (left || right) is true
                    if ((has2[0] || has2[1]) && (has2[2] || has2[3]))
                    {
                        flag = false;
                        break;
                    }
                    */

                }
            }
        }


        cout << "Case #" << i+1 << ": ";
        if (flag)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}

