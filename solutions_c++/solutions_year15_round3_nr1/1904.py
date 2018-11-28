#include <iostream>

using namespace std;

int m[51][51];

int PD(int c, int w)
{
    int &ret = m[c][w];

    if (ret >= 0)
        return ret;

    if (c - w > w)
    {
        ret = PD(c - w, w) + 1;
        return ret;
    }

    ret = PD(c - 2, w) + 1;
    return ret;

}
int main()
{
    int n;

    cin >> n;
    int R, C, W;


    for (int i = 0; i < 50; i++)
    {
        for (int j = 0; j < 50; j++)
        {
            if (i == j)
                m[i][j] = i;
            else if (i == 0 || j == 0)
                m[i][j] = 1;
            else if (j == 1)
                m[i][j] = i;
            else if (i == j + 1)
                m[i][j] = i;
            else if (i <= 2 * j)
                m[i][j] = j + 1;
            else
                m[i][j] = -1;
        }
    }
    for (int i = 0; i < n; i++)
    {

        cin >> R >> C >> W;

        cout << "Case #" << i + 1<< ": " << PD(C, W) << endl;
    }
}
