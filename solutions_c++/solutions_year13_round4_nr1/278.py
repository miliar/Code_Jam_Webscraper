#include <fstream>
#include <algorithm>
#include <vector>

#define long long long
#define p 1000002013ll
#define f first
#define s second
#define mp make_pair
#define M 1010


using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

long n,m,ans,a[M],f,c[M];
pair<long,long> b[M];

long fun(long k){
	long s=k*(2*n+1-k)/2;
	return s%p;	
}

void read(void){
	cin>>n>>m;
	
	ans=0;
	f=m;
	
	for (int i=0; i<m; ++i){
		long o,en,co;
		cin>>o>>en>>co;
		a[i]=o;
		c[i]=0;
		b[2*i]=mp(o,-co);
		b[2*i+1]=mp(en,co);
		ans=ans+co*fun(en-o);
		ans%=p;
	}
	
	m*=2;
}

void add(long h,long k){
	for (int i=0; i<f; ++i)
	if (a[i]==h){
		c[i]+=k;
		return;
	}
}

void del(long h, long k){
	for (int i=f-1;k>0 && i>=0; --i){
		long y=min(k,c[i]);
		k-=y;
		c[i]-=y;
		ans=ans-y*fun(h-a[i]);
		ans%=p;
	}
}

void kill(void){
	sort(b,b+m);
	sort(a,a+f);
	
	for (int i=0; i<m; ++i){
		long x=-b[i].s;
		long h=b[i].f;
		if (x>0)
		add(h,x);
		else
		del(h,-x);
	}
	
}



int main()
{
	int t;
	cin>>t;
	for (int i=1; i<=t; ++i){
		read();
		kill();
		ans%=p;
		if (ans<0)
		ans+=p;
		cout<<"Case #"<<i<<": "<<ans<<"\n";	
	}
	return 0;
}

