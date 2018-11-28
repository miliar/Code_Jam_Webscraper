#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt4.txt");
    ofstream fout("output.txt");
    #ifndef ONLINE_JUDGE
    freopen("5.txt", "rt", stdin);
    #endif
    int t, s, cont=0, con, res=0, zero;
    string k;
    fin>>t;
    for(int i=0; i<t; i++)
    {
        fin>>s>>k;
        for(int j=0; j<=s; j++)
        {
            con=(int)k[j]-48;
            if(cont<j)
            {
                res++;
                cont=j;
            }
            cont+=con;
        }
        fout<<"Case #"<<i+1<<": "<<res<<endl;
        cont=res=0;
    }
    return 0;
}
