#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int letters[26],n,digits[10],k,T;
    string s;
    cin>>T;
    for (int test = 1;test<=T;test++)
    {

        cin>>s;
        n = s.length();
        memset(letters,0,sizeof(letters));
        memset(digits,0,sizeof(digits));
        for (int i=0;i<n;i++) letters[s[i]-'A']++;
        k = letters['Z'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['Z'-'A']--;
            letters['E'-'A']--;
            letters['R'-'A']--;
            letters['O'-'A']--;
            digits[0]++;
        }

        k = letters['W'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['T'-'A']--;
            letters['W'-'A']--;
            letters['O'-'A']--;
            digits[2]++;
        }

        k = letters['U'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['F'-'A']--;
            letters['O'-'A']--;
            letters['U'-'A']--;
            letters['R'-'A']--;
            digits[4]++;
        }

        k = letters['X'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['S'-'A']--;
            letters['I'-'A']--;
            letters['X'-'A']--;
            digits[6]++;
        }

        k = letters['G'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['E'-'A']--;
            letters['I'-'A']--;
            letters['G'-'A']--;
            letters['H'-'A']--;
            letters['T'-'A']--;
            digits[8]++;
        }

        k = letters['O'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['O'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;
            digits[1]++;
        }

        k = letters['T'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['T'-'A']--;
            letters['H'-'A']--;
            letters['R'-'A']--;
            letters['E'-'A']--;
            letters['E'-'A']--;
            digits[3]++;
        }

        k = letters['F'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['F'-'A']--;
            letters['I'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
            digits[5]++;
        }

        k = letters['S'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['S'-'A']--;
            letters['E'-'A']--;
            letters['V'-'A']--;
            letters['E'-'A']--;
            letters['N'-'A']--;
            digits[7]++;
        }

        k = letters['I'-'A'];
        for (int i=0;i<k;i++)
        {
            letters['N'-'A']--;
            letters['I'-'A']--;
            letters['N'-'A']--;
            letters['E'-'A']--;
            digits[9]++;
        }
        cout<<"Case #"<<test<<": ";
        for (int i=0;i<10;i++)
        {
            for (int j=0;j<digits[i];j++) cout<<i;
        }
        cout<<endl;
    }
    return 0;
}
