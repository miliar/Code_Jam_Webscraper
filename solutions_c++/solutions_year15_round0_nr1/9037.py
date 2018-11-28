#include<iostream>
using namespace std;
# define toint(c) c-=48

int ovation(char *a,int n)
{
    int sum=0,c=0,i;
    for(i=0;i<n;++i)
    {
        if(sum<i)
        {
            ++c;
            ++sum;
        }
        sum+=toint(a[i]);
    }
    return c;
}

int main()
{
    char c[100][1005];
    int t,i,len[100];
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>len[i];
        cin>>c[i];
    }
    for(i=0;i<t;++i)
    {
        cout<<"Case #"<<i+1<<": "<<ovation(c[i],(len[i]+1))<<endl;
    }
    return 0;
}
