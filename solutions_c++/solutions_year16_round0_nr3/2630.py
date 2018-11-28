/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

string coin="";
int64_t out[11];
int64_t dem=0;
int64_t J,N;

int64_t checkPrime(int64_t x)
{
    for(int64_t i=2; i<=sqrt(x); i++)
        if(x%i==0) return i;
    return 0;
}

int64_t mu(int64_t x, int64_t n)
{
    int64_t res=1;
    for(int64_t i=1; i<=n; i++) res*=x;
    return res;
}

int64_t base(string x, int64_t n)
{
    int64_t res=0, d=0;
    for(int64_t i=x.length()-1; i>=0; i--)
    {
        res+=(x[i]-48)*mu(n,d++);
    }
    return res;
}

void init()
{
    for(int64_t i=1; i<=N; i++) coin+="0"; coin[0]='1'; coin[N-1]='1';
}

bool testOK()
{
    for(int64_t i=2; i<=10; i++)
    {
        int64_t num=base(coin,i);
        out[i]=checkPrime(num);
        if(out[i]==0) return false;
    }
    return true;
}

void duyet(int64_t x)
{
    if(dem==J) return;
    for(int64_t i=0; i<2; i++)
    {
        coin[x]=i+48;
        if(x==N-2)
        {
            if(testOK())
            {
                cout<<coin<<' ';
                for(int64_t i=2; i<=10; i++)
                    cout<<out[i]<<' ';
                cout<<"\n";
                dem++;
            }
        }
        else duyet(x+1);
    }
}

int main()
{
#ifdef gsdt
    freopen("c-small-attempt.in","r",stdin);
    freopen("c-small-attempt.out","w",stdout);
#endif // gsdt

    cout<<"Case #1:\n";
    //cout<<checkPrime(10);
    //coin="100001";
    //cout<<testOK()<<endl;
    cin>>J;
    cin>>N>>J;
    init();
    duyet(1);

    return 0;
}

