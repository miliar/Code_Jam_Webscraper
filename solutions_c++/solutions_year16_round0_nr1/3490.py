#include<bits/stdc++.h>
using namespace std;
bool a[10];
bool check(bool a[])
{
    for(int i=0;i<10;i++)
    {
        if(a[i]==false)
            return false;
    }
    return true;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
    long long n,tmp2;
    cin>>n;
    tmp2=n;
    if(!n)
      printf("Case #%d: INSOMNIA\n",test);
      else
    {
        memset(a,false,sizeof(a));
        int i=2;
        while(1)
        {
            long long tmp=n;
            while(tmp)
            {
                a[tmp%10]=true;
                tmp/=10;
            }
            if(check(a))
                break;
            n=i*tmp2;
            i++;
            }
            printf("Case #%d: %d\n",test,n);
    }
    }
    return 0;
}
