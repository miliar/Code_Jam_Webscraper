#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string sum(const string& str, const string& cur)
{
    // sum of two numbers
    int i = 0; // str
    string res(cur.size() + 1, '0');
    while (true)
    {
        int sum = (str[i] - '0') + (cur[i] - '0');
        if (res[i] != '0')
            sum++;

        if (sum < 10)
        {
            res[i] = ('0' + sum);
        }
        else
        {
            res[i] = ('0' + sum - 10);
            res[i + 1] = ('1');
        }
        i++;

        if (i == str.size())
        {
            for (;i < cur.size(); ++i)
            {
                int sum = (cur[i] - '0');
                if (res[i] != '0')
                    sum++;

                if (sum < 10)
                {
                    res[i] = ('0' + sum);
                }
                else
                {
                    res[i] = ('0' + sum - 10);
                    res[i + 1] = ('1');
                }
            }
            break;
        }
    }

    i = res.size() - 1; // res
    while (res[i] == '0')
    {
        res.pop_back();
    }
    return res;
}

string solve(int N)
{
    if (N == 0)
        return "INSOMNIA";

    string str = std::to_string(N);
    std::reverse(str.begin(), str.end());
    vector<int> numbers(10);
    string cur = str;

    while (true)
    {
        for (int i = 0; i < cur.size(); ++i)
        {
            numbers[cur[i] - '0'] = 1;
        }

        bool quit = true;
        for (int i = 0; i < 10; ++i)
        {
            quit = quit && numbers[i] == 1;
        }
        if (quit)
            break;
        cur = sum(str, cur);
    }

    std::reverse(cur.begin(), cur.end());
    return cur;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");

    int T;

    in >> T;

    for (int i = 1; i <= T; ++i)
    {
        int N;
        in >> N;

        out << "Case #" << i << ": " << solve(N) << endl;
    }

    // cout << sum("1", "1") << endl;
    // cout << sum("1", "2") << endl;
    // cout << sum("1", "3") << endl;
    // cout << sum("1", "9") << endl;
    // cout << sum("2", "89") << endl;

    return 0;
}