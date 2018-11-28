#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,n,peo,count,i,j;
    char c;
    cin>>t;
    for (j=1;j<=t;j++)
    {
        scanf("%*c%c%*c",&c);
        //cout<<c;
        n=(int)c-48;
        //cout<<n;
        count=0;
        peo=0;
        for(i=0;i<=n;i++)
        {
            scanf("%c",&c);
            if(count<i)
            {
            	peo+=(i-count);
                count=count+(i-count);
            }
            count+=((int)c-48);
        }
        cout<<"Case #"<<j<<": "<<peo<<'\n';
        //Case #1:
    }
    return 0;
}
