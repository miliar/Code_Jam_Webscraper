#include <bits/stdc++.h>
using namespace std;
string to_string(int n)
{
    stringstream convert;

    convert << n;

    string Result = convert.str();
    return Result;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cont,i,m[11],z;
    long long int n,valor;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        string s;

        cin >> s;

        istringstream aux1(s);
        aux1 >> n;

        if(!n)
             cout<<"Case #"<<x<<": INSOMNIA"<<'\n';
        else
        {
            cont=0;
            memset(m,0,sizeof m);
            z=1;
            while(1)
            {
                i=0;
                valor=n*z;
                s=to_string(valor);
                 z++;
                //cout<<valor<<'\n';
                while(s[i])
                {
                    if(!m[s[i]-'0']) cont++;
                     m[s[i]-'0']=1;
                     i++;
                }

                if(cont==10) break;
            }
            cout<<"Case #"<<x<<": "<<valor<<'\n';
        }
    }
    return 0;
}
