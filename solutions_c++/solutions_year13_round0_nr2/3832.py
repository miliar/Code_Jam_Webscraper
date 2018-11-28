#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>

using namespace std;

void printH(vector<vector<int> > &lawn)
{
    int N = lawn.size();
    int M = lawn[0].size();

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            cout << lawn[i][j] << " ";
        }
        cout << endl;
    }
}

bool findH(const vector<vector<int> > &lawn, int value, int &ii, int &jj)
{
    int N = lawn.size();
    int M = lawn[0].size();

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (lawn[i][j] == value)
            {
                ii = i;
                jj = j;
                return true;
            }
        }
    }
    return false;
}

vector<int> createHList(const vector<vector<int> > &lawn)
{
    int N = lawn.size();
    int M = lawn[0].size();

    set<int> hSet;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            hSet.insert(lawn[i][j]);
        }
    }
    vector<int> hList(hSet.begin(), hSet.end());
    sort(hList.begin(), hList.end());
    return hList;
}

bool checkH(vector<vector<int> > &lawn, int ii, int jj)
{
    int N = lawn.size();
    int M = lawn[0].size();

    bool flagH = true;
    for (int i = 0; i < N; ++i)
    {
        if (lawn[i][jj] != lawn[ii][jj] && lawn[i][jj] != 0)
        {
            flagH = false;
            break;
        }
    }

    if (flagH)
    {
        for (int i = 0; i < N; ++i)
        {
            lawn[i][jj] = 0;
        }
        return flagH;
    }

    bool flagV = true;
    for (int j = 0; j < M; ++j)
    {
        if (lawn[ii][j] != lawn[ii][jj] && lawn[ii][j] != 0)
        {
            flagV = false;
            break;
        }
    }

    if (flagV)
    {
        for (int j = 0; j < M; ++j)
        {
            lawn[ii][j] = 0;
        }
    }

    return flagH || flagV;
}

void replaceH(vector<vector<int> > &lawn, int replace)
{
    int N = lawn.size();
    int M = lawn[0].size();

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (lawn[i][j] == 0)
                lawn[i][j] = replace;
}

string process(vector<vector<int> > &lawn)
{
    int N = lawn.size();
    int M = lawn[0].size();

    if (N == 1 || M == 1)
        return "YES";

    vector<int> hList = createHList(lawn);

    for (size_t i = 0; i < hList.size() - 1; ++i)
    {
        int ii;
        int jj;
        while (findH(lawn, hList[i], ii, jj))
        {
            if (!checkH(lawn, ii, jj))
                return "NO";
        }
        replaceH(lawn, hList[i + 1]);
    }

    return "YES";
}

int main(int argc, char **argv)
{
    ifstream ifs(argv[1]);

    int count;
    ifs >> count;

    for (int k = 0; k < count; k++)
    {
        int N;
        ifs >> N;
        int M;
        ifs >> M;

        vector<vector<int> > lawn(N);

        for (int i = 0; i < N; i++)
        {
            lawn[i].resize(M);
            for (int j = 0; j < M; j++)
            {
                ifs >> lawn[i][j];
            }
        }

        cout << "Case #" << k + 1 << ": " << process(lawn) << endl;
    }
    return 0;
}
