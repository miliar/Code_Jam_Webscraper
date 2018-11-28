#include<bits/stdc++.h>

    using namespace std;
    #define ll long long
    #define MOD 1000000007
    #define infi (int)1e9
    #define FOR(i,a,b) for(i = a; i < b; i++)
    #define FORD(i,a,b) for(i = a; i >= b; i--)
    #define REP(i,a) for(i = 0;i <= a; i++)
    #define REPD(i,a) for(i = a; i >= 0; i--)
    #define s(n)  scanf("%d",&n)
    #define sc(n)  scanf("%c", &n)
    #define sl(n) scanf("%lld", &n)
    #define sf(n) scanf("%f", &n)
    #define ss(n) scanf("%s", n);
    #define all(a) a.begin(), a.end()
    #define fi first
    #define se second
    #define pb push_back
    #define mp make_pair
    #define fill(a, v) memset(a, v, sizeof(a))
    #define PI 3.1415926535897932384626

    ll l ,x, y;
    string str;
char product(char x , char y) {
    int f = 0;
    //cout <<"   "<< x <<" "<<y <<"  ";
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
   // cout <<ch <<endl;
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
        ll t, i, cc = 1;
        freopen("inp.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
        sl(t);
        while(t--) {
            sl(l);
            sl(x);
            y = x;
            cin >> str;
            x = min(x , (ll)12);
            string fin ="";
            FOR(i, 0, x)
                fin = fin+str;
            char pr = '1';
            char w = 'i';
            char p = '1';
            FOR(i, 0, fin.size()) {
                if (i < str.size())
                    p = product(p, str[i]);
                if (w == '1' && i % str.size() == 0)
                    break;
                char ch = fin[i];
                pr = product(pr, ch);
                if(w != '1' && pr == w) {
                    pr = '1';
                    w = next(w);
                //    cout << pr <<" "<<w <<endl;
                }
             //   cout << pr <<" "<<w <<endl;
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
                    pd = product(p,p);
                else {
                    pd = product(product(p,p), p);
                }
            }
            pr = product(pr, pd);

            if (w == '1' && pr == '1') {
              printf("Case #%lld: YES\n", cc);
            } else {
                printf("Case #%lld: NO\n", cc);
            }
            cc++;
        }
        return 0;
}
