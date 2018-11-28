#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

int minEatenSecondMethod(int N, vector<int>& m)
{
    int maxDif = 0;
    for (int i = 1; i < N; ++i)
    {
        maxDif = max(maxDif, m[i-1] - m[i]);
    }

    int eaten = 0;
    for (int i = 0; i < N-1; ++i)
    {
        eaten += min(maxDif, m[i]); 
    }
    return eaten;
}

int minEatenFirstMethod(int N, vector<int>& m)
{
    int eaten = 0;
    for (int i = 1; i < N; ++i)
    {
        if (m[i] < m[i-1])
        {
            eaten += abs(m[i] - m[i-1]);
        }
    }
    return eaten;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int N;
        cin >> N;

        vector<int> m(N);  
        for (int i = 0; i < N; ++i)
        {
            cin >> m[i];
        }


        cout << "Case #" << (t+1) << ": " << minEatenFirstMethod(N, m) << " " << minEatenSecondMethod(N, m) << endl;

    }
    return 0;
}
