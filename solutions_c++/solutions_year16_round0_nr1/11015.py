#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);

    long long int t,n,j,r,c,i,l=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        j=n;
        long long int k=1,sum=0;
        int arr[10];
        memset(arr,0,sizeof(arr));

        if(n==0)
          {

            cout<<"case "<<"#"<<l<<": "<<"INSOMNIA\n";
            l=l+1;
            continue;
          }
        while(1)
        {
            c=j;

            while(c!=0)
            {
                r=c%10;
                arr[r]=1;
                c=c/10;

            }

            for(i=0;i<10;i++)
            {

                sum=sum+arr[i];
            }

            if(sum==10)
            {

              cout<<"case "<<"#"<<l<<": "<<j<<endl;
                l=l+1;
                break;
            }
            k=k+1;
            j=n*k;

            sum=0;
        }
    }
}
