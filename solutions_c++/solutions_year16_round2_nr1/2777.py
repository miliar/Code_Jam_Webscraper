#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int n;
    fin >> n;
    for (int i = 0; i < n; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        string s;
        fin >> s;
        int c[250] = {};
        for (int j = 0 ; j < s.length(); j++)
        {
            c[s[j] - 'A']++;
        }
        int ans[10] = {};
        for (int j = 0; j < c['Z' - 'A']; j++)
        {
            ans[0]++;
            c['E' - 'A']--;
            c['R' - 'A']--;
            c['O' - 'A']--;

        }
        int v = c['W' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[2]++;
            c['T' - 'A']--;
            c['O' - 'A']--;
            c['W' - 'A']--;

        }
        v = c['U' - 'A'];
        for (int j = 0; j < v ; j++)
        {
            ans[4]++;
            c['F' - 'A']--;
            c['R' - 'A']--;
            c['O' - 'A']--;
            c['U' - 'A'];

        }
        for (int j = 0; j < c['X' - 'A']; j++)
        {
            ans[6]++;
            c['S' - 'A']--;
            c['I' - 'A']--;

        }
        v = c['G' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[8]++;
            c['E' - 'A']--;
            c['I' - 'A']--;
            c['H' - 'A']--;
            c['T' - 'A']--;
            c['G' - 'A']--;

        }
        v = c['H' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[3]++;
            c['T' - 'A']--;
            c['H' - 'A']--;
            c['R' - 'A']--;
            c['E' - 'A']--;
            c['E' - 'A']--;

        }
        v = c['F' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[5]++;
            c['F' - 'A']--;
            c['I' - 'A']--;
            c['V' - 'A']--;
            c['E' - 'A']--;

        }
        v = c['S' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[7]++;
            c['S' - 'A']--;
            c['E' - 'A']--;
            c['V' - 'A']--;
            c['E' - 'A']--;
            c['N' - 'A']--;

        }
        v = c['I' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[9]++;
            c['N' - 'A']--;
            c['I' - 'A']--;
            c['N' - 'A']--;
            c['E' - 'A']--;

        }
        v = c['O' - 'A'];
        for (int j = 0; j < v; j++)
        {
            ans[1]++;
            c['O' - 'A']--;
            c['N' - 'A']--;
            c['E' - 'A']--;

        }
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < ans[i]; j++)
                fout << i;
        fout << "\n";
    }

    return 0;
}

