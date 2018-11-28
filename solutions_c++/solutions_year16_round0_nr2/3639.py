#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int tt;
    fin>>tt;
    for(int t=1;t<=tt;t++)
    {
        string a;
        fin>>a;
        int ans=0;
        fout<<"Case #"<<t<<": ";
        if(a.size()==1)
        {
            if(a[0]=='+')fout<<0<<endl;
            else fout<<1<<endl;
            continue;
        }
        for(int i=1;i<a.size();i++)
        {
            if(a[i]!=a[i-1])
                ans++;
        }
        if(a[a.size()-1]=='-')ans++;
        fout<<ans<<endl;

    }

}
