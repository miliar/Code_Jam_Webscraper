#include<stdio.h>
long long raise(long long x, long long y)
{
    long long sign=1;
    if(x<0)
    {
        if(y%2==1)
            sign=-1;
        x=-x;
    }

    if(x==1)
        return sign;
    else if(x==3)
    {
        switch(y%4)
        {
            case 0: return 1*sign;
                    break;
            case 1: return 3*sign;
                    break;
            case 2: return -1*sign;
                    break;
            case 3: return -3*sign;
                    break;
        }
    }
    else if(x==4)
    {
        switch(y%4)
        {
            case 0: return 1*sign;
                    break;
            case 1: return 4*sign;
                    break;
            case 2: return -1*sign;
                    break;
            case 3: return -4*sign;
                    break;
        }
    }
    else
    {
        switch(y%4)
        {
            case 0: return 1*sign;
                    break;
            case 1: return 5*sign;
                    break;
            case 2: return -1*sign;
                    break;
            case 3: return -5*sign;
                    break;
        }

    }
}
long long mul(long long x , long long y)
{
    long long sign=1;
    if(x<0)
    {
        x=-x;
        sign*=-1;
    }
    if(y<0)
    {
        y=-y;
        sign*=-1;
    }
    if(x==1 || y==1)
    {
        return sign*(x*y);
    }
    else if(x==y)
    {
        return -1*sign;
    }
    else if(x==3)
    {
        if(y==4)
            return 5*sign;
        else
            return -4*sign;
    }
    else if(x==4)
    {
        if(y==5)
            return 3*sign;
        else
            return -5*sign;
    }
    else
    {
        if(y==3)
            return 4*sign;
        else
            return -3*sign;
    }
}
int main()
{
    long long j,i,t,l,x,a[100006],p,k,one;
    char tmp[10006];
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lld%lld",&l,&x);
        scanf("%s",tmp);
        one=1;
        for(j=0;j<l;j++)
        {
            //i=3 j=4 k=5 1=1 -1=-1
            if(tmp[j]=='i')
                a[j]=3;
            else if(tmp[j]=='j')
                a[j]=4;
            else
                a[j]=5;

            one=mul(one,a[j]);
        }

        if(x<=8)
        {
            p=l;
            for(j=1;j<x;j++)
            {
                for(k=0;k<l;k++)
                {
                    a[p]=a[p-l];
                    p++;
                }
            }

            //actual code
            p=1;
            long long curr=a[0];
            long long found=0;
            if(curr==3)
            {
                found=1;
            }
            while(found!=1 && p<(l*x))
            {
                curr=mul(curr,a[p]);
                p++;
                if(curr==3)
                    found=1;
            }
            curr=1;
            while(found!=2 && p<(l*x))
            {
                curr=mul(curr,a[p]);
                p++;
                if(curr==4)
                    found=2;
            }
            curr=1;
            while(p<(l*x))
            {
                curr=mul(curr,a[p]);
                p++;
            }
            if(curr==5)
                printf("Case #%lld: YES\n",i);
            else
                printf("Case #%lld: NO\n",i);
        }
        else
        {
            p=l;
            for(j=1;j<8;j++)
            {
                for(k=0;k<l;k++)
                {
                    a[p]=a[p-l];
                    p++;
                }
            }

            p=1;
            long long curr=a[0];
            long long found=0;
            if(curr==3)
            {
                found=1;
            }
            while(found!=1 && p<(l*8))
            {
                curr=mul(curr,a[p]);
                p++;
                if(curr==3)
                    found=1;
            }
            curr=1;
            while(found!=2 && p<(l*8))
            {
                curr=mul(curr,a[p]);
                p++;
                if(curr==4)
                    found=2;
            }
            curr=1;

            if(found!=2)
            {
                printf("Case #%lld: NO\n",i);
            }
            else
            {
                while(p<(l*8))
                {
                    curr=mul(curr,a[p]);
                    p++;
                }
                curr = mul(curr,raise(one,x-8));

                if(curr==5)
                    printf("Case #%lld: YES\n",i);
                else
                    printf("Case #%lld: NO\n",i);
            }
        }
    }
    return 0;
}
