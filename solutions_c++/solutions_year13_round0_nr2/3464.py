#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for (int k = 1; k <= t; k++)
    {
        int n, m;
        cin>>n;
        cin>>m;
        int lawn[n][m];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin>>lawn[i][j];
            }
        }
        int rowMaxes[n];
        int columnMaxes[m];
        for (int i = 0; i < n; i++)
        {
            rowMaxes[i] = lawn[i][0];
            for (int j = 1; j < m; j++)
            {
                if (lawn[i][j] > rowMaxes[i])
                    rowMaxes[i] = lawn[i][j];
            }
        }
        for (int j = 0; j < m; j++)
        {
            columnMaxes[j] = lawn[0][j];
            for (int i = 1; i < n; i++)
            {
                if (lawn[i][j] > columnMaxes[j])
                    columnMaxes[j] = lawn[i][j];
            }
        }
        int possible = 1;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (!((lawn[i][j] == rowMaxes[i]) || (lawn[i][j] == columnMaxes[j])))
                {
                    possible = 0;
                    break;
                }
            }
        }
        if (possible)
        {
            cout<<"Case #"<<k<<": YES"<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": NO"<<endl;
        }
    }
    return 0;
}
