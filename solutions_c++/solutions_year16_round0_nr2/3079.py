#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream outfile;
    ifstream inpfile;
    inpfile.open("B-large.in");
    outfile.open("prob1.txt");
    long long int t, counter = 1;
    inpfile >> t;
    while (t > 0)
    {
        string s;
        inpfile >> s;
        long long int ans = 0, f = 0, n = s.length();
        while (1)
        {
            /// Checking if problem is solved
            f = 1;
            for (int i = 0; i < n; i++)
            {
                if (s[i] == '-')
                {
                    f = 0;
                    break;
                }
            }

            if (f == 1)
                break;

            /// Solving the problem
            if (s[0] == '-')
            {

                /// Determining pos
                int pos = n - 1;
                for (int i = n - 1; i >= 0; i--)
                {
                    if (s[i] == '-')
                    {
                        pos = i;
                        break;
                    }
                }

                /// Flip from the first to pos
                for (int k = 0; k <= pos; k++)
                {
                    if (s[k] == '+')
                        s[k] = '-';
                    else if (s[k] == '-')
                        s[k] = '+';
                }

                for (int j = 0; j < pos; j++)
                {
                    swap(s[j], s[pos]);
                    pos--;
                }
            }
            else
            {
                /// If we begin with a '+', switch all consecutive +s
                int pos = 0;
                for (int i = 1; i < n; i++)
                {
                    if (s[i] == '-')
                    {
                        pos = i - 1;
                        break;
                    }
                }

                /// Flip from the first to pos
                for (int k = 0; k <= pos; k++)
                {
                    if (s[k] == '+')
                        s[k] = '-';
                    else if (s[k] == '-')
                        s[k] = '+';
                }

                for (int j = 0; j < pos; j++)
                {
                    swap(s[j], s[pos]);
                    pos--;
                }
            }
            ans++;
        }
        outfile << "Case #" << counter << ": " << ans << endl;
        counter++;
        t--;
    }

    outfile.close();
    inpfile.close();
    return 0;
}
