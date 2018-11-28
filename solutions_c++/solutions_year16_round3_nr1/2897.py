#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output_small.txt","w",stdout);
    int t,u=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,cnt=0;
        scanf("%d",&n);
        int a[n];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        while(1){
        int maximum=a[0],flag=0,b,k=0;
        for(int i=0;i<n;i++)
        {
            if(maximum<a[i])
            {
                maximum=a[i];
                k=i;
                flag=0;
            }
            else if(maximum==a[i]&&i!=0)
            {
                flag=1;
                b=i;
            }

        }
        int counter=0,q;
        for(int i=0;i<n;i++)
        {
            if(a[i]==1)
            {
                q=i;
                counter++;
            }
        }
        if(counter>2)
        {
            flag=2;
        }
        //cout<<k<<" "<<b<<endl;
        cnt++;
        if(cnt==1)
        {
            cout<<"Case #"<<u<<": ";
        }
        if(flag==0)
        {

            a[k]-=2;
            cout<<char(k+65)<<char(k+65)<<" ";

        }
        else if(flag==1)
        {
            a[k]-=1;
            a[b]-=1;
            cout<<char(k+65)<<char(b+65)<<" ";
        }
        else
        {
            a[q]-=1;
            cout<<char(q+65)<<" ";
        }
        int flag1=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]!=0)
            {
                flag1=1;
                break;
            }
        }
        if(flag1==0)
            break;
        }
        u++;
        cout<<endl;
    }
}
