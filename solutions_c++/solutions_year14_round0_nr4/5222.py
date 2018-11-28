#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
    int t,n,ca,dw,w;
    ca=1;
    double na[10],ken[10];
    cin>>t;
    while(t--)
    {
        dw=w=0;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>na[i];
        for(int i=0;i<n;i++)
            cin>>ken[i];
        sort(na, na+n);
        sort(ken, ken+n);
        int i=n-1,j=n-1;
        while(i>=0 && j>=0)
        {
            if(na[i]>ken[j])
            {
                dw++;
                i--;j--;
            }
            if(na[i]<ken[j])
            {
                j--;
            }
        }
        i=j=n-1;
        while(i>=0 && j>=0)
        {
            if(na[i]<ken[j])
            {
                w++;
                i--;j--;
            }
            if(na[i]>ken[j])
            {
                i--;
            }
        }
        printf("Case #%d: %d %d\n",ca++,dw,n-w);
    }
    return 0;
}
