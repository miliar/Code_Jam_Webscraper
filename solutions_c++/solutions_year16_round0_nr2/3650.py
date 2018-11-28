#include<bits/stdc++.h>
using namespace std;
//#define fout cout
//#define fin cin
string a;
void flip(int j)
{
    for(int i=0;i<=j;i++)
        if(a[i]=='+')a[i]='-';
        else a[i]='+';
    for(int i=0;i<=j/2;i++)
        swap(a[i],a[j-i]);
}

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int tt;
    fin>>tt;
    for(int t=1;t<=tt;t++)
    {
        fin>>a;
        int ans=0;
        fout<<"Case #"<<t<<": ";
        int n=a.size();
        if(n==1 && a[0]=='+')
        {
            fout<<0<<endl;
            continue;
        }
        if(n==1 && a[0]=='-')
        {
            fout<<1<<endl;
            continue;
        }
        for(int i=1;i<n;i++)
        {
            if(a[i]!=a[i-1])
                ans++;
        }
        if(a[n-1]=='-')ans++;
        fout<<ans<<endl;

    }

}
