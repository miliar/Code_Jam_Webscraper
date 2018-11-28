#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;
const char* fi = "A-small-attempt2.in";
const char* fo = "a.out";
const int maxn = 1000010;

long long SolveSmall(string str, int n);
long long SolveLarge(string str);
bool IsConsonant(char ch);

string s;
int n;

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);

    int nTest;
    cin >> nTest;

    for (int i=1; i<=nTest; i++)
    {
        cin >> s >> n;

        long long result = SolveSmall(s,n);

        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}

bool IsConsonant(char ch)
{
    return (ch!='a' && ch!='u' && ch!='e' && ch!='i' && ch!='o');
}

long long SolveSmall(string str, int n)
{
    long long result = 0;

    for (unsigned int i=0; i<str.length(); i++)
        for (unsigned int j=i; j<str.length(); j++)
        {
            int cnt = 0;
            for (unsigned int k=i; k<=j; k++)
            {
                if (IsConsonant(str[k])) cnt++;
                else cnt = 0;

                if (cnt>=n) { result++; break; }
            }
        }

    return result;
}
