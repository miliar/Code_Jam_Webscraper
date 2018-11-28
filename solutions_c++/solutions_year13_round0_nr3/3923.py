#include <iostream>
#include <stdio.h>
#include <string>
#include <cmath>
using namespace std;

bool huiwen(long long no)
{
    string s;
    while (no!=0)
    {
        s+=no%10;
        no/=10;
    }
    for (int i=0;i<=s.size()/2;i++)
        if (s[i]!=s[s.size()-1-i]) return false;

    return true;
}

bool good(long long no)
{
    if (huiwen(no))
    {
        long long nno=(long long)pow(no,0.5);
        if (no==nno*nno)
            if (huiwen(nno)) return true;
    }
    return false;

}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int i,j,k;
    long long n,m,a,b,r;

    cin>>T;t=1;
    while (T--)
    {

        cin>>a>>b;r=0;
        for (i=a;i<=b;i++)
            if (good(i)) r++;
        cout<<"Case #"<<t<<": "<<r<<endl;
        t++;


    }

    return 0;
}
