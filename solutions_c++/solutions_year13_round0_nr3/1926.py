#include<cstdio>
#include<vector>

#define pb push_back



using namespace std;

long long T,A,B;
vector <long long> V;
long long  Solve(long long  x)
{
	long long  i,s=0;
	for(i=0;i<V.size();i++)
		if(V[i] <= x)
			s++;
		else
			break;
	return s;
}
void Read()
{
	long long  i;
	scanf("%lld",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%lld %lld",&A,&B);
		printf("Case #%lld: %lld\n",i,Solve(B)-Solve(A-1));
	}
}
bool isPal(long long  x)
{
	long long  i,L=0;
	long long  D[30];
	while(x)
	{
		D[++L]=x%10;
		x/=10;
	}
	for(i=1;i<=L/2;i++)
		if(D[i] != D[L-i+1])
			return 0;
	return 1;
}
void Init()
{
	long long  i;
	for(i=1;i<=10000000;i++)
		if(isPal(i) && isPal(i*i))
			V.pb(i*i);
}
int main()
{
	Init();
	Read();
	return 0;
}
