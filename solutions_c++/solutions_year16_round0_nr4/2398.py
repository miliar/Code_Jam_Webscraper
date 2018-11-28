
#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <cstring>
#include <InfInt.h>

using namespace std;

int main()
{
    int t, u, k, c, s, no_of_tiles, dig, i;
    InfInt offset;
    
    freopen("D.in", "rt", stdin);
    freopen("D.out", "wt", stdout);
    cin>>t;
    u=1;
    while(u<=t)
    {
        cin>>k>>c>>s;
         
        cout<<"Case #"<<u<<":";
        u++;
        if(k==1)
        {
            cout<<" 1\n";
            continue;
        }
        if(c==1)
        {
            if(s<k)
            {
                cout<<" IMPOSSIBLE\n";
                continue;
            }
            for(i=0;i<k;i++)
                cout<<" "<<i+1;
            cout<<endl;
            continue;
        }
           
        no_of_tiles=k-1;
        if(no_of_tiles>s)
        {
            cout<<" IMPOSSIBLE\n";
            continue;
        }
        InfInt temp=1;
        for(i=0;i<c-1;i++)
            temp*=k;
        offset=0;
        dig=2;
        while(no_of_tiles>0)
        {
            cout<<" "<<offset+dig;
            dig++;
            offset+=temp;
            no_of_tiles--;
        }
        cout<<endl;
        
        
    }
    return 0;
}

/**/

