#include <fstream>
#include <cstring>

const int LMAX = 10005;

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int T,Smax,l,N,it;
int answer,contor;
char s[LMAX];

int main()
{
    f >> T;
    f.getline(s,123);
    for (int t = 1; t <= T; ++t)
    {
        f.getline(s,1234);
        l = strlen(s);
        it = 0;
        Smax = 0;
        answer = 0;
        contor = 0;
        while (s[it] >= '0' && s[it] <= '9')
        {
            Smax = Smax*10 + int(s[it] - '0');
            it++;
        }
        it++;
        for (int i = 0; i <= Smax; ++i)
        {
            if (contor < i)
            {
                answer += i - contor;
                contor += i - contor;
            }
            contor += int(s[i+it]-'0');
        }
        g << "Case #" << t << ": " << answer << '\n';
    }

    f.close();
    g.close();
    return 0;
}
