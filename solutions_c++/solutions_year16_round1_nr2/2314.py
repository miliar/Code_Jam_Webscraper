#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int t,n,i,j,num,x;
    cin>>t;

    int a[5005];
    for(x=1;x<=t;x++)
    {
        cin>>n;
        memset(a,0,sizeof(int)*5005);
        for(i=1;i<2*n;i++)
        {
            for(j=1;j<=n;j++)
            {
                cin>>num;
                a[num]++;
            }
        }
        cout<<"Case #"<<x<<": ";
        for(i=1;i<=5000;i++)
        {
            if(a[i]&1)
                cout<<i<<" ";
        }
        cout<<endl;
    }

}
