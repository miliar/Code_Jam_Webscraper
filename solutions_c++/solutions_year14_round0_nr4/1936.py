#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j,k,l,m,n,o,p,q;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>j;
        double A[j],B[j];
        int used[j];
        for(k=0;k<j;k++)
            used[k]=0;
        for(k=0;k<j;k++)
        cin>>A[k];
        for(k=0;k<j;k++)
        cin>>B[k];
        sort(A,A+j);
        sort(B,B+j);
        l=0;
        o=0;
        for(k=0;k<j;k++)
        {
            for(m=0;m<j;m++)
            {
                if(A[k]>B[m]&&used[m]==0)
                {
                    used[m]=1;
                    o++;
                    break;
                }
            }
        }
        l=0;
        p=0;
        for(k=0;k<j&&l<j;k++)
        {
            while(l<j&&B[l]<A[k])
            {
                l++;p++;
               // cout<<A[k]<<" "<<B[l]<<" "<<p<<endl;
            }
            l++;
        }
        cout<<"Case #"<<i+1<<": "<<o<<" "<<p<<endl;
    }
    return 0;
}
