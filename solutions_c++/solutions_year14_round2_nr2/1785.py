#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j,k,l,m,n,o,p;
    cin>>t;
    for(p=0;p<t;p++)
    {
        cin>>i>>j>>k;
        l=0;
        for(m=0;m<i;m++)
        {
            for(n=0;n<j;n++)
            {
                if((m&n)<k)
                l++;
            }
        }
        cout<<"Case #"<<p+1<<": "<<l<<endl;
    }
    return 0;
}
