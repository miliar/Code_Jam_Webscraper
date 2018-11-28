#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,ii;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>n;
        float a[n],b[n],c[n],d[n];
        int answ=0,ansd=0,i,j;
        for(i=0;i<n;i++)
            cin>>a[i];
        for(i=0;i<n;i++)
            cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);

        for(i=0;i<n;i++)
            c[i]=a[i];
        for(i=0;i<n;i++)
            d[i]=b[i];
        for(i=0;i<n;i++) //c
        {
            if(c[i]==-1)
                    continue;
            for(j=0;j<n;j++)
            {
                if(d[j]==-1)
                    continue;
                if(c[i]<d[j])
                {
                    c[i]=-1;
                    d[j]=-1;
                    answ++;
                    break;
                }
            }
        }
        answ=n-answ;
        if(a[n-1]>b[n-1])
        {
           for(i=0;i<n;i++)
            {
                if(b[i]==-1)
                    continue;
                for(j=0;j<n;j++)
                {
                    if(a[j]==-1)
                    continue;
                    if(b[i]<a[j])
                    {
                        a[j]=-1;
                        b[i]=-1;
                        ansd++;
                        break;
                    }
                }
            }
        }
        else
        {
            int xx;
            ansd=0;
            for(i=0;i<n;i++) //c
            {
                if(a[n-1]<b[i])
                {
                    xx=i;
                    break;
                }
            }
            i=0;
            for(j=xx;j<n;j++)
                {
                    b[j]=-1;
                    a[i]=-1;
                    i++;
                }
            for(i=0;i<n;i++)
            {
                if(b[i]==-1)
                    continue;
                 for(j=0;j<n;j++)
                 {
                     if (a[j]==-1)
                     continue;
                     if(a[j]>b[i])
                     {
                         a[j]=-1;
                         b[i]=-1;
                         ansd++;
                         break;
                     }
                 }
            }
          }
      cout<<"Case #"<<ii<<": "<<ansd<<" "<<answ<<"\n";
    }
    return 0;
}
