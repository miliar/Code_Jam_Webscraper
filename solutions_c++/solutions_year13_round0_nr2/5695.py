#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i =1; i < t+1; i++)
    {
        int n,m;
        cin >> n >> m;
        int lawn[n][m];
        int max_rows[n];
        int max_cols[n];
        for (int j = 0; j < n; j++)
            max_rows[j] = 0;
        for (int k = 0; k < m; k++)
            max_cols[k] = 0;

        for (int j = 0; j < n; j++)
        for (int k = 0; k < m; k++)
        {
            cin >> lawn[j][k];
            if (lawn[j][k] > max_rows[j])
                max_rows[j] = lawn[j][k];
            if (lawn[j][k] > max_cols[k])
                max_cols[k] = lawn[j][k];
        }
        
        bool flag = true;
        for (int j = 0; j < n; j++)
        for (int k = 0; k < m; k++)
            if(min(max_cols[k], max_rows[j]) != lawn[j][k])
                flag = false;

        string s;
        s = "Case #";
       /* stringstream ss;
        ss << i;
        s += ss.getstring();*/
        cout << s << i;
        s = ": ";
        if(flag)
            cout << ": YES" << endl;
        else
            cout << ": NO" << endl;
    }
}

