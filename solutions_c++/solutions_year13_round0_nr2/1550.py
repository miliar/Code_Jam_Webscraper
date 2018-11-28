#include <fstream>
#include <vector>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main()
{
    int N;
    cin >> N;
    for (int gh = 0; gh < N; ++gh)
    {
        vector <vector <int> > A;
        int n, m;
        cin >> n >> m;
        A.resize(n, vector <int> (m, 0));
        vector <int> maxX(n, 0), maxY(m, 0);
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                cin >> A[i][j];
                maxX[i] = max(maxX[i], A[i][j]);
                maxY[j] = max(maxY[j], A[i][j]);
            }
        }
        int Flag = 1;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (A[i][j] < maxX[i] && A[i][j] < maxY[j])
                {
                    Flag = 0;
                }
            }
        }
        cout << "Case #" << gh + 1 << ": ";
        if (Flag)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

}
