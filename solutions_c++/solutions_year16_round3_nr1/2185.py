#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("outputrr444new.o", "w", stdout);
    int t,arr[3],j,n,i,in[30],sum=0,mx,save;
    cin >> t;
    for(int ca=1; ca<=t; ca++)
    {
        sum=0,mx=0;
        cin >> n;
        for(i=1; i<=n; i++)
        {
            cin >> in[i];
            sum+=in[i];
            if(in[i]>mx)
            {
                mx=in[i];
                save=i;
            }
        }

        int ck=1;
        int mx1=-1,mx2=-1;
        j=0;
        printf("Case #%d: ",ca);
        if(sum%2!=0)
        {
            printf("%c ",save+64);
            in[save]--;
        }
        while(ck)
        {
            mx1=0;
            for(i=1; i<=n; i++)
            {
                if(in[i]==mx2)
                {
                    arr[j++]=i;
                    in[i]--;
                }
                if(j==2)
                {
                    printf("%c%c ",arr[0]+64,arr[1]+64);
                    j=0;
                }
                mx1=max(mx1,in[i]);
            }

            mx2=mx1;
            if(mx1==0)
            {
                break;
            }
        }
        cout << endl;

    }
}
