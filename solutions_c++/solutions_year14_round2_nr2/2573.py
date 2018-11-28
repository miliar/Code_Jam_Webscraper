#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int t,a,b,k,count=0,x=1,i,j;
    freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>a>>b>>k;
        count=0;
        for(i=0;i<a;++i)
        {
            for(j=0;j<b;++j)
            {
                if((i&j)<k)
                    ++count;
            }
        }
        cout<<"Case #"<<x<<": "<<count<<"\n";
    x++;
    }
    return 0;

    }

