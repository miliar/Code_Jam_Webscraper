#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define SZ(a) ((int)a.size())
#define pb push_back

int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out" , "w+" , stdout);
    int tcase,cas=1;
    cin>>tcase;

    while(tcase--)
    {
        ll mxvalue;
        string str;

        cin>>mxvalue>>str;
//        if(cas==87) cout<<mxvalue<<" "<<str<<endl;
        ll total = 0;
        ll need = 0;

        for(int i = 0 ; i<=mxvalue ; i++)
        {
            if(str[i]=='0') continue;
            if(total>=i)
            {
                total += (str[i]-'0');
            }
            else
            {
                ll tmp = abs(i-total);
                need += tmp;
                total += tmp;
                total += (str[i]-'0');
            }
        }
        cout<<"Case #"<<cas++<<": "<<need<<endl;
    }
    return 0;
}
