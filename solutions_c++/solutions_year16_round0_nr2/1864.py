#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int Max = 0;

int main()
{
    ifstream in;
    in.open("B.in");
    ofstream out;
    out.open("B.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i)
    {
        string a;
        in >> a;
        out << "Case #" << i + 1 << ": ";
        vector <int> A;
        for (int i = 0; i < a.size(); ++i)
        {
            if (i == 0 || a[i - 1] != a[i])
            {
                if (a[i] == '+')
                {
                    A.push_back(1);
                }
                else
                {
                    A.push_back(-1);
                }
            }
        }
        if (A[A.size() - 1] == 1)
        {
            out << A.size() - 1 << endl;
        }
        else
        {
            out << A.size() << endl;
        }
    }
    out.close();
    in.close();
    return 0;
}
