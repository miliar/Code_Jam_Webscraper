#include<bits/stdc++.h>
using namespace std;
#define L long long
vector<L> v;
L M=1e9+7;
main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    int t;
    cin>>t;
    for(int k = 1;k <= t; k++)
    {
        string s;

        cin>>s;

        int a[26]={0};
        int c[10]={0};
        for(int i=0;i<s.length();i++)
        {
            a[s[i]-'A']++;
        }
        c[0] = a['Z' - 'A'];

        c[2] = a['W' - 'A'];

        c[4] = a['U' - 'A'];

        c[6] = a['X' - 'A'];

        c[8] = a['G' - 'A'];

        c[1] = a['O' - 'A'] - c[0] - c[2] - c[4];

        c[3] = a['T' - 'A'] - c[2] - c[8];

        c[5] = a['F' - 'A'] - c[4];

        c[7] = a['S' - 'A'] - c[6];

        c[9] = a['I' - 'A'] - c[8] - c[6] - c[5];


        cout<<"Case #"<<k<<": ";

        for(int i=0;i <= 9; i++)
        {
            while(c[i])
            {
                c[i]--;
                cout << i;
            }
        }
        cout << "\n";
    }
}
