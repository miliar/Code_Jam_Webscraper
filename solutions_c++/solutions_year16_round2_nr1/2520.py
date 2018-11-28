#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    ios_base::sync_with_stdio(0);
    ll sum=0,count=0,t;
    ifstream f("A-large (1).in");
    ofstream o("Bout.out");
    f>>t;
    int z=t;
    while(t--)
    {
        char a[3000];
        ll n;
        f>>a;
        n=strlen(a);
        int b[26]={0},c[10]={0};
        for(int i=0;i<n;i++)
        {
            b[a[i]-'A']++;
        }
        c[0]=b[25];
        b['E'-'A']-=b[25];
        b['R'-'A']-=b[25];
        b['O'-'A']-=b[25];
        b[25]=0;
        c[2]=b['W'-'A'];
        b['T'-'A']-=b['W'-'A'];
        b['O'-'A']-=b['W'-'A'];
        b['W'-'A']=0;
        c[6]=b['X'-'A'];
        b['S'-'A']-=b['X'-'A'];
        b['I'-'A']-=b['X'-'A'];
        b['X'-'A']=0;
        c[8]=b['G'-'A'];
        b['E'-'A']-=b['G'-'A'];
        b['I'-'A']-=b['G'-'A'];
        b['H'-'A']-=b['G'-'A'];
        b['T'-'A']-=b['G'-'A'];
        b['G'-'A']=0;
        c[4]=b['U'-'A'];
        b['F'-'A']-=b['U'-'A'];
        b['O'-'A']-=b['U'-'A'];
        b['R'-'A']-=b['U'-'A'];
        b['U'-'A']=0;
        c[1]=b['O'-'A'];
        b['N'-'A']-=b['O'-'A'];
        b['E'-'A']-=b['O'-'A'];
        b['O'-'A']=0;

         c[3]=b['H'-'A'];
        b['E'-'A']-=b['H'-'A'];
         b['E'-'A']-=b['H'-'A'];
        b['R'-'A']-=b['H'-'A'];
        b['T'-'A']-=b['H'-'A'];
        b['H'-'A']=0;
        c[5]=b['F'-'A'];
        b['E'-'A']-=b['F'-'A'];
         b['V'-'A']-=b['F'-'A'];
        b['I'-'A']-=b['F'-'A'];
        b['F'-'A']=0;
        c[7]=b['S'-'A'];
        b['E'-'A']-=b['S'-'A'];
         b['V'-'A']-=b['S'-'A'];
        b['E'-'A']-=b['S'-'A'];
        b['N'-'A']-=b['S'-'A'];
        b['S'-'A']=0;
        c[9]=b['I'-'A'];
        o<<"Case #"<<z-t<<": ";
        for(int i=0;i<=9;i++)
        {
            for(int j=0;j<c[i];j++)
                o<<i;
        }
        o<<endl;
    }
	return 0;
}




