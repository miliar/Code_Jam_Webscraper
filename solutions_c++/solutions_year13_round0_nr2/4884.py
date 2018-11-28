
#include <cstdio>
#include <vector>
using namespace std;

vector<int> getRow(int n, int m, int input[100][100], int row)
{
    vector<int> result(m);
    for (int i = 0; i < m; i++)
    {
        result[i] = input[row][i];
    }
    return result;
}

vector<int> getColumn(int n, int m, int input[100][100], int column)
{
    vector<int> result(n);
    for (int i = 0; i < n; i++)
    {
        result[i] = input[i][column];
    }
    return result;
}

void setRow(int n, int m, int input[100][100], int row)
{
    for (int i = 0; i < m; i++)
    {
        input[row][i] = -1;
    }
}

void setColumn(int n, int m, int input[100][100], int column)
{
    for (int i = 0; i < n; i++)
    {
        input[i][column] = -1;
    }
}

int getMono(vector<int> &v)
{
    int first;
    bool completed = true;
    for (auto it = v.cbegin(); it != v.cend(); ++it)
    {
        if (*it < 0 == false)
        {
            first = *it;
            completed = false;
            break;
        }
    }

    if (completed)
    {
        return -1;
    }

    for (auto it = v.cbegin(); it != v.cend(); ++it)
    {
        if (*it >= 0 && *it != first)
        {
            return -1;
        }
    }
    return first;
}

int getMin(int n, int m, int input[100][100])
{
    int result = INT_MAX;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (input[i][j] >= 0)
            {
                result = std::min(result, input[i][j]);
            }
        }
    }

    return result;
}

void print(int n, int m, int input[100][100])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", input[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

bool testCase(int n, int m, int input[100][100])
{
    do
    {
        // print(n, m, input);

        int arrMin = getMin(n, m, input);

        bool ed = false;

        for (int i = 0; i < n && !ed; i++)
        {
            if (getMono(getRow(n, m, input, i)) == arrMin)
            {
                ed = true;
                setRow(n, m, input, i);
                break;
            }
        }

        for (int i = 0; i < m && !ed; i++)
        {
            if (getMono(getColumn(n, m, input, i)) == arrMin)
            {
                ed = true;
                setColumn(n, m, input, i);
                break;
            }
        }

        if (!ed)
        {
            bool complete = true;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (input[i][j] < 0 == false)
                    {
                        complete = false;
                        break;
                    }
                }
            }

            if (complete)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

    } while (true);
}

int main()
{
    FILE *file_in = fopen("input.txt", "rt"),
        *file_out = fopen("output.txt", "wt");

    int t;
    fscanf(file_in, "%d", &t);

    for (int c = 1; c <= t; c++)
    {
        int n, m;
        fscanf(file_in, "%d%d", &n, &m);

        int input[100][100];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                fscanf(file_in, "%d", &input[i][j]);
            }
        }

        auto result = testCase(n, m, input);
        fprintf(file_out, "Case #%d: %s\n", c, result ? "YES" : "NO");
    }

    return 0;
}
