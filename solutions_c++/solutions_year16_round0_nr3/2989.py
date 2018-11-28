#include <iostream>
#include <string>
#include <cmath>
using namespace std;

long long ipow(int l,int si)
{
    if(si==0)return 1;
    return l*ipow(l,si-1);
}

int dec(long long a,int l)
{
    long long s=0;
    int si=0;
    while(a!=0)s+=(a%2)*ipow(l,si),si++,a/=2;
    int i;
    for(i=2;i<=sqrt(s);i++)if(s%i==0)return i;
    return 0;
}

void ot(long long a,int re[9],int n)
{
    string s="";
    int l=0;
    while(a!=0)s=(char)('0'+(a%2))+s,a/=2,l++;
    while(l<n)s='0'+s,l++;
    cout<<s;
    int i;
    for(i=0;i<9;i++)cout<<" "<<re[i];
    cout<<endl;
}

int main()
{
    int tc;
    cin>>tc;
    cout<<"Case #1:"<<endl;
    int n,j;
    cin>>n>>j;
    long long a=1<<(n-1),lm=1<<n;
    int b=0;
    while(a<lm&&b<j)
    {
        //cout<<a<<endl;
        if(a%2==0){a++;continue;}
        int re[9],i;
        re[8]=dec(a,10);
        if(re[8]==0){a++;continue;}
        for(i=0;i<8;i++)
        {
            re[i]=dec(a,i+2);
            if(re[i]==0)break;
        }
        if(i!=8){a++;continue;}
        ot(a,re,n);
        a++,b++;
    }
    return 0;
}
