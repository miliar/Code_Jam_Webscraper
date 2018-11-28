#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, i, j, tam, q, r;
    char v[1000], atu;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        atu='+';
        q = 0;
        scanf("%*c%s", v);
        tam = strlen(v);
        for(j=0;j<tam;j++)
        {
            if(v[j]!=atu && atu=='+')
                q++;
            atu = v[j];
        }
        r = 2*q;
        if(v[0]=='-')
            r--;
        cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
