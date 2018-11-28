#include<bits/stdc++.h>

using namespace std;
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define M_PIl 3.141592653589793238462643383279502884L

const int MAX = (long long)1e8+1;
long long divs[MAX];

vector<int> primes;
vector<bool>isp(MAX,1);

bool check(long long x)
{
  if(x<=0){return false;}
  for(int i=0;(long long) primes[i] * primes[i] <= x && i<primes.size();i++)
  {
    if(x % primes[i] == 0)
      return false;
  }
  return true;
}

int lim,cnt,j,n; long long k;

long long power(long long x, long long p)
{
    long long ret=1;
    for(int i=0;i<p;i++)
    {
        ret*=x;
    }
    return ret;
}

void rec(int s, string str)
{
    if(cnt==j){return;}
    if(s==n-2)
    {
        str+="1"; vector<long long>num;
        for(int j=2;j<=10;j++)
        {
            k=0;
            for(int i=0;i<=str.size();i++)
            {
                if(str[i]=='1'){k+=power(j,str.size()-i-1);}
            }
            //cout<<str<<" "<<j<<" "<<k<<" "<<divs[k]<<endl;
            if(check(k)){return;}
        }
        for(int j=2;j<=10;j++)
        {
            k=0;
            for(int i=0;i<=str.size();i++)
            {
                if(str[i]=='1'){k+=power(j,str.size()-i-1);}
            }
            for(int i=2;i*i<=k;i++)
            {
                if(k%i==0){num.push_back(i); break;}
            }
        }
        cnt++;
        cout<<str;
        for(int i=2;i<=10;i++)
        {
            cout<<" "<<num[i-2];
        }
        cout<<endl;
    }
    else
    {
        rec(s+1,str+"0");
        rec(s+1,str+"1");
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    for(long long i=2;i<=MAX;i++)
    {
        if(isp[i])
        {
            primes.push_back(i);
            for(long long j=i*i;j<=MAX;j+=i)
            {
                isp[j]=0;
            }
        }
    }
	isp[0]=0; isp[1]=0; divs[0]=1; divs[1]=1;

    int t; cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>n>>j; cnt=0;
        cout<<"Case #"<<tc<<":"<<endl;
        rec(0,"1");
    }
    return 0;
}
