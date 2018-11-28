#include <iostream>
using namespace std;

int main()
{
    int n_cases;
    cin >> n_cases;
    for(int c = 1; c <= n_cases; ++c)
    {
        long long int r;
        long long int ml;
        cin >> r;
        cin >> ml;

        long long int pntd = 0;
        long long int ls = 0;
        while(pntd <= ml)
        {
            pntd += 2*r + 4*(++ls) - 3;
        }

        cout << "Case #" << c << ": " << ls-1 << endl;
    }
    return 0;
}
