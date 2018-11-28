#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double float64;

long long mul(long long a,long long b,long long MOD)
{
	long long a_high=	a/1000000000;
	long long a_low =	a%1000000000;

	long long b_high=	b/1000000000;
	long long b_low =	b%1000000000;

	long long result = (a_high*b_high)%MOD;
	for(int i=0;i<9;i++)
		result=(result*10)%MOD;

	result=(result+a_high*b_low+a_low*b_high)%MOD;
	for(int i=0;i<9;i++)
		result=(result*10)%MOD;

	result=(result+a_low*b_low)%MOD;
	return result;
}

long long p(long long a,long long b,long long MOD)
{
	if(b==0) return 1;

    long long x=p(a,b/2,MOD);

    if((b&1)==0)
	   return mul(x,x,MOD);
    else
	   return mul(mul(x,x,MOD),a,MOD);
}

bool fermat(long long num)
{
    int iterations =1000;
	if(num==1)
		return false;
	if(num==2)
		return true;
	else
	{
		for(int i=0;i<iterations;i++)
		{
			long long a=(rand()%(num-2))+2;

			if(p(a,num-1,num)!=1) return false;
		}
	}
	return true;
}

ll factor(ll n)
{
  ll x = sqrt(n);
    for(ll i=2;i<=x;i++)
    {
        if(n%i==0)
            return i;
    }
    return -1;
}
long long  mul_mod(long long  a, long long  b, long long  m){
   long long  y = (long long )((float64)a*(float64)b/m+(float64)1/2);
   y = y * m;
   long long  x = a * b;
   long long  r = x - y;
   if ( (long long)r < 0 ){
      r = r + m; y = y - 1;
   }
   return r;
}


long long pot(long long a, long long b, long long c){
   if(b == 0) return 1;
   if(b == 1) return a%c;
   long long  resp = pot(a,b>>1,c);
   resp = mul_mod(resp,resp,c);
   if(b&1)
      resp = mul_mod(resp,a,c);
}

bool isPrime(long long n){
   long long  d = n-1;
   long long  s = 0;
   if(n <=3 || n == 5) return true;
   if(!(n&1)) return false;
   while(!(d&1)){ s++; d>>=1; }
   for(long long  i = 0;i<32;i++){
      long long  a = rand();
      a <<=32;
      a+=rand();
      a%=(n-3); a+=2;
      long long  x = pot(a,d,n);
      if(x == 1 || x == n-1) continue;
      for(long long  j = 1;j<= s-1;j++){
         x = mul_mod(x,x,n);
         if(x == 1) return false;
         if(x == n-1)break;
      }
      if(x != n-1) return false;
   }
   return true;
}


int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        OF << "Case #" << 1 << ":\n";
        int n,j; IF >> n >> j;

         int count=0;
         int xx=(1<<(n-2));

        for(int i=0;i<xx;i++)
        {
            int tt=i,p=0,bin[20]={0};
            ll numb[12]={0};
            while(tt)
            {
                bin[p++] = tt%2;
                tt /= 2;
            }
            int flag=0;
            for(int b=2;b<=10;b++)
            {
                ll num=1LL+pow(b,n-1);
                int po=1;
                for(int in=n-3;in>=0;in--)
                {
                    num += 1LL*pow(b,po)*bin[in];
                    po++;
                }
                numb[b-2]=num;
                if(isPrime(num) && fermat(num))
                {
                    flag=1; break;
                }
            }
            if(!flag)
            {
                int fa[10],ff=0;
                for(int i=0;i<9;i++)
                {
                    fa[i] = factor(numb[i]);
                    if(fa[i]==-1)
                    {
                        ff=1; break;
                    }
                }
                if(ff==0){
                count++;
                OF << 1;
                for(int in=0;in<=n-3;in++)
                    OF << bin[in];
                OF << 1 << " ";
                for(int i=0;i<9;i++)
                    OF << factor(numb[i]) << " ";
                OF << "\n";
                }

            }
            if(count>=j)
                break;
        }
    }
    OF.close(); IF.close();
}


