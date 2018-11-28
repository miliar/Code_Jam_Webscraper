#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main()
{
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");
    int i,j,k,n,t,ans1,ans2,tmp;
    double a[1010],b[1010];
    fin>>t;
    for (k=1; k<=t; k++)
    {
        fin>>n;
        for (i=0;i<n;i++) 
            fin>>a[i];
        for (i=0;i<n;i++) 
            fin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        tmp=ans1=0;
        for (i=0;i<n;i++)
            {
               while (tmp<n && a[i]>b[tmp]) tmp++;
               tmp++;
               if (tmp>n) ans1++;
            }
        tmp=0;
        ans2=0;
        for (i=0;i<n;i++)
        if (a[i]>b[tmp])
        {ans2++; tmp++;}
        fout<<"Case #"<<k<<": ";
        fout<<ans2<<' '<<ans1<<endl;
    }

    return 0;
}
