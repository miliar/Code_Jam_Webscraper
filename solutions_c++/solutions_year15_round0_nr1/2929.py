#include <fstream>
#include <iostream>

using namespace std;

int main()
{
        ifstream fin("A-large.in");
        ofstream fout("A-large.out");
        int t;
        fin >> t;
        for (int T = 1; T <= t; ++T)
        {
                int ms;
                fin >> ms;
                string shy;
                fin >> shy;
                int a[ms];
                for (int j = 0; j <= ms; ++j)
                {
                        a[j] = shy[j] - '0';
                        cout << a[j] << " ";
                }
                cout << endl;
                int n = 0, standing = 0;
                for (int j = 0; j <= ms; ++j)
                {
                        cout << j << " " << standing << " " << n << endl;
                        if (standing < j)
                        {
                                int temp = (j - standing);
                                n += (j - standing);
                                standing += temp;
                        }
                        standing += a[j];
                }
                cout << endl;
                fout << "Case #" << T << ": " << n << endl;
        }
}
