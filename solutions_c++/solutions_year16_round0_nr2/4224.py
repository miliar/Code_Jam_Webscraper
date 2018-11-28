#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;

void flip(char s[], int n)
{
    for (int i = 0; i < n; i++)
        s[i] = (s[i] == '+') ? '-' : '+';
    for (int i = 0; i < n/2; i++)
        swap(s[i], s[n - i - 1]);
}

bool ok(char s[], int len)
{
    for (int i = 0; i < len; i++)
        if (s[i] == '-')
            return false;
    return true;
}


int main()
{
    int T, N;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in >> T;
    for (int i = 0; i < T; i++)
    {
        char s[101];
        in >> s;
        int len = strlen(s);

        int res = 0;
        while (!ok(s, len))
        {
            int idx = 0;
            while (idx < len - 1 && s[idx] == s[idx + 1])
                idx++;
            flip(s, idx + 1);
            res++;
        }
        out << "Case #" << i + 1 << ": " << res << endl;
    }
}
