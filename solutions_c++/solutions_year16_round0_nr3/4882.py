#include <bits/stdc++.h>
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MOD 1000000007
#define ulli long long int
#define uli long int
#define maxsize 16

using namespace std;

unsigned int total,n,k=0;
bitset <maxsize> b;
map <ulli,bool> m;
ulli factor(ulli x)
{   ulli i=floor(sqrt(x));
    for(;i>=2;i--)
        if(x%i==0) return i;
    return i;
}
ulli notprime(ulli n)
{   for(ulli i=2;i*i<=n;i++)
    {   if(n%i==0)
            return i;
    }
    return -1;
}
ulli basex(ulli x)
{   ulli i,num=1,p=x;
    for(i=1;i<maxsize;i++)
    {   if(b[i]==1)
            num+=p;
        p*=x;
    }
    return num;
}
int f()
{   for(int i=2;i<=10;i++)
    {   if(notprime(basex(i))==-1)
            return 0;
    }
    return 1;
}
void setbit()
{   ulli i,j,p;
    p=(1<<(n-2));
    for(i=1;i<p;i++)
    {   for(j=0;j<=n-1;j++)
        {   if((i&(1<<j))>0)
                b[j+1]=1;
            else
                b[j+1]=0;
            b[0]=b[n-1]=1;
            if(f()==1&&m[basex(10)]==false)
            {   k++;
                cout<<b<<" ";
                for(int i=2;i<=10;i++)
                    cout<<factor(basex(i))<<" ";
                cout<<endl;
                m[basex(10)]=true;
            }
            if(k==total)
                return;
        }
    }
}
int main()
{   ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t,test;
    cin>>test;
    for(t=1;t<=test;t++)
    {   cout<<"Case #";
        cout<<t<<":"<<endl;
        cin>>n>>total;
        b.reset();
        setbit();
    }
    return 0;
}
