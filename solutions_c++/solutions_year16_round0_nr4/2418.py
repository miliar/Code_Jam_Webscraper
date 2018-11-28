#include <bits/stdc++.h>
using namespace std;

/// Prototypes
long long int power(long long int a, long long int b);

int main()
{
    ofstream outfile;
    ifstream inpfile;
    inpfile.open("D-small-attempt0.in");
    outfile.open("prob4.txt");
    long long int t, counter = 1;

    inpfile >> t;
    while (t > 0)
    {
        long long int k, c, s, temp = 1;
        inpfile >> k >> c >> s;

        outfile << "Case #" << counter << ": ";
        counter++;

        while (s > 0)
        {
            outfile << temp << " ";
            temp += power(k, c - 1);
            s--;
        }
        outfile << endl;
        t--;
    }

    outfile.close();
    inpfile.close();

    return 0;
}

long long int power(long long int a, long long int b)
{
    if (b == 0)
        return 1;

    long long int aa = a;
    for (int i = 1; i < b; i++)
        aa *= a;
    return aa;
}
