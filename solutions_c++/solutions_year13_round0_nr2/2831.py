#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

bool match(int N, int M, vector<vector<int> > &d, vector<int>& maxR, vector<int>& maxC)
{
    vector<vector<int> > e(N, vector<int>(M, 0));
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            e[i][j] = min(maxR[i], maxC[j]);
            if(e[i][j]!=d[i][j])
            {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    freopen("lawnmower.in", "r", stdin);
    freopen("lawnmower.out", "w", stdout);

    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        int N, M;
        cin >> N >> M;
        vector<vector<int> > d(N, vector<int>(M, 0));
        vector<int> maxR(N, 0);
        vector<int> maxC(M, 0);
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                cin >> d[i][j];
                maxR[i] = max(maxR[i], d[i][j]);
                maxC[j] = max(maxC[j], d[i][j]);
            }
        }

        if(match(N, M, d, maxR, maxC))
        {
            cout << "Case #" << t+1 << ": YES" << endl;
        }
        else
        {
            cout << "Case #" << t+1 << ": NO" << endl;
        }
    }

    return 0;
}
