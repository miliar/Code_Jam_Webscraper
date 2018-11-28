#include <iostream>
#include <vector>

using namespace std;

int findMin(vector<int> &v)
{
    int min = 100;
    int ind = -1;
    for (int i = 0; i < v.size(); i ++)
    {
        if (min > v[i])
        {
            min = v[i];
            ind = i;
        }
    }
    return ind;
}


int solve(vector<int> &v, int N, int M)
{
    if (N == 1 || M == 1)
        return 1;

    int ind = findMin(v);
    if (ind == -1)
        return 1;

    int val = v[ind];
    // check row and columns
    int r = 1;
    int c = 1;
    int rowNum = ind/M;
    int colNum = ind%M;
    // row
    for (int i = rowNum*M; i < rowNum*M+M; i++)
    {
        if (v[i] != val && v[i] != 101)
        {
            r = 0;
            break;
        }
    }
    for (int i = colNum; i < N*M; i += M)
    {
        if (v[i] != val && v[i] != 101)
        {
            c = 0;
            break;
        }
    }

    if (!r && !c)
        return 0;

    if (r == 1)
    {
        for (int i = rowNum*M; i < rowNum*M+M; i++)
            v[i] = 101;
    }
    if (c == 1)
    {
        for (int i = colNum; i < N*M; i += M)
            v[i] = 101;
    }
    return solve(v, N, M);

}



int main(void)
{
    int n;
    cin >> n;

    int N;
    int M;
    for (int i = 0; i < n; i++)
    {
        vector<int> lawn;
        cin >> N;
        cin >> M;
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                int tmp;
                cin >> tmp;
                lawn.push_back(tmp);
            }
        }
        if (solve(lawn, N, M))
            cout << "Case #" << i+1 << ": YES" << endl;
        else
            cout << "Case #" << i+1 << ": NO" << endl;
    }

    return 0;
}
