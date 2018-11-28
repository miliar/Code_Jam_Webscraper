#include <bits/stdc++.h>

using namespace std;

// Rabin Karp Test taken from "https://ronzii.wordpress.com/2012/03/04/miller-rabin-primality-test/"

bool arr[100000900]= {0};
vector <int> pr;

long long mulmod(long long a, long long b , long long c)
{
    long long x=0,y=a%c;
    while(b>0)
    {
        if(b & 1)
        {
            x = (x+y)%c;
        }
        y=(y*2)%c;
        b>>=1;
    }
    return x%c;
}

long long modulo(long long a,long long b,long long c)
{
    long long y=a,x=1;
    while(b>0)
    {
        if(b & 1)
        {
            x = mulmod(x,y,c);
        }
        y = mulmod(y,y,c);
        b>>=1;
    }
    return x%c;
}

bool miller(long long p,int iterations)
{
    if(p<2) return false;
    if(p!=2 && p%2==0) return false;
    long long s = p-1;
    while(s%2==0)
    {
        s/=2;
    }
    for(int i=0; i<iterations; i++)
    {
        long long a = rand()%(p-1)+1,temp=s;
        long long mod = modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1)
        {
            mod = mulmod(mod,mod,p);
            temp*=2;
        }
        if(mod!=p-1 && temp%2==0)
        {
            return false;
        }

    }
    return true;
}

void sieve()
{
    int i,j,k;

    arr[0]=arr[1]=1;
    for (i=2; i<10050; ++i)
    {
        if (arr[i]==0)
        {
            j=2;
            while ((i*j)<=100000500)
            {
                arr[i*j]=1;
                j++;
            }
        }
    }
    for (i=2; i<100000500; ++i)
        if (arr[i]==0)
            pr.push_back(i);
}

long long int fastpow (long long int x, long long int y)
{
    long long int res=1;
    while (y>0)
    {
        if (y&1)
        {
            res=res*x;
            y--;
        }
        x=(x*x);
        y/=2;
    }
    return res;
}

int main()
{
    FILE *f1,*f2;

    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");

    int t,i,k,n,s;
    long long int j,m,l,p;
    sieve();

    fscanf (f1,"%d",&t);

    for (i=0; i<t; ++i)
    {
        fscanf (f1,"%d %d",&n,&k);
        long long int cnt=0;
        m=fastpow(2,15);
        l=fastpow(2,16);
        fprintf (f2,"Case #%d:\n",i+1);
        for (j=l-1; j>m; --j)
        {
            if (cnt==k)
                break;
            char str[40];
            p=j;
            s=n-1;
            while (p>0)
            {
                str[s]=(char)((p%2)+48);
                p/=2;
                s--;
            }
            str[n]='\0';
            if (str[n-1]=='0' || str[0]=='0')
                continue;
            //cout<<str<<endl;
            long long int x,y;
            vector <int> V;
            for (p=2; p<11; ++p)
            {
                x=0;
                for (s=0; s<n; ++s)
                {
                    y=str[s]-48;
                    x=x+y*fastpow(p,1LL*(n-1-s));
                }
                //cout<<p<<" "<<x<<endl;
                if (miller(x,40))
                    break;
                for (int z=0; z<pr.size(); ++z)
                    if (x%pr[z]==0)
                    {
                        V.push_back(pr[z]);
                        break;
                    }
            }
            if (V.size()==9)
            {
                fprintf (f2,"%s ",str);
                for (p=0; p<8; ++p)
                    fprintf (f2,"%d ",V[p]);
                fprintf (f2,"%d\n",V[8]);
                cnt++;
            }
        }
    }
    return 0;
}
