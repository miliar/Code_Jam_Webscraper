#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
typedef long long lld;

lld mass[10000003];
lld lenm=0;
lld binaryA(lld target)
{
    lld l=1,r=lenm,mid;
    while (l<=r)
    {
        mid=(l+r)/2;
        if (mass[mid]<target)
        {
            l=mid+1;
        }
        else
        {
            if (mid!=l&&mass[mid-1]>=target)
            {
                r=mid-1;
                continue;
            }
            else return mid;
        }
    }
    return -1;
}
lld binaryB(lld target)
{
    lld l=1,r=lenm,mid;
    while (l<=r)
    {
        mid=(l+r)/2;
        if (mass[mid]>target)
        {
            r=mid-1;
        }
        else
        {
            if (mid!=r&&mass[mid+1]<=target)
            {
                l=mid+1;
                continue;
            }
            else return mid;
        }
    }
    return -1;
}
bool Palindrome(lld num)
{
    char cn[20];
    lld l,r,i,leng=0,cp=num;
    while (cp>0)
    {
        leng++;
        cn[leng]=cp%10;
        cp/=10;
    }
    l=1;
    r=leng;
    while (l<=r)
    {
        if (cn[l]!=cn[r]) return false;
        l++;
        r--;
    }
    return true;
}
int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    lld t,i,j,a,b,ind1,ind2,v;
    for (i=1;i<=10000001;i++)
    {
        v=i*i;
        if (Palindrome(v)&&Palindrome(i))
        {
            lenm++;
            mass[lenm]=v;
        }
    }
    scanf("%lld",&t);
    for (i=1;i<=t;i++)
    {
        scanf("%lld %lld",&a,&b);
        ind1=binaryA(a);
        ind2=binaryB(b);

        printf("Case #%lld: ",i);
        if (ind1==-1||ind2==-1||ind1>ind2)
        {
            printf("0\n");
        }
        else
        {
            printf("%lld\n",ind2-ind1+1);
        }
    }
}
