#include <iostream>
#include <fstream>

using namespace std;


    std::ifstream fin("input1.in");
    std::ofstream fout("output1.out");

int main()
{
    bool a [110];
    int num, n, k, i, j, ans;
    bool t;
    string s;

    fin >> num;
    for (i=0; i<num; i++)
    {
        bool exit = false;
        ans = 0;
        fin >> s;
        int l = s.size();
        for (j=0; j<100; j++) a[j] = true;
        for (j=0; j<l; j++)
        {
            if (s[j]=='+') a[j] = true; else a[j] = false;
        }
        // k - the first plus;
        ans = 0;
        while (2>1) {
        for (j=l-1; j>=0; j--) if (a[j]==false)
        {
            k = j + 1;
            break;
        }
        else
        {
            if ((j==0) && (a[j]==true))
            {
                fout << "Case #" << i + 1 << ": " << ans << endl;
                exit = true;
                break;
            }
        }
        if (exit==true) break;
        if ((a[0]==true) && (a[k-1]==false))
        {
            int z = 0;
            while (2>1)
            {
                if (a[z]==true)
                {
                    a[z] = false;
                    z++;
                }
                else break;
            }
            ans++;
        }

        if ((a[0]==false) && (a[k-1]==false))
        {
            int kol;
            kol = (k-1) / 2;
            for (j=0; j<=kol; j++)
            {
                t = a[j];
                a[j] = !a[k-j-1];
                a[k-j-1] = !t;
            }
            ans++;
        }
        }
    }
    return 0;
}
