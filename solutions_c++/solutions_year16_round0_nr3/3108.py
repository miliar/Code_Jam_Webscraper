#include<bits/stdc++.h>
using namespace std;
vector<long long>v[60];
long long int b[40];
typedef unsigned long long ULL;
#define MAX 8700000
#define MAX2 1000
int a[(MAX>>6)+100];
int pri[6000005];
int siz;
void sieve()
{
	int i,j,k = 1,yy;
	a[0]=1;
	pri[k]=2;k++;
	for(i=3;i<MAX2;i=i+2)
	{
		if(!(a[i>>6]&(1<<((i>>1)&31))))
		{
			for(j=i*i,yy=i<<1;j<MAX;j=j+yy)
			{
				a[j>>6]=a[j>>6]|(1<<((j>>1)&31)) ;
			}
		}
	}
	for(i=3;i<MAX;i+=2)
	{
		if(!(a[i>>6]&(1<<((i>>1)&31))))
		{
			pri[k]=i;k++;
			if(k>=6000000)break;
		}
	}
	siz=k;
   	return;
}
ULL mulmod(ULL a, ULL b, ULL c){
	ULL x = 0,y = a%c;
	
	while(b>0){
		if(b&1) x = (x+y)%c;
		y = (y<<1)%c;
		b >>= 1;
	}
	
	return x;
}

ULL pow(ULL a, ULL b, ULL c){
	ULL x = 1, y = a;
	
	while(b>0){
		if(b&1) x = mulmod(x,y,c);
		y = mulmod(y,y,c);
		b >>= 1;
	}
	
	return x;
}

bool miller_rabin(ULL p, int it){
	if(p<2) return false;
	if(p==2) return true;
	if((p&1)==0) return false;
	
	ULL s = p-1;
	while(s%2==0) s >>= 1;
	
	while(it--){
		ULL a = rand()%(p-1)+1,temp = s;
		ULL mod = pow(a,temp,p);
		
		if(mod==-1 || mod==1) continue;
		
		while(temp!=p-1 && mod!=p-1){
			mod = mulmod(mod,mod,p);
			temp <<= 1;
		}
		
		if(mod!=p-1) return false;
	}
	
	return true;
}
 
long long fast_exp(long long int base, long long int exp) {
    long long  res=1;
    while(exp>0) {
       if(exp%2==1) res=(res*base);
       base=(base*base);
       exp/=2;
    }
    return res;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	sieve();
	int t;int k=1;
	scanf("%d",&t);
	while(t--)
	{
		long long n,J;
		scanf("%lld %lld",&n,&J);
		//n=16;
		//J=50;
		printf("Case #%d:\n",k);
		long long y=0;
		long long N=(1LL<<n);
		long long i,j;
		for(i=0;i<N;i++)
		{
			long long x;
			int co=0;
			int h=0;
			for(j=0;j<n;j++)
			{
				if(i&(1<<j))
				{
					b[h++]=1;
				}
				else
				{
					b[h++]=0;
				}
			}
			if(b[0]!=1||b[h-1]!=1)
			continue;
			for(int base=2;base<=10;base++)
			{
				x=0;
				for(j=0;j<h;j++)
				{
					x+=(fast_exp((long long)base,j))*b[j];
				}
				if(miller_rabin(x,18))
				{
					co=1;
					break;
				}
			}
			if(co==1)
			continue;
			long long d;
			int coo;
			for(int base=2;base<=10;base++)
			{
				x=0;
				coo=0;
				for(j=0;j<h;j++)
				{
					x+=(fast_exp((long long)base,j))*b[j];
				}
				
				d=x;
				for(j=2;j<=sqrt(d);j++)
				{
					if(d%j==0)
					{
						coo=1;
						v[y].push_back(j);
						break;	
					}
				}
				if(coo==0)
				{
					co=1;
					break;
				}
			
			}
			if(co==1)
			{
				v[y].clear();
				continue;
			}
			for(j=h-1;j>=0;j--)
			printf("%lld",b[j]);
			printf(" ");
			/*x=0;
			for(int base=2;base<=10;base++){
				x=0;
			for(j=0;j<h;j++)
			{
					x+=(fast_exp(base,j))*b[j];
			}
			cout<<x<<" ";}*/
			for(j=0;j<v[y].size();j++)
			printf("%lld ",v[y][j]);
			printf("\n");
			y++;
			if(y==J)
			break;
		}
	}
}
