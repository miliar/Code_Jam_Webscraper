#include <fstream>

using namespace std;

int f(int n)
{
    bool seen[10] = {0};
    int ctr = 0, i;

    for (i = n; ctr != 10; i += n)
    {
        int temp = i;

        while (temp)
        {
            int cur = temp % 10;
            temp /= 10;

            if (!seen[cur])
            {
                seen[cur] = true;
                ++ctr;
            }

        }
    }

    return i - n;
}



int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t, n;

    in >> t;

    for (int i = 1; i <= t; ++i)
    {
        in >> n;

        if (n == 0)
            out << "Case #" << i << ": INSOMNIA\n";

        else
            out << "Case #" << i << ": " << f(n) << '\n';
    }

    return 0;
}
