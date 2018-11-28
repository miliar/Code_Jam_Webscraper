#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("output.txt");
    double z[1000],x[1000];
    int t;
    fin>>t;
    for(int k=1;k<=t;++k)
    {
        int n;
        fin>>n;
        for(int i=0;i<n;++i)fin>>z[i];
        for(int i=0;i<n;++i)fin>>x[i];
        //system("PAUSE");
        sort(z,z+n);
        sort(x,x+n);
        //system("PAUSE");
        int ans1=0,ans2=0;
        int a=0,b=n-1;
        for(int i=n-1;i>=0;--i)
        {
            if(z[i]>x[b])ans1++;
            else b--;
        }
        b=0;
        //system("PAUSE");
        for(int i=0;i<n;++i)
        {
            if(z[i]>x[b])++ans2,++b;
        }
        fout<<"Case #"<<k<<": "<<ans2<<" "<<ans1<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
