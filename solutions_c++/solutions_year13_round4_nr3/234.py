#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

int N;
int A[2000];
int B[2000];

int deg[2000];
bool used[2000];
int X[2000];

// (i, j) \in edges means that X[i] < X[j]
vector< vector<int> > edges;

bool ricorri(int k)
{
    if (k == N+1)
        return true;

    for (int i = 0; i < N; i += 1)
    {
//        cout << i << " " << deg[i] << " " << used[i] << endl;
        if (deg[i] == 0 && !used[i])
        {
            used[i] = true;

            X[i] = k;

            // check < before
            int cnt = 0;
            if (A[i] > 1) {
                for (int l = 0; l < i; l += 1)
                {
                    if (used[l] && A[l] == A[i] - 1 && X[l] < k)
                    {
                        cnt += 1;
                    }
                }
                if (cnt == 0)
                {
                    used[i] = false;
                    continue;
                }
            }
cnt = 0;
            if (B[i] > 1) {
                for (int l = N-1; l > i; l -= 1)
                {
                    if (used[l] && B[l] == B[i] - 1 && X[l] < k)
                    {
                        cnt += 1;
                    }
                }
                if (cnt == 0)
                {
                    used[i] = false;
                    continue;
                }
            }

//            cout << i << endl;
//            cout << edges[i].size() << endl;
            for (int j = 0; j < edges[i].size(); j += 1)
            {
                deg[edges[i][j]] -= 1;
//                cout << deg[edges[i][j]] << endl;
            }

            // recurse
            if (ricorri(k+1))
            {
                return true;
            }

            for (int j = 0; j < edges[i].size(); j += 1)
            {
                deg[edges[i][j]] += 1;
            }

            used[i] = false;
        }
    }

    return false;
}


int elabora ()
{
    cin >> N;

    for (int i = 0; i < N; i += 1)
    {
        cin >> A[i];
    }
    for (int i = 0; i < N; i += 1)
    {
        cin >> B[i];
    }

    edges.assign(N, vector<int>());

    int max_val = 1;
    int max_idx = 0;
    int max_cnt = 0;

    for (int i = 0; i < N; i += 1)
    {
        if (A[i] > max_val)
        {
            if (max_cnt == 1)
            {
                // X[i] > X[max_idx]
                edges[max_idx].push_back(i);
                //cout << max_idx << " < " << i << endl;
            }
            max_val = A[i];
            max_idx = i;
            max_cnt = 0;
        }
        if (A[i] == max_val)
        {
            max_cnt += 1;
        }

        // A[j] >= A[i] --> X[i] < X[j]
        for (int j = 0; j < i; j += 1)
        {
            if (A[j] >= A[i])
            {
                edges[i].push_back(j);
                //cout << i << " < " << j << endl;
            }
        }
    }

    max_val = 1;
    max_idx = N-1;
    max_cnt = 0;

    for (int i = N-1; i >= 0; i -= 1)
    {
        if (B[i] > max_val)
        {
            if (max_cnt == 1)
            {
                // X[i] > X[max_idx]
                edges[max_idx].push_back(i);
                //cout << max_idx << " < " << i << endl;
            }
            max_val = B[i];
            max_idx = i;
            max_cnt = 0;
        }
        if (B[i] == max_val)
        {
            max_cnt += 1;
        }

        // B[j] >= B[i] --> X[i] < X[j]
        for (int j = N-1; j > i; j -= 1)
        {
            if (B[j] >= B[i])
            {
                edges[i].push_back(j);
                //cout << i << " < " << j << endl;
            }
        }
    }

    // We have a large set of necessary conditions

    memset(deg, 0, 2000 * sizeof(int));
    memset(used, 0, 2000 * sizeof(bool));

    for (int i = 0; i < N; i += 1)
    {
        for (int j = 0; j < edges[i].size(); j += 1)
        {
            deg[edges[i][j]] += 1;
        }
    }

    if (!ricorri(1))
    {
        cerr << "argh" << endl;
    }

    cout << X[0];
    for (int i = 1; i < N; i += 1)
    {
        cout << ' ' << X[i];
    }
}

int main ()
{
    int tcs;
    cin >> tcs;
    for (int i = 1; i <= tcs; i += 1)
    {
        cout << "Case #" << i << ": ";
        elabora();
        cout << endl;
    }
}
