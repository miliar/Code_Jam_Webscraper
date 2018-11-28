#include<bits/stdc++.h>
using namespace std;
#define ll long long

string s;
ll a[29];

int main()
{
    freopen("inp.in","r",stdin);
    freopen("opt.out","w",stdout);
    ll t,p,i;

    cin>>t;

    p = 1;
    while(p <= t)
    {
        for(i=0;i<=27;i++)
        {
            a[i] =0;
        }
        string n;
        cin>>s;
        for(i=0;i<s.length();i++)
        {
            a[s[i] - 'A']++;
        }
        while(a['Z' - 'A'] >=1 && a['E' - 'A'] >= 1 && a['R' - 'A'] >= 1 && a['O' - 'A'] >= 1)
        {
            n = n + '0';
            a['Z' - 'A']--;
            a['E' - 'A']--;
            a['R' - 'A']--;
            a['O' - 'A']--;
        }
        while(a['T' - 'A'] >=1 && a['W' - 'A'] >= 1 && a['O' - 'A'] >= 1 )
        {
            n = n + '2';
            a['T' - 'A']--;
            a['W' - 'A']--;
            a['O' - 'A']--;
        }
        while(a['F' - 'A'] >=1 && a['O' - 'A'] >= 1 && a['U' - 'A'] >= 1 && a['R' - 'A'] >= 1)
        {
            n = n + '4';
            a['F' - 'A']--;
            a['O' - 'A']--;
            a['U' - 'A']--;
            a['R' - 'A']--;
        }
        while(a['S' - 'A'] >=1 && a['I' - 'A'] >= 1 && a['X' - 'A'] >= 1 )
        {
            n = n + '6';
            a['S' - 'A']--;
            a['I' - 'A']--;
            a['X' - 'A']--;
        }
        while(a['E' - 'A'] >=1 && a['I' - 'A'] >= 1 && a['G' - 'A'] >= 1 && a['H' - 'A'] >= 1 && a['T' - 'A'] >= 1)
        {
            n = n + '8';
            a['E' - 'A']--;
            a['I' - 'A']--;
            a['G' - 'A']--;
            a['H' - 'A']--;
            a['T' - 'A']--;
        }
        while(a['O' - 'A'] >=1 && a['N' - 'A'] >= 1 && a['E' - 'A'] >= 1 )
        {
            n = n + '1';
            a['O' - 'A']--;
            a['N' - 'A']--;
            a['E' - 'A']--;
        }
        while(a['F' - 'A'] >=1 && a['I' - 'A'] >= 1 && a['V' - 'A'] >= 1 && a['E' - 'A'] >= 1)
        {
            n = n + '5';
            a['F' - 'A']--;
            a['I' - 'A']--;
            a['V' - 'A']--;
            a['E' - 'A']--;
        }


        while(a['T' - 'A'] >=1 && a['H' - 'A'] >= 1 && a['R' - 'A'] >= 1 && a['E' - 'A'] >= 2)
        {
            n = n + '3';
            a['T' - 'A']--;
            a['H' - 'A']--;
            a['R' - 'A']--;
            a['E' - 'A'] -= 2;
        }



        while(a['S' - 'A'] >=1 && a['E' - 'A'] >= 2 && a['V' - 'A'] >= 1 && a['N' - 'A'] >= 1)
        {
            n = n + '7';
            a['S' - 'A']--;
            a['E' - 'A'] -= 2;
            a['V' - 'A']--;
            a['N' - 'A']--;
        }

        while(a['N' - 'A'] >=2 && a['I' - 'A'] >= 1 && a['E' - 'A'] >= 1 )
        {
            n = n + '9';
            a['N' - 'A']--;
            a['I' - 'A']--;
            a['N' - 'A']--;
            a['E' - 'A']--;
        }

        sort(n.begin() , n.end() );
        cout<<"Case #"<<p<<": "<<n;
        cout<<endl;
        p++;
    }
    return 0;
}
