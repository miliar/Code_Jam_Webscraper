#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;
int T,N,m;
int a[111][111];
string s,sm,ss;

string process(string s, int x)
{
    string s1;
    int d=0;
    int u=1;
    s1.clear();
    s1+=s[0];
    for (int i=1; i<s.length(); i++)
    {
        //cout<<s[i] <<ss[d]<<endl;
        if (s[i]==s1[d]) u++;
        else
        {
            a[x][d]=u;
            u=1; d++; s1+=s[i];
            //cout<<d<<endl;
        }
    }
    a[x][d]=u;
return s1;
}

int main()
{
    freopen("a.inp", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    for (int test=1; test<=T; test++)
    {
        bool ok=true;
        cin>>N;
        cin>>s;
        sm=process(s, 0);
        //cout<<sm<<endl;
        m=sm.length();
        for (int i=1; i<N; i++)
        {
            cin>>s;
            ss=process(s, i);
            if (ss!=sm)
            {
                ok=false;

            }
        }
        if (ok)
        {
        int kq=0;
        int b[111];
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<N; j++) b[j]=a[j][i];
            sort(b, b+N);

            for (int j=0; j<N; j++) kq+=abs(b[j]-b[N/2]);
        }
        cout<<"Case #"<<test<<": "<<kq<<endl;
        }
        else cout<<"Case #"<<test<<": Fegla Won"<<endl;
    }
    return 0;
}


