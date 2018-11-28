#include<bits/stdc++.h>
using namespace std;
long long a[1000005]= {0},h[11];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long t,x;
    cin>>t;
    for(x=1; x<=t; x++)
    {
        long long i=0,n,temp,r,j,c=0,y=2;
        for(i=0; i<10; i++)
            h[i]=0;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<x<<": INSOMNIA\n";
            continue;
        }
        temp=n;
        i=0;
        while(temp>0)
        {
            r=temp%10;
            if(h[r]==0)
            {
                h[r]=1;
                c++;
            }
            a[i++]=r;
            temp=temp/10;
        }
        //cout<<i<<"\n";
        if(c==10)
        {
            cout<<"Case #"<<x<<": "<<n<<"\n";
            continue;
        }

        while(y<=1000000)
        {
            temp=0;
            for(j=0; j<i; j++)
            {
                a[j]=a[j]*y+temp;
                temp=(a[j]-(a[j]%10))/10;
                a[j]=a[j]%10;
                if(h[a[j]]==0)
                {
                    h[a[j]]=1;
                    c++;
                }
            }
            if(temp!=0)
                while(temp>0)
                {
                    r=temp%10;
                    if(h[r]==0)
                    {
                        h[r]=1;
                        c++;
                    }
                    a[i++]=r;
                    temp=temp/10;
                }
            if(c==10)
                break;
            temp=n;
            i=0;
            while(temp>0)
            {
                r=temp%10;
                a[i++]=r;
                temp=temp/10;
            }
            y++;
        }
        if(c<10)
            cout<<"Case #"<<x<<": INSOMNIA\n";
        else
        {
            cout<<"Case #"<<x<<": ";
            for(j=i-1; j>=0; j--)
                cout<<a[j];
            printf("\n");
        }
    }
}
