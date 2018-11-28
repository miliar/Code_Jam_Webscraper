#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define pb push_back
int arr[10];
int main()
{
    LL int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        LL int n;
        scanf("%lld",&n);
        memset(arr,0,sizeof(arr));
        if(n==0)
            printf("Case #%d: INSOMNIA\n",tc);
        else
        {
            LL int n1=n;
            while(1)
            {
                LL int c=n;
                while(c>0)
                {
                    arr[(c%10)]=1;
                    c/=10;
                }
                int chk=0;
                int cnt=0;
                for(int i=0;i<10;i++)
                {
                    if(arr[i])
                        cnt++;
                }
                if(cnt==10)
                    chk=1;
                if(chk)
                {
                     printf("Case #%d: %lld\n",tc,n);
                     break;
                }
                n+=n1;
             }
         }
     }    
     return 0;
 }                      
