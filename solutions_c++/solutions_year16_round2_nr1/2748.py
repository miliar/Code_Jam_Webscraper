#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int case_i, case_n;

int ca(char p)
{
    return p - 65;
}

int main()
{
    string s;
    int l;
    int a[200], ans[10];
    cin >> case_n;
    for (case_i = 1; case_i <= case_n; case_i++)
    {
        memset(ans, 0, sizeof(ans));
        memset(a, 0, sizeof(a));
        cin >> s;
        l = s.length();
        for(int i = 0; i<l; i++)
        {
            a[s[i]]++;
        }
        while (a['Z'] > 0)
        {
            a['Z']--;
            a['E']--;
            a['R']--;
            a['O']--;
            ans[0]++;
        }
        while (a['W'] > 0)
        {
            a['T']--;
            a['W']--;
            a['O']--;
            ans[2]++;
        }
        while (a['U'] > 0)
        {
            a['F']--;
            a['U']--;
            a['O']--;
            a['R']--;
            ans[4]++;
        }
        while (a['X'] > 0)
        {
            a['S']--;
            a['I']--;
            a['X']--;
            ans[6]++;
        }
        while (a['G'] > 0)
        {
            a['E']--;
            a['I']--;
            a['G']--;
            a['H']--;
            a['T']--;
            ans[8]++;
        }
        while (a['O'] > 0)
        {
            a['O']--;
            a['N']--;
            a['E']--;
            ans[1]++;
        }
        while (a['R'] > 0)
        {
            a['T']--;
            a['H']--;
            a['R']--;
            a['E']-=2;
            ans[3]++;
        }
        while (a['S'] > 0)
        {
            a['S']--;
            a['E']--;
            a['V']--;
            a['E']--;
            a['N']--;
            ans[7]++;
        }
        while (a['F'] > 0)
        {
            a['F']--;
            a['I']--;
            a['V']--;
            a['E']--;
            ans[5]++;
        }
        while (a['I'] > 0)
        {
            a['N']-=2;
            a['I']--;
            a['E']--;
            ans[9]++;
        }
        cout << "Case #" << case_i << ": ";
        for (int i=0; i<10; i++)
        {
            while (ans[i] > 0)
            {
                cout << i;
                ans[i]--;
            }
        }
       cout << endl;
    }

    return 0;
}
