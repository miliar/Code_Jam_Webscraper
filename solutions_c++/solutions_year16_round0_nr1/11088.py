#include<bits/stdc++.h>
using namespace std;
long n[10000000],r[10000000];
int main()
{
    long t,i,j,k,f,s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        f=1;
        long a[20]={0};
        cin>>n[i];
       /*
            printf("Case #%ld: INSOMNIA\n",i);*/
        if(n[i]!=0){
        j=1;
        while(1)
        {
            f=1;
            s = j*n[i];
            r[i] = s;
            for(;s>0;)
            {
                k = s%10;
                s = s/10;
                if(a[k]==0)
                    a[k]++;
            }
            for(k=0;k<=9;k++)
            {
                if(a[k]==0){
                    f=0;
                    break;
                }
            }
            if(f==1)
                break;
            j++;
        }
        }
    }
        for(i=1;i<=t;i++)
        {
            if(n[i]==0)
                printf("Case #%ld: INSOMNIA\n",i);
            else
                printf("Case #%ld: %ld\n",i,r[i]);
        }
    return 0;
}
