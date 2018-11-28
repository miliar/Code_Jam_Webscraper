#include<bits/stdc++.h>
# define l long long int
using namespace std;
bool check(bool a[])
{
    l i,f=1;
    for(i=0;i<10;i++)
    {
       if(a[i]==0)
       {
           f=0;
           break;
       }
    }
    return f;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    l t,m;
    cin>>t;
    for(m=1;m<=t;m++)
    {
        l n,i=1,num,res;
        bool a[10]={0};
        cin>>n;
        cout<<"Case #"<<m<<": ";
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
        while(check(a)!=1)
        {
            num=n*i;
            while(num)
            {
                res=num%10;
                a[res]=1;
                num=num/10;
            }
            if(check(a)==1)
            {
                break;
            }
            else
            {
            i++;
            }
        }
        }
        cout<<i*n<<endl;
    }
    return 0;
}
