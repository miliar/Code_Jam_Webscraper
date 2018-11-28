#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a[26];
    int b[10];

    int t, i, j;

    string s;

    freopen("A-large.in","r", stdin);
    freopen("out.txt", "w", stdout);
cin>>t;
    i =0;
    while (i < t) {
        i++;

        cin>>s;

        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));

        for (j = 0; j < s.length(); j++) {
            a[s[j]-'A']++;
        }
//cout<<"--------- "<<a['o'-'a']<<endl;

        //zero
        if (a['z'-'a'] > 0) {
            b[0] = a['z'-'a'];
            //a['z'-'a']-= a['z'-'a'];
            a['e'-'a']-= a['z'-'a'];
            a['r'-'a']-= a['z'-'a'];
            a['o'-'a']-= a['z'-'a'];
        //cout<<"---"<<a['z'-'a']<<endl;
        }
        //two
        if (a['w'-'a'] > 0) {
                //cout<<"hello "<<a['w'-'a']<<endl;
            b[2] = a['w'-'a'];
            a['t'-'a']-= a['w'-'a'];
            a['o'-'a']-= a['w'-'a'];
        }
        //six
        if (a['x'-'a'] > 0) {
            b[6] = a['x'-'a'];
            a['s'-'a']-= a['x'-'a'];
            a['i'-'a']-= a['x'-'a'];
        }
        //seven
        if (a['s'-'a'] > 0) {
            b[7] = a['s'-'a'];

            a['e'-'a']-= a['s'-'a'];
            a['v'-'a']-= a['s'-'a'];
            a['e'-'a']-= a['s'-'a'];
            a['n'-'a']-= a['s'-'a'];
            a['s'-'a']-= a['s'-'a'];
        }
        //eight
        if (a['g'-'a'] > 0) {
            b[8] = a['g'-'a'];
            a['e'-'a']-= a['g'-'a'];
            a['i'-'a']-= a['g'-'a'];
            a['t'-'a']-= a['g'-'a'];
            a['h'-'a']-= a['g'-'a'];
        }
        //four
        if (a['u'-'a'] > 0) {
            b[4] = a['u'-'a'];
            a['f'-'a']-= a['u'-'a'];
            a['o'-'a']-= a['u'-'a'];
            a['r'-'a']-= a['u'-'a'];
        }
        //five
        if (a['f'-'a'] > 0) {
            b[5] = a['f'-'a'];

            a['i'-'a']-= a['f'-'a'];
            a['v'-'a']-= a['f'-'a'];
            a['e'-'a']-= a['f'-'a'];
            a['f'-'a']-= a['f'-'a'];
        }
        //one
        if (a['o'-'a'] > 0) {
            //cout<<"nnnnn "<<a['o'-'a']<<endl;
            b[1] = a['o'-'a'];
            a['n'-'a'] -= a['o'-'a'];
            a['e'-'a'] -= a['o'-'a'];
        }
        //nine
        if (a['i'-'a'] > 0) {
            b[9] = a['i'-'a'];

            a['n'-'a']-= a['i'-'a'];
            a['e'-'a']-= a['i'-'a'];
            a['i'-'a']-= a['i'-'a'];
        }
        //three
        if (a['t'-'a'] > 0) {
            b[3] = a['t'-'a'];

            a['h'-'a']-= a['t'-'a'];
            a['r'-'a']-= a['t'-'a'];
            a['e'-'a']-= a['t'-'a'];
            a['t'-'a']-= a['t'-'a'];
        }

    cout<<"Case #"<<i<<": ";
        for (j = 0; j < 10; j++) {
            //cout<<b[j]<<' '<<j<<endl;
            while (b[j] > 0) {
                printf("%d", j);
                b[j]--;
            }
        }
        printf("\n");
    }
    return 0;
}
