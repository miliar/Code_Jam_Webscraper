#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sl(n) scanf("%lld",&n)

bool has[2000009];
ll ar[2000009];
ll a[10];

ll to_binary(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%2;
        val+=mod*m;
        m=m*10;
        n=n/2;
    }
    return val;
}

ll to_three(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*3;
        n=n/10;
    }
    return val;
}

ll to_four(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*4;
        n=n/10;
    }
    return val;
}

ll to_five(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*5;
        n=n/10;
    }
    return val;
}

ll to_six(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*6;
        n=n/10;
    }
    return val;
}

ll to_seven(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*7;
        n=n/10;
    }
    return val;
}

ll to_eight(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*8;
        n=n/10;
    }
    return val;
}

ll to_nine(ll n)
{
    ll m=1,mod,val=0;
    while(n>0)
    {
        mod=n%10;
        val+=mod*m;
        m=m*9;
        n=n/10;
    }
    return val;
}
int main()
{
    ll a[50]={32769,32773,32775,32777,32781,32787,32793,32795,32799,32805,32811,32815,32817,32821,32823,32827,32829,32835,32841,32847,
               32855,32857,32859,32861,32863,32865,32871,32875,32877,32883,32885,32889,32891,32895,32901,32905,32913,32919,32923,32925,
               32935,32937,32953,32955,32961,32967,32973,32979,32985,32991};
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.in");

    if(!fin.is_open())
    {
        fout<<"file error";
    }
    else
    {
        ll t,n,j;
        fin>>t;
        fin>>n>>j;
        fout<<"Case #"<<1<<": \n";
        for(int i=0;i<50;i++)
        {
                ll j;
                ll m1=to_binary(a[i]);
                ll m3=to_three(m1);
                ll m4=to_four(m1);
                ll m5=to_five(m1);
                ll m6=to_six(m1);
                ll m7=to_seven(m1);
                ll m8=to_eight(m1);
                ll m9=to_nine(m1);

                fout<<m1<<" ";
                for(j=2;j<a[i]/2;j++)
                {
                    if(a[i]%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m3/2;j++)
                {
                    if(m3%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m4/2;j++)
                {
                    if(m4%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m5/2;j++)
                {
                    if(m5%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m6/2;j++)
                {
                    if(m6%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m7/2;j++)
                {
                    if(m7%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m8/2;j++)
                {
                    if(m8%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m9/2;j++)
                {
                    if(m9%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                for(j=2;j<m1/2;j++)
                {
                    if(m1%j==0)
                    {
                        fout<<j<<" ";
                        break;
                    }
                }
                fout<<endl;
        }
    }
}
