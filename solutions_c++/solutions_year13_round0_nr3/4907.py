#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
bool pal(int a)
{
    int d=0,c=0;
    int num=a;
    while(num)
    {
        d=d*10;
        d+=num%10;
        num=num/10;
    }
    if(d==a)
    return 1;
    else return 0;
}
int main()
{
    int t,a,b;
    cin>>t;
    for(int m=1;m<=t;m++)
    {
        int ans=0;
        cin>>a>>b;
        for(int i=a;i<=b;i++)
        {
            int s=sqrt(i);
            if(s*s!=i)
            continue;
            else if(pal(s) && pal(i))
            ans++;
        }
        cout<<"Case #"<<m<<": "<<ans<<"\n";
    }
}