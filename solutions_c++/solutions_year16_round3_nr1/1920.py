#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    int t;
    in >> t;
    for (int k = 1; k <= t; ++k)
    {
        int n;
        in >> n;
        vector <int> P(n);
        int f = 0;
        for (int i = 0; i < n; ++i)
        {
            in >> P[i];
            if (P[i] > 0)
            {
                ++f;
            }
        }
        out << "Case #" << k << ": ";
        auto it = max_element(P.begin(), P.end());
        int b = *it;
        while(b > 0)
        {
                for (int j = 0; j < n; ++j)
                {
                    if (f == 2 && *(max_element(P.begin(), P.end())) > 0)
                    {
                        int ind1 = 0, ind2 = 0;
                        for (int j = 0; j < n; ++j)
                        {
                            if (P[j] > 0)
                            {
                                ind2 = ind1;
                                ind1 = j;
                            }
                        }
                        if (P[ind2] == P[ind1])
                        {
                            char a = 'A' + ind2;
                            out << a;
                            --P[ind2];
                            a = 'A' + ind1;
                            out << a << " ";
                            --P[ind1];
                        }
                        else if (P[ind2] > P[ind1])
                        {
                            char a = 'A' + ind2;
                            out << a << " ";
                            --P[ind2];
                        }
                        else
                        {
                            char a = 'A' + ind1;
                            out << a << " ";
                            --P[ind1];
                        }
                    }
                    else if (P[j] == b)
                    {
                        char a = 'A' + j;
                        out << a << " ";
                        --P[j];
                        if (P[j] == 0)
                        {
                            --f;
                        }
                    }
                }
            it = max_element(P.begin(), P.end());
            b = *it;
       }
       out << endl;
    }
    in.close();
    out.close();
    return 0;
}
