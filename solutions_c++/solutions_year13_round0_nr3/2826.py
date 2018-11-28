#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<vector>
#define m 1005
#define ll long long
using namespace std;
vector<int>p;
bool check(ll n)
{
    ll temp=n,num=0;
    while(n)
    {
        num=(num*10)+(n%10);
        n=n/10;

    }
    if(num==temp)
        return true;
        return false;
}
void func()
{
    for(ll i=1;i*i<=(m+5);i++)
    {
        if(check(i)&&check(i*i))
            p.push_back(i*i);

    }
}
int main()
{
    FILE *fr,*fw;
    fr=fopen("C-small-attempt0.in","r");
    fw=fopen("outputC.txt","w");
    func();
    ll t,kase=1,l,h,ans=0;
   fscanf(fr,"%lld",&t);
    while(t--)
    {
        ans=0;
       fscanf(fr,"%lld %lld",&l,&h);
        int len=p.size();
       // cout<<len<<endl;
        for(ll i=0;i<len;i++)
            if(p[i]>=l&&p[i]<=h)
            ans++;
       fprintf(fw,"Case #%lld: %lld\n",kase++,ans);

    }




}
