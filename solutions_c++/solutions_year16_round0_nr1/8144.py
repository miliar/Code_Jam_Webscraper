#include <fstream>
using namespace std;

ifstream fi ("data.in");
ofstream fo ("data.out");

bool M[10];
int n, cnt, n_test;

void mark (int k)
{
    while (k)
    {
        if (M[k % 10]) --cnt, M[k % 10] = false;
        k /= 10;
    }
}

int main ()
{
    fi >> n_test;
    for (int i = 1; i <= n_test; ++i)
    {
        fo << "Case #" << i << ": ";

        fi >> n;
        if (n == 0) { fo << "INSOMNIA\n"; continue; }

        int k = 0;
        cnt = 10;
        fill_n(M, 10, true);

        while (true)
        {
            k += n;
            mark(k);
            if (cnt == 0) break;
        }

        fo << k << "\n";
    }
}
