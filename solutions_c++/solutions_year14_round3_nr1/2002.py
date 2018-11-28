#include<iostream>
#include<stdio.h>
using namespace std;
int hcf(int a,int b)
{
    //assuming a>b
    while(a%b!=0)
    {
    	int temp=a;
    	a=b;
    	b=temp%b;
    }
    return b;
}
int ans()
{
    int p,q,dr=1,hcffpq,c=0;
    long double x=1,y;
        scanf("%d/%d",&p,&q);
        hcffpq=hcf(q,p);
        q=q/hcffpq;
        p=p/hcffpq;
        
        while(dr<q)
        {
            dr*=2;c++;
        }
        
        if(c>40 || dr!=q )return 0;
        
        y=(long double)p/q;
        
        for(int i=0;i<40;i++)
        if(y<=x&&y>=x/2)
        return (i+1);
        else
        x/=2;
        
        
}
int main()
{
    short t,tc=0;
    cin>>t;
    while(tc++<t)
    {
        int flag;
        flag=ans();
        if(flag==0)
        cout<<"Case #"<<tc<<": impossible"<<endl;
        else
        cout<<"Case #"<<tc<<": "<<flag<<endl;                  
    }
    return 0;
}
