#include<iostream>
using namespace std ;
int main()
{
    long long int t,x ;
    cin>>t;
    x=t;
    while(t--)
    {
        long long int m=1,n,i,flag=1,tn,temp ;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<x-t<<": INSOMNIA"<<endl;
        }
        else
        {
            long long int a[10];
            for(i=0;i<10;i++)
            {
                a[i]=0;
            }
            while(flag)
            {
                tn=n;
                //cout<<tn<<endl;
                while(tn)
                {
                    temp=tn%10;
                    a[temp]=1;
                    tn=tn/10;
                }
                flag=0;
                for(i=0;i<10;i++)
                {
                    if(a[i]==0)
                    {
                        m++;
                        n=n*m/(m-1);
                        //cout<<a[i]<<i;
                        flag=1;
                        break;
                    }

                }
                //cout<<endl;
            }
            cout<<"Case #"<<x-t<<": "<<n<<endl;
        }
    }
    return 0;
}
