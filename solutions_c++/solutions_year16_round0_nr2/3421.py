#include<bits/stdc++.h>
using namespace std;
//ifstream fin("B-large.in");
//ofstream fout("out6.txt");
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(false);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        string a;
        cin>>a;
        int co=0;
        for(int i=0;i<a.length()-1;i++)
        {
            if(a[i]!=a[i+1])
                co++;
        }
        if(a[a.length()-1]=='-')
            co++;
         cout<<"Case #"<<k<<": "<<(co)<<"\n";
    }
}
