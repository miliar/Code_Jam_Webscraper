#include <iostream>
using namespace std;

bool sum(int count[])
{
    int s=0;
    for(int i=0;i<10;i++)
    {
        s+=count[i];
    }
    if(s==10)
        return true;
    return false;
}
int main()
{
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        long int n,ans;
        cin>>n;
        int flag=0;
        int count[10]={0};
        for(int i=1;i<=1000000;i++)
        {
            if(n==0)
            {
                break;
            }
            else
            {
                long int m=i*n;
                long int x=m;
                while(x>0)
                {
                    count[x%10]=1;
                    x/=10;
                }
                if(sum(count))
                {
                    flag=1;
                    ans=m;
                    break;
                }
                
            }
        }
        
        cout<<"Case #"<<T<<": ";
        if(flag)
        {
            cout<<ans<<endl;
        }
        else
            cout<<"INSOMNIA"<<endl;
        
    }
    return 0;
}

