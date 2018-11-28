#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    FILE *fin = freopen("B-small.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-small.out", "w", stdout);
    int tries,N, max;
    cin >> tries;
    for (int j = 1; j <= tries; j++)
    {
        cin >> N;
        int **arr = new int*[2*N-1];
        max = 0;
        for (int i = 0; i < 2*N-1; i++)
        {
            arr[i] = new int[N];
            for (int k = 0; k < N; k++)
            {
                cin >> arr[i][k];
            }
            if (arr[i][N-1] > max)
                max = arr[i][N-1];
        }
        int *check = new int[max];
        fill_n(check, max, 0);
        vector<int> missing;
        for (int i = 0; i < 2*N-1; i++)
        {
            for (int k = 0; k < N; k++)
                check[arr[i][k]-1]++;
        }
        for (int i = 0; i < max; i++)
        {
            if (check[i] % 2 != 0)
                missing.push_back(i+1);
        }
        cout << "Case #" << j << ": ";
        for (int i = 0; i < N; i++)
            cout << missing[i] << " ";
        cout << endl;
    }
    return 0;
}
