#include<iostream>
#include<cstring>
using namespace std;
int check(int[]);
void blea(int);
int main()
{
    int t;
    cin>>t;
    int n;
    for(int i=0;i<t;i++)
    {
        cin>>n;
      cout<<"Case #"<<i+1<<": ";
      blea(n);
      cout<<endl;
    }
    return 0;
}
void blea(int num)
{
    int flag;
    if(num==0)
    {
        cout<<"INSOMNIA";
    }
    else
    {
    int n;
    int c[10];
    memset(c,0,sizeof(c));
    int i=1;
    n=num;
    while(1)
    {
        //cout<<"iteration no " <<i;
        n=num*i;
        int m,r;
        m=n;
        //cout<<m;
        while(m)
        {
            r=m%10;
            c[r]=1;
            m=m/10;
        }
        //cout<<"out";
        i++;
        flag=check(c);
        if(flag==1)
        {
            cout<<n;
            break;
        }
        else{
            continue;
        }
    }
    }
}
int check(int c[])
{
    int flag=0;
    for(int i=0; i<10;i++)
    {
        if(c[i]>=1)
        {
            flag=1;
        }
        else{
            flag=0;
            break;
        }
    }
    return flag;

}
