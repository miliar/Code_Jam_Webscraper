#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> inputTest(ifstream& in)
{
    vector<vector<int>> res;

    int n, m;
    in >> n >> m;
    for (int i = 0; i < n; ++i)
    {
        res.push_back(vector<int>(m, 0));
        for (int j = 0; j < m; ++j)
        {
            in >> res[i][j];
        }
    }

    return res;
}

string processTest(vector<vector<int>> test)
{
    int n = test.size();
    int m = test[0].size();

    for (int h = 100; h > 0; --h)
    {
        vector<vector<int>> testTmp = test;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (test[i][j] == h)
                {
                    bool isH = true;
                    bool isW = true;
                    for (int ii = 0; ii < n; ++ii)
                        if (test[ii][j] == -1)
                        {
                            isH = false;
                            break;
                        }

                    for (int jj = 0; jj < m; ++jj)
                        if (test[i][jj] == -1)
                        {
                            isW = false;
                            break;
                        }


                    if (!isH && !isW)
                        return "NO";

                    testTmp[i][j] = -1;
                }
            }
        }

        test = testTmp;
    }

    return "YES";
}

void outputTest(ofstream& out, int t, const string& res)
{
    out << "Case #" << t + 1 << ": " << res << endl;
}

int main()
{
    ifstream in("input.txt");
    if (!in.is_open())
        return 1;

    ofstream out("ouput.txt");
    if (!out.is_open())
        return 1;

    int testCases;
    in >> testCases;

    for (int t = 0; t < testCases; ++t)
    {
        vector<vector<int>> test;
        test = inputTest(in);
        string res = processTest(test);
        outputTest(out, t, res);
    }

	return 0;
}

