#include <bits/stdc++.h>

using namespace std;

bool yes;
string gs;
int len;
inline bool trans(char &ch, char ch2)
{
    if (ch=='1')
    {
        ch=ch2;
        return false;
    }
    else if (ch=='i')
    {
        if (ch2=='1')      { ch = 'i'; return false; }
        else if (ch2=='i') { ch = '1'; return true; }
        else if (ch2=='j') { ch = 'k'; return false; }
        else if (ch2=='k') { ch = 'j'; return true; }
    }
    else if (ch=='j')
    {
        if (ch2=='1')      { ch = 'j'; return false; }
        else if (ch2=='i') { ch = 'k'; return true; }
        else if (ch2=='j') { ch = '1'; return true; }
        else if (ch2=='k') { ch = 'i'; return false; }
    }
    else if (ch=='k')
    {
        if (ch2=='1')      { ch = 'k'; return false; }
        else if (ch2=='i') { ch = 'j'; return false; }
        else if (ch2=='j') { ch = 'i'; return true; }
        else if (ch2=='k') { ch = '1'; return true; }
    }
}
char cachek[20000];
void solvek(int p)
{
    if (cachek[p]) return;
    cachek[p] = 1;
    int sign = 0;
    char ch = gs[p];
    p++;
    for (int i=p;i<len;i++)
    {
        bool bsign = trans(ch, gs[i]);
        if (bsign) sign = 1-sign;
    }
    if (ch=='k' && sign==0)
    {
        yes = true;
    }
}

void solvej(int p)
{
    int sign = 0;
    char ch = gs[p];
    p++;
    for (int i=p;i<len;i++)
    {
        if (yes) return;
        if (ch=='j' && sign==0)
        {
            solvek(i);
        }
        bool bsign = trans(ch, gs[i]);
        if (bsign) sign = 1-sign;
    }
}

void solvei(int p)
{
    int sign = 0;
    char ch = gs[p];
    p++;
    for (int i=p;i<len;i++)
    {
        if (yes) return;
        if (ch=='i' && sign==0)
        {
            solvej(i);
        }
        bool bsign = trans(ch, gs[i]);
        if (bsign) sign = 1-sign;
    }
}

int main(int argc,char *argv[])
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int L,X;
        cin >> L >> X;
        memset(cachek, 0, sizeof(cachek));
        char buf[65536];
        cin.getline(buf, 65536);
        cin.getline(buf, 65536);
        string s = buf;
        stringstream ss;
        for (int i=0;i<X;i++)
            ss << s;
        gs = ss.str();
        len = gs.length();
        yes = false;
        solvei(0);
        cout << "Case #" << t+1 << ": " << ((yes) ? "YES" : "NO") << endl;
    }

  return 0;
}
