#include <iostream>
#include <math.h>
#include <cstring>
#define ll long long
using namespace std;

int main()
{
    int t,r;
    cin>>t;
    r=t;
    while(t--)
    {
        ll n;
        cin>>n;
        if(n==0)cout<<"Case #"<<r-t<<": INSOMNIA"<<endl;
        else
        {
            cout<<"Case #"<<r-t<<": ";
            int arr[10];
            for(int i=0;i<10;i++)arr[i]=1;
            //for(int i=0;i<10;i++)cout<<arr[i]<<endl;
            ll cnt=0,b=1;
            while(true)
            {
                int c=0;
                //for(int i=0;i<10;i++)cout<<arr[i]<<" ";cout<<endl;
                for(int i=0;i<10;i++)if(arr[i]!=1)c++;

                //cout<<c<<endl;
                if(c==10)break;
                int num=n*b;//cout<<num<<endl;
                while(num>0)
                {
                    int r=num%10;
                    if(arr[r]!=0)arr[r]=0;
                    num=num/10;

                }
                cnt++;b++;
            }
            int a[100000];
            memset(a,0,sizeof a);
            int i=0,c=0;
            while(n>0)
            {
                //cout<<n<<" ";
                int v=(n%10)*cnt+c;
                a[i]=v%10;
                c=v/10;
                n=n/10;
                i++;
            }
           while(c!=0){a[i]=c%10;c=c/10;i++;}
            for(int j=i-1;j>-1;j--)cout<<a[j]; cout<<endl;

        }
    }
    return 0;
}
