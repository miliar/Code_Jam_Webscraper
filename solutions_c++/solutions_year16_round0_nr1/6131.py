#include<bits/stdc++.h>
using namespace std;
void fun(int flag[],int n)
{
    while(n>0)
    {
        int a=n%10;
        n=n/10;
        flag[a]=0;
    }
}
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;++i)
    {
        int n;
        cin>>n;
        int flag[10];
        memset(flag,1,sizeof flag);
        int g,j=1;
        while(flag[0]||flag[1]||flag[2]||flag[3]||flag[4]||flag[5]||flag[6]||flag[7]||flag[8]||flag[9]){
            if(n==0)
            {
                break;
            }
            fun(flag,n*j);
            g=n*j;
            ++j;
        }
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<g<<endl;
        }
    }
}
