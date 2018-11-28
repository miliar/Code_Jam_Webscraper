#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,t1=1,m,n,val,done,i;
    cin>>t;
    while(t1<=t)
    {
        cin>>n;
        done=0;
        int a[10];
        for(i=0;i<10;i++)
        {
            a[i]=0;
        }
        i=1;
        if(n!=0)
        {
            while(done!=10)
            {
                m=n*i;
                while(m>0)
                {
                    val=m%10;
                    if(a[val]==0)
                    {
                        a[val]=1;
                        done=done+1;
                    }
                    m=m/10;
                }
                i++;
            }
        }
        if(n==0)
        {
            cout<<"Case #"<<t1<<": INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<t1<<": "<<(i-1)*n<<endl;
        }
        t1++;
    }
    return 0;
}
