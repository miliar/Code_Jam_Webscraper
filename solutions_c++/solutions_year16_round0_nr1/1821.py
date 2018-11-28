#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int Max = 0;

int main()
{
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("A-large.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i)
    {
        int a;
        in >> a;
        int f = a;
        out << "Case #" << i + 1 << ": ";
        if (a == 0)
        {
            out << "INSOMNIA" << endl;
        }
        else
        {
            int b = 0;
            vector <bool> A(10);
            while(b < 10)
            {
                int x = a;
                while (x > 0)
                {
                    int s = x % 10;
                    x /= 10;
                    if (!A[s])
                    {
                        A[s] = true;
                        ++b;
                    }
                }
                a += f;
            }
            out << a - f << endl;
        }
    }
    out.close();
    in.close();
    return 0;
}
