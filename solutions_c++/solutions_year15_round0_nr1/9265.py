#include <bits/stdc++.h>
#define f(x) for(int j=0;j<x;++j)
#include <algorithm>
#include <cmath>
#include <string.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int t;
    cin>>t;


    for(int i=1;i<=t;++i)

    {
       cout<<"Case #"<<i<<": ";
       int smax;
       cin>>smax;
       string prs;
       cin>>prs;

       int nbi=0;
       int nbp=0;

       for(int j=0;j<prs.length();j++)
       {
            int prsj;
            prsj=(int)prs[j] -'0';
            if(nbp<j)
            {
                    nbi++;
                    nbp+=1;
            }
            nbp+=prsj;
       }
       cout<<nbi;
        cout<<endl;
    }



    return 0;
}
