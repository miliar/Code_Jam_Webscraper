#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int fr[1010];
int main()
{
    int T, Smax;
    string s;
    ifstream g("ceva.in");
    int i, j;
    g>>T;
    ofstream f("standingovation.out");

    for (j = 1; j <= T; j++)
    {
        g>>Smax;
        g>>s;
        fr[0] = s[0] - '0';
        for (i = 1; i <= Smax; i++)
            fr[i] = fr[i - 1] + s[i] - '0';
        int answer = 0;
        for (i = 1; i <= Smax; i++)
            if (fr[i - 1] + answer < i) answer = i - fr[i - 1];
        f<<"Case #"<<j<<": "<<answer<<endl;
        for (i = 0; i <= Smax; i++)
            fr[i] = 0;
    }

}
