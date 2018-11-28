#include <fstream>
using namespace std;

ifstream fi ("B.in");
ofstream fo ("B.out");

string s;
int n_test;

int cal ()
{
    int k = 1, c = 0;
    for (int i = s.size() - 1; i >= 0; --i)
    if ((s[i] == '+') ^ k) k ^= 1, ++c;

    return c;
}

int main ()
{
    fi >> n_test;
    for (int i = 1; i <= n_test; ++i)
    {
        fo << "Case #" << i << ": ";

        fi >> s;
        fo << cal() << "\n";
    }
}
