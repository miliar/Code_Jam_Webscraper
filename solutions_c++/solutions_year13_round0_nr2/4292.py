#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

bool checkValidity(int *grass, int *maxrow, int *maxcol, int n, int m, int height)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(grass[i*m+j] == height)
            {
                if(maxrow[i] > height && maxcol[j] > height)
                    return false;
            }
        }
    }
    return true;
}

void doCase()
{
    int n, m;
    cin >> n >> m;

    set<int> heights;

    int *grass = new int[n*m];
    int *maxrow = new int[n];
    int *maxcol = new int[m];
    for(int i=0; i<n; i++)
        maxrow[i] = 0;
    for(int i=0; i<m; i++)
        maxcol[i] = 0;

    for(int i=0; i<n*m; i++)
    {
        cin >> grass[i];
        heights.insert(grass[i]);
    }
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            int h = grass[i*m+j];
            maxrow[i] = max(maxrow[i], h);
            maxcol[j] = max(maxcol[j], h);
        }
    }

    vector<int> vheights;
    for(set<int>::iterator it = heights.begin(); it != heights.end(); ++it)
        vheights.push_back(*it);
    sort(vheights.begin(), vheights.end());

    for(int i=0; i<(int)vheights.size(); i++)
    {
        if(!checkValidity(grass, maxrow, maxcol, n, m, vheights[i]))
        {
            cout << "NO" << endl;
            delete[] grass;
            delete[] maxrow;
            delete[] maxcol;
            return;
        }
    }
    delete[] grass;
    delete[] maxrow;
    delete[] maxcol;
    cout << "YES" << endl;
}

int main()
{
    int sets;
    cin >> sets;
    for(int i=0; i<sets; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}


