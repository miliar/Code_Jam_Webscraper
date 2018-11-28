#include <iostream>
#include <vector>

using namespace std;

int a[1024][2048];
int b[1024][2048];
int z;

int x0[1024];
int y0[1024];
int x1[1024];
int y1[1024];

int y[2048];

int dx[] = {0, -1, 0, 1};
int dy[] = {1, 0, -1, 0};

vector<int> xx;
vector<int> yy;
vector<int> dd;

int main()
{
    int p;
    cin >> p;

    for (int tt=1; tt<=p; tt++)
    {
        int n, m, k;
        cin >> n >> m >> k;

        int t = 0;
        y[t++] = 0;

        for (int i=0; i<k; i++)
        {
            cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
            y[t++] = y0[i];
            y[t++] = ++y1[i];
        }

        t = m;

        for (int i=0; i<n; i++)
            for (int j=0; j<t; j++)
                a[i][j] = 1;

        for (int i=0; i<k; i++)
        {
            for (int u=x0[i]; u<=x1[i]; u++)
                for (int v=y0[i]; v<y1[i]; v++)
                    a[u][v] = 0;
        }

        k = 0;

        for (int i=0; i<n; i++)
            if (a[i][0])
            {
                z++;
                xx.clear();
                xx.push_back(i);
                yy.clear();
                yy.push_back(0);
                dd.clear();
                dd.push_back(0);
/*
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<t; j++)
                cout << a[i][j] << " ";
            cout << endl;
        }
*/
                for (; xx.size();)
                {
                    a[xx.back()][yy.back()]--;
                    b[xx.back()][yy.back()] = z;

//                    cout << xx.back() << " " << yy.back() << endl;

                    if (yy.back() == t-1)
                    {
                        k++;
                        break;
                    }

                    for (int q = 0; q < 5; q++)
                    {
                        if (q == 4)
                        {
                            xx.pop_back();
                            yy.pop_back();
                            dd.pop_back();
                            break;
                        }

                        int d = 5 - q + dd.back() & 3;
                        int x = xx.back() + dx[d];
                        int y = yy.back() + dy[d];

                        if (x >= 0 && x < n && y >= 0 && y < t)
                            if (a[x][y] && b[x][y] != z)
                            {
                                xx.push_back(x);
                                yy.push_back(y);
                                dd.push_back(d);
                                break;
                            }
                    }
                }
            }

        cout << "Case #" << tt << ": " << k << endl;
    }
    return 0;
}
