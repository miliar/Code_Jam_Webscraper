#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int t ;
    cin>>t;

    for(int i=1; i<=t; i++)
    {
        int a,b,k;
        cin>>a>>b>>k;

        int valid_pairs=0;
        for(int l=0; l<a; l++)
        {
            for(int u=0; u<b; u++)
            {
                int c=l&u;

                if(c  < k)
                {
                    valid_pairs++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<valid_pairs<<'\n';
    }

    return 0;
}
