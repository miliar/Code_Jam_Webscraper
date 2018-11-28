#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int t,i,a,b,k,t1,t2,div,x,l,r,f,flag0,flag1,count;
    double sq;
    scanf("%d",&t);
    k=0;
    while(t--)
    {
        scanf("%d%d",&a,&b);
        count=0;
        for(i=a;i<=b;++i)
        {
            t2=i;
            sq=sqrt(t2);
            t1=(int)sq;
            if(t1!=sq)
            continue;
            else
            {
                f=flag0=flag1=0;
                
                div = 1;
                x=t1;
                while (x / div >= 10)
                div *= 10;
                while (x != 0) 
                {
                    l = x / div;
                    r = x % 10;
                    if (l != r)
                    {
                        f=1;
                        break;
                    }
                    x = (x % div) / 10;
                    div /= 100;
                }
                if(f==0)
                flag0=1;
                
                f=0;
                x=t2;
                div = 1;
                while (x / div >= 10)
                div *= 10;
                while (x != 0) 
                {
                    l = x / div;
                    r = x % 10;
                    if (l != r)
                    {
                        f=1;
                        break;
                    }
                    x = (x % div) / 10;
                    div /= 100;
                }
                if(f==0)
                flag1=1;
                
                if(flag1 && flag0)
                {
                    count++;
                    //cout<<t2<<endl;
                }
            }
        }
        printf("Case #%d: %d\n",++k,count);
    }            
    return 0;
}
