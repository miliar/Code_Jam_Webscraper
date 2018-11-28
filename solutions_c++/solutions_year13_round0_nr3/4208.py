#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
using namespace std;
bool ispal(long long n)
{
    string str;
    while (n>0)
    {
        str+=((n%10)+'0');
        n/=10;
    }
    bool pal=1;
    int i=0;
    while (i<=str.size()/2)
    {
        if (str[i]!=str[str.size()-1-i])
            pal=0;
        i++;
    }
    return pal;
}
int main (){
  //  freopen ("C-large-1.in","r",stdin);
   // freopen ("outputlarge.txt","w",stdout);
    vector <long long> FS;
    int storevar=0;
    long long i=1;
    while (i*i<=10e14)
    {
        if (ispal(i)&&ispal(i*i))
            FS.push_back(i*i);
        i++;
    }
    storevar=0;
    while (storevar<FS.size()){
        printf("%lld\n",FS[storevar]);
        storevar++;
    }
    long long a,b;
    int count,t,T=1;
    scanf ("%d",&t);
    while (t--)
    {
        scanf("%lld %lld",&a,&b);
        storevar=0;
        count=0;
        while (storevar<FS.size())
        {
            if (FS[storevar]>=a&&FS[storevar]<=b)
                count++;
            storevar++;
        }
        printf("Case #%d: %d\n",T,count);
        T++;
    }

}
