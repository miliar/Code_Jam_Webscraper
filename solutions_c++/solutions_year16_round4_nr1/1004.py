#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie (NULL);
    cout.precision(10);
    cout << fixed;

    int test_count;
    cin >> test_count;
    for (int test = 1; test <= test_count; test++)
    {
        int N;
        cin >> N;
        int R, P, S;
        cin >> R >> P >> S;
    
        string solution = "";
        vector<string> v;
        if (N % 2)
        {
            v = vector<string>{"PR", "PS", "RS"};
        }
        else
        {
            v = vector<string>{"PRPS", "PRRS", "PSRS"};
        }

        for (auto tmp : v) {
            int n = N;
            if (N % 2)
                n -= 1;
            else
                n -= 2;


            while (n)
            {
                string tmp2 = "";
                for (char c : tmp) {
                    if (c == 'P')
                        tmp2 += "PRRS";
                    if (c == 'S')
                        tmp2 += "PRPS";
                    if (c == 'R')
                        tmp2 += "PSRS";
                }
                tmp = tmp2;
                n -= 2;
            }

            int p = 0;
            int r = 0;
            int s = 0;

            for (char c : tmp) {
                if (c == 'P')
                    p++;
                if (c == 'S')
                    s++;
                if (c == 'R')
                    r++;
            }
            
            if (p == P && r == R && s == S)
            {
                // sort
                int size = 4;
                while (size < (1 << N))
                {
                    string res = "";
                    for (int start = 0; start < tmp.size(); start += 2*size)
                    {
                        string s1 = tmp.substr(start, size);
                        string s2 = tmp.substr(start + size, size);
                        if (s1 < s2)
                        {
                            res += s1;
                            res += s2;
                        }
                        else
                        {
                            res += s2;
                            res += s1;
                        }
                    }
                    size *= 2;
                    tmp = res;
                }
                
                if (solution == "")
                {
                    solution = tmp;
                }
                else
                {
                    solution = min(solution, tmp);
                }
            }
        }

        if (solution.size() == 0)
            solution = "IMPOSSIBLE";

        int result = 0;
        cout << "Case #" << test << ": " << solution << endl;
    }

    return 0;
}
