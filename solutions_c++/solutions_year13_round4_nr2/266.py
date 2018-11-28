#include <fstream>
#include <algorithm>
#include <vector>

#define long long long
#define M 100


using namespace std;

ifstream cin ("input.txt");
ofstream cout("output.txt");

long n,m,p[M];

void pre(void){
	p[0]=1;
	for (int i=1; i<M; ++i){
		p[i]=2*p[i-1];
	}
}

bool fun(long n, long x, long m){
	if (x==0)
	return 1;
	
	if (m<=p[n-1])
	return 0;
	
	return fun(n-1, (x-1)/2, m-p[n-1]);
}

bool gun(long n, long x, long m){
	if (x==0)
	return m==p[n];
	
	if (m<=p[n-1])
	return gun(n-1, (x-1)/2, m);
	
	return 1;
}

void kill(void){
	long l=0,r=p[n]-1,mi;
	while (l<r){
		mi=(l+r)/2;
		if (fun(n,mi+1,m))
		l=mi+1;
		else
		r=mi;
	}
	
	cout<<l<<" ";
	
	l=0,r=p[n]-1;
	while (l<r){
		mi=(l+r)/2;
		if (gun(n,mi,m))
		r=mi;
		else
		l=mi+1;
	}
	
	cout<<p[n]-1-l<<"\n";
}



int main()
{
	int t;
	pre();
	cin>>t;
	for (int i=1; i<=t; ++i){
		cin>>n>>m;
		cout<<"Case #"<<i<<": ";
		kill();
	}
	return 0;
}

