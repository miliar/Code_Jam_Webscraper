#include<bits/stdc++.h>

using namespace std;

#define ll long long

ll l ,x, y;

string str;

char multiplication(char x , char y) {

    int f = 0;

    if (x == '0' || x == 'I' || x == 'J' || x == 'K') {
        if (x == '0')
            x = '1';
        else
            x += 32;
        f++;
    }
    if (y == '0' || y == 'I' || y == 'J' || y == 'K') {
        if (y == '0')
            y = '1';
        else
            y += 32;
        f++;
    }
    char ch;
    if (x == '1' && y == '1') ch =  '1';
    if (x == '1' && y == 'i') ch =  'i';
    if (x == '1' && y == 'j') ch =  'j';
    if (x == '1' && y == 'k') ch =  'k';
    if (x == 'i' && y == '1') ch =  'i';
    if (x == 'i' && y == 'i') ch =  '0';
    if (x == 'i' && y == 'j') ch =  'k';
    if (x == 'i' && y == 'k') ch =  'J';
    if (x == 'j' && y == '1') ch =  'j';
    if (x == 'j' && y == 'i') ch =  'K';
    if (x == 'j' && y == 'j') ch =  '0';
    if (x == 'j' && y == 'k') ch =  'i';
    if (x == 'k' && y == '1') ch =  'k';
    if (x == 'k' && y == 'i') ch =  'j';
    if (x == 'k' && y == 'j') ch =  'I';
    if (x == 'k' && y == 'k') ch =  '0';

    if (f % 2) {
        if (ch == '1')
            ch = '0';
        else if (ch == '0')
            ch = '1';
        else if (ch < 97)
            ch += 32;
        else
            ch -= 32;
    }

    return ch;
}
char next(char x)
{

    if(x == 'i')
        return 'j';
    if(x == 'j')
        return 'k';
    return '1';
}
int main()
{
        freopen("inp.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
        ll t, i, u = 0;
        cin >> t;
        while(t--) {
            cin >> l >> x;
            y = x;
            cin >> str;
            x = min(x , (ll)12);
            string sexy = "";
            for (i = 0; i < x; i++)
                sexy = sexy+str;
            char pr = '1';
            char w = 'i';
            char p = '1';
            for (i = 0; i < sexy.size(); i++) {
                if (i < str.size())
                    p = multiplication(p, str[i]);
                if (w == '1' && i % str.size() == 0)
                    break;
                char ch = sexy[i];
                pr = multiplication(pr, ch);
                if(w != '1' && pr == w) {
                    pr = '1';
                    w = next(w);
                }
            }
            x = y;
            char pd = '1';
            i /= str.size();
            if (x > i) {
                x -= i;
                x %= 4;
                if (x == 0)
                    pd = '1';
                else if (x == 1)
                    pd = p;
                else if (x == 2)
                    pd = multiplication(p,p);
                else {
                    pd = multiplication(multiplication(p,p), p);
                }
            }
            pr = multiplication(pr, pd);

            if (w != '1' || pr != '1') {
                cout << "Case #" << ++u << ": " << "NO" << endl;
            } else {
                cout << "Case #" << ++u << ": " << "YES" << endl;
            }
        }
        return 0;
}
