#include<bits/stdc++.h>

#define MOD 1000000007
#define MODSET(d) if ((d) >= MOD) d %= MOD;

using namespace std;

bool isSelected[200];
vector< vector<int> > remaining, transpose;
int t, n;
bool hasDone = false;

void brute(int index)
{
    if (hasDone)
        return;

    if (index == 0)
    {
        vector< vector<int> > matrix(n);

        int cnt = 0;
        int done = 0;
        for (auto s: remaining)
        {
            if (isSelected[cnt])
            {
                matrix[done] = s;
                done++;
            }
            cnt++;
        }

        for (int i = 0; i < n; i++)
        {
            bool print = true;

            cnt = 0;
            for (auto s: remaining)
            {
                if (!isSelected[cnt])
                {
                    bool isEqual = true;

                    for (int j = 0; j < n; j++)
                    {
                        if (s[j] != matrix[j][i])
                        {
                            isEqual = false;
                            break;
                        }
                    }

                    if (isEqual)
                    {
                        print = false;
                        break;
                    }
                }
                cnt++;
            }

            if (print)
            {
                cout << "Case #" << t << ":";
                for (int j = 0; j < n; j++)
                {
                    cout << " " << matrix[j][i];
                }
                cout << "\n";
                hasDone = true;
            }
        }

    }
    else
    {
        for (int i = remaining.size()-1; i >= 0; i--)
        {
            if (!isSelected[i])
            {
                isSelected[i] = true;

                for (int j = 0; j < n; j++)
                {
                    transpose[j][index - 1] = remaining[i][j];
                }

                int matches = 0;
                for (int j = 0; j < n; j++)
                {
                    for (int k = remaining.size()-1; k >= 0; k--)
                    {
                        if (!isSelected[k])
                        {
                            bool isEqual = true;

                            for (int l = index - 1; l < n; l++)
                            {
                                if (remaining[k][l] != transpose[j][l])
                                {
                                    isEqual = false;
                                    break;
                                }
                            }

                            if (isEqual)
                            {
                                matches++;
                                break;
                            }
                        }
                    }
                }

                if (matches >= n-1)
                {
                    brute(index - 1);
                }

                if (hasDone)
                    return;

                isSelected[i] = false;
            }
        }
    }
}

int main()
{
    #ifdef VSP4
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif // VSP4

    int T, i, j, k, curr;
    vector< vector<int> > lists;

    cin >> T;

    for (t = 1; t <= T; t++)
    {
        cin >> n;

        memset(isSelected, false, sizeof(isSelected));
        lists.assign(2*n - 1, vector<int>(n));
        transpose.assign(n, vector<int>(n));

        for (i = 0; i < 2*n - 1; i++)
        {
            for (j = 0; j < n; j++)
            {
                cin >> lists[i][j];
            }
            sort(lists[i].begin(), lists[i].end());
        }

        sort (lists.begin(), lists.end());

        remaining = lists;

        hasDone = false;

        brute(n);
    }

    return 0;
}
