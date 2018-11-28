#include<iostream>
#include<cstdio>

using namespace std;

int ar[10];

int check(long n)
{
    int f=0;
    int i=1;
    long vd;
    for(int i=0;i<10;i++) ar[i]=0;
    while(f==0)
    {
        vd=n*i;
        while(vd!=0)
        {
            ar[vd%10]++;
            vd=vd/10;
        }
        for(int j=0;j<10;j++)
        {
            if(ar[j]==0)
            { f=0; break;}
            else f=n*i;
        }
        i++;
    }
    return f;
}

int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    long num;
    for(int i=1;i<=t;i++)
    {
        cin>>num;
        int flag=-1;
        if(num==0) flag=0;
        else{
            flag = check(num);
        }
        cout<<"Case #"<<i<<": ";
        if(flag==0) cout<<"INSOMNIA\n";
        else cout<<flag<<"\n";
    }
    return 0;
}
