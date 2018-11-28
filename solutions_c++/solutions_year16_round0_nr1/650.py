#include <fstream>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int T;
int N, X;
bool seen[10];
int total;

void reset()
{
    total = 0;
    for (int i=0; i<=9; i++)
        seen[i] = 0;
}

void add(int x)
{
    while (x > 0)
    {
        if (!seen[x%10])
        {
            total++;
            seen[x%10] = 1;
        }
        x /= 10;
    }
}

int main()
{
    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        f >> N;
        if (N == 0)
            g << "INSOMNIA\n";
        else
        {
            X = N;
            reset();
            add(X);
            while (total < 10)
            {
                X += N;
                add(X);
            }
            g << X << '\n';
        }
    }
    
    f.close();
    g.close();
    return 0;
}