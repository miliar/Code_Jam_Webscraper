#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int jia(int a, int b)
{
    if (a==1 & b>=1) return 101;

    int r=0;
    while (1)
    {
        if (a>b) break;
        a=a*2-1;
        r++;
    }
    return r;
}

int jia2(int& a, int b)
{
    int r=0;
    while (1)
    {
        if (a>b) break;
        a=a*2-1;
        r++;
    }
    return r;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,TT;
    int i,j,k,n,m[100000];
    int a,r;



    cin>>T;TT=1;
    while (T--)
    {
        r=0;j=0;
        cin>>a>>n;
        for (i=0;i<n;i++) cin>>m[i];
        sort(m,m+n);
        while (1)
        {
            if (j==n) break;
            if (a>m[j]) {a+=m[j];j++;continue;}

            if (jia(a,m[j])>=n-j) {r+=n-j;break;}

            r+=jia2(a,m[j]);
        }

        cout<<"Case #"<<TT<<": "<<r<<endl;

        TT++;
    }

    return 0;
}
