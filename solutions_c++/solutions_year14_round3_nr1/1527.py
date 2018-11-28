#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<cmath>
#define ll long long int
using namespace std;

ll gcd(ll a,ll b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}

int main()
{
    fstream f1,f2;
    f1.open("input.in",ios::in);
    f2.open("output.txt",ios::out);
    int t,w=1;
    f1>>t;
    while(t--)
    {
        ll i,j,k,m,n,l;
        string s;
        ll temp=0;
        f1>>s;
        l=s.length();
        for(i=0;i<l;i++)
        {
            if(s[i]!='/')
            {
                temp=temp*10+s[i]-'0';
            }
            else
                break;
        }
        ll a=temp;
        temp=0;
        for(i=i;i<l;i++)
        {
            if(s[i]!='/')
            {
                temp=temp*10+s[i]-'0';
            }
        }
        ll b=temp;
        //cout<<a<<" "<<b<<"\n";
        ll temp1;
        temp1=gcd(a,b);
        b/=temp1;
        if(b&(b-1))
        {
            f2<<"Case #"<<w<<": "<<"impossible"<<"\n";
        }
        else
        {
            ll co=0;
            a/=temp1;
            while(a<b)
            {
                b/=2;
                co++;
            }
            f2<<"Case #"<<w<<": "<<co<<"\n";
        }

        w++;
    }
    return 0;
}
