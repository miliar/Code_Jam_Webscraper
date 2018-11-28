#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> pols;
vector<string> sqar;

void generatePolinromeFromOne(vector<int> cur, int i, int oneCount, vector<vector<int>>& res, const int& maxLenght, const bool& even)
{
    if (i > maxLenght)
        return;

    if (oneCount > 4)
        return;

    if (i == maxLenght)
    {
        int leng = 2 + maxLenght * 2;
        if (!even)
            --leng;

        vector<int> t(leng);
        t[0] = 1;
        t[leng - 1] = 1;
        for (int i = 0; i < maxLenght; ++i)
        {
            t[i + 1] = cur[i];
            t[leng - 2 - i] = cur[i];
        }

        int sum = 0;
        for (auto& x: t)
        {
            sum+=x;
        }

        if (sum < 10)
            res.push_back(t);

        return;
    }

    cur[i] = 0;
    generatePolinromeFromOne(cur, i + 1, oneCount, res, maxLenght, even);

    cur[i] = 1;
    generatePolinromeFromOne(cur, i + 1, oneCount + 1, res, maxLenght, even);
}

void generatePolindrome(int l, vector<vector<int>>& res)
{
    vector<int> cur;

    if (l == 1)
    {
        cur = vector<int>(1, 1);
        res.push_back(cur);

        cur = vector<int>(1, 2);
        res.push_back(cur);

        cur = vector<int>(1, 3);
        res.push_back(cur);
    }
    else
    {
        cur = vector<int>(((l - 2) + 1) / 2, 0);
        generatePolinromeFromOne(cur, 0, 0, res, ((l - 2) + 1) / 2, (l - 2) % 2 == 0);

        if (l % 2 != 0)
        {
            cur = vector<int>(l, 0);
            cur[0] = 1; cur[l - 1] = 1;
            cur[(l - 1) / 2] = 2;
            res.push_back(cur);
        }

        cur = vector<int>(l, 0);
        cur[0] = 2; cur[l - 1] = 2;
        res.push_back(cur);

        if (l % 2 != 0)
        {
            cur = vector<int>(l, 0);
            cur[0] = 2; cur[l - 1] = 2;
            cur[(l - 1) / 2] = 1;
            res.push_back(cur);
        }
    }
}

vector<string> calculateSquares(const vector<vector<int>>& pols)
{
    vector<string> res;

    for(auto& pol: pols)
    {
        vector<int> s;
        for (int i = 0; i < pol.size(); ++i)
        {
            s.push_back(0);

            for (int j = 0; j <= i; ++j)
            {
                s[i] += pol[j] * pol[i - j];
            }
        }

        for (int i  = s.size() - 2; i >= 0; --i)
            s.push_back(s[i]);

        string str;
        for (int i = 0; i < s.size(); ++i)
        {
            char buf[100];
            str.push_back(itoa(s[i], buf, 10)[0]);
        }

        res.push_back(str);
    }

    return res;
}

pair<string, string> inputTest(ifstream& in)
{
    pair<string, string> res;

    in >> res.first >> res.second;

    return res;
}

int processTest(pair<string, string> test)
{
    int answ = 0;

    for(auto& x: sqar)
    {
        if (((x.size() == test.first.size() && x >= test.first) || x.size() > test.first.size()) &&
            ((x.size() == test.second.size() && x <= test.second) || x.size() < test.second.size()))
            ++answ;
    }

    return answ;
}

void outputTest(ofstream& out, int t, int res)
{
    out << "Case #" << t + 1 << ": " << res << endl;
}

bool isPolindrome(__int64 n)
{
    vector<int> num;
    while (n > 0)
    {
        num.push_back(n % 10);
        n /= 10;
    }

    for (int i = 0; i < num.size() / 2; ++i)
        if (num[i] != num[num.size() - 1 - i])
            return false;

    return true;
}

int main()
{
//     int count = 0;
//     for (int i = 1; i <= 50000000; ++ i)
//     {
//         if (isPolindrome(i))
//         {
//             int j = sqrt((double)i);
//             if (j * j == i && isPolindrome(j))
//             {
//                 cout << i << endl;
//                 ++count;
//             }
//         }
//     }
//     cout << endl;
//     cout << count;
//     return 0;

    for (int l = 1; l <= 50; ++l)
    {
        generatePolindrome(l, pols);
    }

    sqar = calculateSquares(pols);

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
        pair<string, string> test;
        test = inputTest(in);
        int res = processTest(test);
        outputTest(out, t, res);
    }

    return 0;
}

