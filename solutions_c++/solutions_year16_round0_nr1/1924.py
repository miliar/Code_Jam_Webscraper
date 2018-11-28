#include <bits/stdc++.h>

using namespace std;

int main()
{
    ofstream fout("res.txt");
    unordered_set<int> s;
    ifstream fin("in.txt");
    int t;
    fin >> t;
    for(int o=0; o<t; o++)
    {
        cout << "Case #" << (o+1)<<": ";
        fout << "Case #" << (o+1)<<": ";
        s.clear();
        long long n;

        fin >> n;
        long long r = n;
        if(n == 0)
        {
            fout << "INSOMNIA" << endl;
            continue;
        }
        while(s.size() != 10)
        {
            long long nn = n;
            while(nn > 0)
            {
                s.insert(nn%10);
                nn/=10;
            }
            if(s.size() == 10)
            {
                fout << n << endl;
            }
            else
            {
                n += r;
            }
        }

    }
    return 0;
}
