#include <iostream>
#include <fstream>
#define NMAX 1010

using namespace std;

int smax;
char s[1010];
fstream f("output.in",ios::in);
fstream g("output.out",ios::out);

void solve(int t)
{
    f>>smax;f.get();
    f.getline(s,NMAX);
    int sum = 0,sol = 0;
    for(int i = 0; i <= smax; ++i)
    {
        int x = (s[i] - '0');
        if (i == 0) sum += x;
        else if (sum >= i) sum += x;
            else
            {
                sol += (i-sum);
                sum = i;
                sum += x;
            }

    }
    g<<"Case #"<<t<<": "<<sol<<"\n";
}
int main()
{
    int T;
    f>>T;
    for(int t = 1; t <= T; ++t)
    {
        solve(t);
    }
    return 0;
}
