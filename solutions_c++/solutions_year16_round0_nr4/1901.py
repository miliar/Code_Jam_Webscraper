#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    ifstream fin("in.txt");
    ofstream fout("res.txt");
    fin >> t;
    for(int tc = 0; tc < t; tc ++)
    {
        int k, c, s;
        fin >> k >> c >> s;
        fout << "Case #"<<tc+1<<": ";
        for(int i = 1; i <= s; i++)
        {
            fout << i << " ";
        }
        fout << endl;
    }
    return 0;
}
