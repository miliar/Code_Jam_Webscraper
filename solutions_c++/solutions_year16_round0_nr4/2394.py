#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.txt");

    if(!fin.is_open())
    {
        cout<<"file error";
    }
    else
    {
        long long t,n,c,k,s;
        fin>>t;
        s=t;
        while(t--)
        {
            fin>>n>>c>>k;
            fout<<"Case #"<<s-t<<": ";
            for(int i=1;i<=k;i++)
                fout<<i<<" ";
            fout<<endl;
        }
        fin.close();
        fout.close();
    }
}
