#include <bits/stdc++.h>
using namespace std;

int num[12];
int alpha[27];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output11.txt", "w", stdout);

    int T;
    cin >> T;

    for(int test=1; test<=T; test++)
    {
        string S;
        cin >> S;

        memset(num, 0, sizeof(num));
        memset(alpha, 0, sizeof(alpha));

        for(int i=0; i<S.size(); i++)
            alpha[S[i]-'A']++;

        while(alpha['Z'-'A'])
        {
            alpha['Z'-'A']--;
            alpha['E'-'A']--;
            alpha['R'-'A']--;
            alpha['O'-'A']--;
            num[0]++;
        }

        while(alpha['W'-'A'])
        {
            alpha['T'-'A']--;
            alpha['W'-'A']--;
            alpha['O'-'A']--;
            num[2]++;
        }

        while(alpha['X'-'A'])
        {
            alpha['S'-'A']--;
            alpha['I'-'A']--;
            alpha['X'-'A']--;
            num[6]++;
        }

        while(alpha['U'-'A'])
        {
            alpha['F'-'A']--;
            alpha['O'-'A']--;
            alpha['U'-'A']--;
            alpha['R'-'A']--;
            num[4]++;
        }

        while(alpha['G'-'A'])
        {
            alpha['E'-'A']--;
            alpha['I'-'A']--;
            alpha['G'-'A']--;
            alpha['H'-'A']--;
            alpha['T'-'A']--;
            num[8]++;
        }

        while(alpha['F'-'A'])
        {
            alpha['F'-'A']--;
            alpha['I'-'A']--;
            alpha['V'-'A']--;
            alpha['E'-'A']--;
            num[5]++;
        }

        while(alpha['V'-'A'])
        {
            alpha['S'-'A']--;
            alpha['E'-'A']--;
            alpha['V'-'A']--;
            alpha['E'-'A']--;
            alpha['N'-'A']--;
            num[7]++;
        }

        while(alpha['H'-'A'])
        {
            alpha['T'-'A']--;
            alpha['H'-'A']--;
            alpha['R'-'A']--;
            alpha['E'-'A']--;
            alpha['E'-'A']--;
            num[3]++;
        }

        while(alpha['I'-'A'])
        {
            alpha['N'-'A']--;
            alpha['I'-'A']--;
            alpha['N'-'A']--;
            alpha['E'-'A']--;
            num[9]++;
        }

        while(alpha['O'-'A'])
        {
            alpha['O'-'A']--;
            alpha['N'-'A']--;
            alpha['E'-'A']--;
            num[1]++;
        }

        printf("Case #%d: ", test);

        for(int i=0; i<10; i++)
        {
            while(num[i])
            {
                num[i]--;
                cout << i;
            }
        }

        cout << endl;
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
