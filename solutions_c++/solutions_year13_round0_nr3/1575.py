#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
long long const MAX=10000000;
bool judge(long long x)
{
    int l=0;
    char a[320],b[320],c[320];
    memset(a,'\0',sizeof(a));
    memset(b,'\0',sizeof(b));
    memset(c,'\0',sizeof(c));
    bool flag=false;
    while(x>0)
    {
        a[l++]=x%10+'0';
        x/=10;
    }
    strcpy(b,a);
    strrev(a);
    int j=0;
    for(int i=0;i<l;i++)
    {
        if(b[i]!='0')
        {
            j=i;
            break;
        }
    }
    int cl=0;
    for(;j<l;j++)
    {
        c[cl++]=b[j];
    }
    if(strcmp(a,c)==0)
    {
        return true;
    }
    return false;
}
int main()
{
    int t;
    long long num[100];
    int ln=0;
    memset(num,0,sizeof(num));
    for(long long i=1;i<=MAX;i++)
    {
        if(judge(i)&&judge(i*i))
        {
            num[ln++]=i*i;
        }
    }

//    freopen("C-large-1.in","r",stdin);
//    freopen("C-large-1.txt","w",stdout);

    cin>>t;
    for(int c=1;c<=t;c++)
    {
        int ans=0;
        long long a,b;
        cin>>a>>b;
        for(int i=0;i<ln;i++)
        {
            if(num[i]>=a&&num[i]<=b)
            {
                ans++;
            }
            if(num[i]>b)
            {
                break;
            }
        }
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
    return 0;
}
