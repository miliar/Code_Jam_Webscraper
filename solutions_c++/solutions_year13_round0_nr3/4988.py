#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<cstdlib>
using namespace std;
vector<long> pl;
void pldrm()
{
    char a[10];
    long n,m,i,j,k;
    for(n=1;n<10;n++) pl.push_back(n);
    for(n=1;n<10;n++) pl.push_back(n*11);
    for(n=0;n<10;n++)
    {
        for(i=1;i<10;i++)
        {
            a[0]=i+48;
            a[1]=n+48;
            a[2]=i+48;
            a[3]='\0';
            m=atol(a);
            pl.push_back(m);
        }
    }
    for(n=1;n<10;n++)
    {
        for(i=0;i<10;i++)
        {
            a[0]=n+48;
            a[1]=i+48;
            a[2]=i+48;
            a[3]=n+48;
            a[4]='\0';
            m=atol(a);
            pl.push_back(m);
        }
    }
    for(n=1;n<10;n++)
    {
        for(i=0;i<10;i++)
        {
            for(j=0;j<10;j++)
            {
                a[0]=n+48;
                a[1]=i+48;
                a[2]=j+48;
                a[3]=i+48;
                a[4]=n+48;
                a[5]='\0';
                m=atol(a);
                pl.push_back(m);
            }
        }
    }
    for(n=1;n<10;n++)
    {
        for(i=0;i<10;i++)
        {
            for(j=0;j<10;j++)
            {
                a[0]=n+48;
                a[1]=i+48;
                a[2]=j+48;
                a[3]=j+48;
                a[4]=i+48;
                a[5]=n+48;
                a[6]='\0';
                m=atol(a);
                pl.push_back(m);
            }
        }
    }
    for(n=1;n<10;n++)
    {
        for(i=0;i<10;i++)
        {
            for(j=0;j<10;j++)
            {
                for(k=0;k<10;k++)
                {
                    a[0]=n+48;
                    a[1]=i+48;
                    a[2]=j+48;
                    a[3]=k+48;
                    a[4]=j+48;
                    a[5]=i+48;
                    a[6]=n+48;
                    a[7]='\0';
                    m=atol(a);
                    pl.push_back(m);
                }

            }
        }
    }
}
int main()
{
    pldrm();
    long test,t,a,b,temp,count,i,sq,num;
    freopen("C://Users//Sheemul//Downloads//C-small-attempt0.in","r",stdin);
    scanf("%ld",&test);
    for(t=1;t<=test;t++)
    {
        scanf("%ld %ld",&a,&b);
        temp=sqrt(a);
        if(temp*temp==a) a=temp;
        else a=temp+1;
        b=sqrt(b);
        count=0;
        for(i=0;;i++)
        {
            if(pl[i]>=a)
            {
                break;
            }
        }
        for(;pl[i]<=b;i++)
        {
            sq=pl[i]*pl[i];
            temp=sq;
            num=0;
            while(temp)
            {
                num=10*num+(temp%10);
                temp=temp/10;
            }
            if(num==sq) count++;
        }
        freopen("E://Anamul Kabir//output.txt","a",stdout);
        printf("Case #%ld: %ld\n",t,count);
    }
}
