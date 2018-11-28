#include<bits/stdc++.h>
//Definitions
#define LL long long
#define LLU unsigned long long
#define fora(var,end) for(int var=0;var<end;var++)
#define fore(var,start,end) for(int var=start;var<end;var++)
#define forit(it1,a) for(typeof(a.begin()) it1=a.begin();it1!=a.end();it1++)
#define pub push_back
#define fst first
#define snd second
#define MOD 1000000007
#define mkp make_pair
#define beg begin
#define ed end
#define pii pair<int,int>
#define all(v) v.begin(),v.end()
#define P(a,b) cout<<a<<" "<<b<<" "
#define PNL printf("\n")
#define vi vector<int>
#define vpi vector<pair<pair<int,int>,int> >
#define FL(a,n,x) fill(a,a+n,x)
#define db1(a) cout<<#a<<":"<<a<<endl;
#define db2(a,b) cout<<#a<<":"<<a<<" , "<<#b<<" : "<<b<<endl;
#define db3(a,b,c) cout<<#a<<":"<<a<<" , "<<#b<<":"<<b<<" , "<<#c<<":"<<c<<endl;
//AP_HAWKDOWN from hereon
using namespace std;
int p[200000];
vector<int> v;
int isprime(LL x)
{
    for(int i=0; i<v.size(); i++)
    {
        int h=v[i];

        if(h*h>x)
        {
            break;
        }
        if(x%h==0)
        {
            return h;
        }

    }
    return 0;
}
LL pw[100][100];
LL base[20];
int main()
{
    //freopen("INPUT.txt","r",stdin);
    freopen("OUTPUT.txt","w",stdout);
    int t;
    cin>>t;
    while(t--)
    {
    int N,J;
    cin>>N>>J;
//freopen("ip.cpp","r",stdin);
    for(int i=2; i<=100000; i++)
    {
        if(p[i]==0)
        {
            for(int j=2; i*j<=100000; j++)
            {
                p[i*j]=1;
            }
        }
    }
    for(int i=2; i<=100000; i++)
    {
        if(p[i]==0)
        {
            v.pub(i);
        }
    }

    for(LL i=2;i<=10;i++)
    {
        pw[i][0]=1;
        for(LL k=1;k<=20;k++)
        {
            pw[i][k]=pw[i][k-1]*i;
        }

    }
    cout<<"Case #1:\n";
    int num=0;
    for(int i=0; i<(1<<N-2); i++)
    {
        if(num==J)
        {
            break;
        }
        int flag=0;
        int x=2*i+1+(1<<(N-1));
        int ct=0;
        for(int k=0;k<=10;k++)
        {
            base[k]=0;
        }
        while(x>0)
        {
            if(x%2==1)
            {
                for(int k=2; k<=10; k++)
                {
                    base[k]+=pw[k][ct];
                }
            }
            ct++;
            x/=2;
        }
        for(int k=2;k<=10;k++)
        {
            if(isprime(base[k])==0)
            {
                flag=1;
                break;
            }

        }
        if(flag==0)
        {
            cout<<base[10]<<" ";
            for(int k=2;k<=10;k++)
            {
                cout<<isprime(base[k])<<" ";
            }
            num++;
            cout<<endl;
        }


    }
    }
    return 0;
}
