#include <iostream>
#include <cstdio>
using namespace std;
long long n,t,p[1002],a,b,c,i,j,k,l;
bool ka[12];
void av(long long x)
{
    while(x>0)
    {
        l=x%10;
        if(!ka[l])
        {
            ka[l]=true;
            k++;
        }
        x/=10;
    }
}
int main()
{
    freopen("input.txt", "r" , stdin);
    freopen("output.txt" , "w" , stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        if(n==0)
        {
            goto x;
        }
        k=0;
        for(j=0;j<10;j++)
            ka[j]=false;
        j=0;
        while(k<10)
        {
            j++;
            av(n*j);
            if(k==10)
            {
                p[i]=n*j;
                break;
            }
        }
    x:
        cout<<"Case #"<<i<<": ";
        if(p[i]==0)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<p[i]<<endl;
    }
    return 0;
}