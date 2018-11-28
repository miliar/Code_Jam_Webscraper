#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    int t;
    fin >> t;
    for (int x = 0; x < t; ++x)
    {
        int n;
        fin >> n;
        bool used[10];
        fill(used, used + 10, false);
        int cnt = 0;
        if (n == 0)
            fout << "Case #" << x + 1 << ": INSOMNIA" << endl;
        else
        {
            int n2;
            for (n2 = n; cnt < 10; n2 += n)
            {
                for (int n3 = n2; n3 > 0; n3 /= 10)
                {
                    if (!used[n3 % 10])
                    {
                        used[n3 % 10] = true;
                        ++cnt;
                    }
                }
            }
            fout << "Case #" << x + 1 << ": " << n2 - n << endl;
        }
    }
    fin.close();
    fout.close();
	return 0;
}

