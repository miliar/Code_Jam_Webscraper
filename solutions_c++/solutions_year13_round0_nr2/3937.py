#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <iostream>
 
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        int N,M;
        cin >> N >> M;
        int lawn[100][100];
        int maxRow[100], maxCol[100];
        for(int i=0; i<N; i++)
            maxRow[i] = 0;
        for(int j=0; j<M; j++)
            maxCol[j] = 0;
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<M; j++)
            {
                cin >> lawn[i][j];
                if(lawn[i][j] > maxRow[i])
                    maxRow[i] = lawn[i][j];
                if(lawn[i][j] > maxCol[j])
                    maxCol[j] = lawn[i][j];
            }
        }
        bool possible = true;
        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                if(lawn[i][j] != maxRow[i] && lawn[i][j] != maxCol[j])
                    possible = false;
        cout << "Case #" << t;
        if(possible)
            cout << ": YES" << endl;
        else
            cout << ": NO" << endl;
    }
}
