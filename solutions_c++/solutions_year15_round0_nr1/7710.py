#include<stdio.h>
#include<iostream>

using namespace std;
int main()
{
    int i,t,n,j,stand,borrow;
    char st[1020];
     freopen("A-large.in","r",stdin);
     freopen("co.out","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {

        cin>>n>>st;
        stand = 0;
        borrow = 0;
        for(j=0;j<=n;j++)
        {
            if(stand>=j)
            {
                stand=stand+(st[j]-48);
            }
            else
            {
                borrow+=(j-stand);
                stand+=(j-stand);
                stand+=(st[j]-48);
            }
        }
        cout<<"Case #"<<i<<": "<<borrow<<endl;
    }
    return 0;
}
