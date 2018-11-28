#include<iostream>
#include<string>

using namespace std;

bool judge(int arr[], int n, int b)
{
    for (int i = 0; i < n; i++)
        if (arr[i] > b)
            return false;
    return true;
}

int main()
{
    int cs;
    int n;
    int mp[110][110];
    cin >> n;
    for (int cs = 1; cs <= n; cs++)
    {
        int N, M;
        cin >> N >> M;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> mp[i][j];

        int tmp0[110], tmp1[110];
        bool res = true;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                for (int k = 0; k < N; k++)
                    tmp0[k] = mp[k][j];

                for (int k = 0; k < M; k++)
                    tmp1[k] = mp[i][k];

                if (judge(tmp0, N, mp[i][j]) == false && judge(tmp1, M, mp[i][j]) == false)
                {
                    res = false;
                    break;
                }
            }
            if (res == false)
                break;
        }
        if (res)
            cout << "Case #" << cs << ": YES" << endl;
        else
            cout << "Case #" << cs << ": NO" << endl;
    }
    return 0;
}
