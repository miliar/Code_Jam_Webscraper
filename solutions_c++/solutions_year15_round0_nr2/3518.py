#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        int d;
        int b[1005];
        for(int i=0;i<1005;i++) b[i]=0;
        scanf("%d",&d);
        int a[d+1];

        int maxx=0;
        for(int i=0;i<d;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]>maxx)  maxx=a[i];
        }
        long long int count=INT_MAX;
        long long int split=0;
        for(int i=1;i<=maxx;i++)
        {
            split=0;
            for(int j=0;j<d;j++)
            {
                if(a[j]<=i) continue;

                if(a[j]%i==0) { split+= (a[j]/i) -1;}
                else split+= a[j]/i;

            }
            count= min(count, (split+ i));
        //    cout<<count<<"   "<<(split+i)<<endl;
        }
        cout<<"Case #"<<z<<": "<<count<<endl;
        z++;



    }



    return 0;
}
