#include <bits/stdc++.h>


std::ifstream in("D-large.in");
std::ofstream out("output.txt");


int main()
{
    int T;
    in >> T;
    for (int t = 1; t <= T; ++t)
    {
        out << "Case #" << t << ": ";
        int n;
        in >> n;
        std::vector <double> naomi(n), ken(n);
        for (int i = 0; i < n; ++i) in >> naomi[i];
        for (int i = 0; i < n; ++i) in >> ken[i];
        std::sort(naomi.begin(), naomi.end());
        std::sort(ken.begin(), ken.end());
        int w = 0, dw = 0;
        for (int i = 0, l = 0, r = n - 1; i < n; ++i)
        {
            int j = n - i - 1;
            if (naomi[j] < ken[r])
            {
                --r;
            }
            else
            {
                ++l;
                ++w;
            }
        }
        for (int i = 0, l = 0, r = n - 1; i < n; ++i)
        {
            int j = n - i - 1;
            if (naomi[r] > ken[j])
            {
                ++dw;
                --r;
            }
            else
            {
                ++l;
            }
        }
        out << dw << " " << w << "\n";
    }
}
