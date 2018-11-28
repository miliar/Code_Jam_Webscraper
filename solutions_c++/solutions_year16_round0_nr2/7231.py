#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;

string s;
int l;

ifstream fin ("B.in");
ofstream fout ("B.out");

void flip(int p)
{
    for(int i=0;i<p;i++)
    {
        if(s[i]=='-') s[i]='+';
        else s[i]='-';
    }
}

void solve()
{
    int sz=s.size();
    int ans=0;
    for(int i=sz-1;i>=0;i--)
    {
        if(s[i]=='-')
        {
            ans++;
            flip(i+1);
        }
    }
    fout << "Case #" << l+1 << ": " << ans << "\n";
}

int main()
{
    int t;
    fin >> t;
    for(l=0;l<t;l++)
    {
        fin >> s;
        solve();
    }
    return 0;
}
