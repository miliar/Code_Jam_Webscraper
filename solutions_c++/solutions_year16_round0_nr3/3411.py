#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;
typedef long long unsigned int ULL;

int done = 0;
ULL num, divi;
vector<ULL>divisors;

ULL get_rep(int a[20], int n, int base)
{
	ULL base_val = 1, prod=0;
	for(int i=n-1; i>=0; --i)
	{
		prod += (base_val * a[i]);
		base_val *= base;
	}
	
	return prod;
}

ULL isprime(ULL n)
{
	if(n==1 || n==2 || n==3 || n == 5 || n == 7)return 0;
	
	ULL limit = sqrt(n);
	
	for(ULL i=2; i<=limit; ++i)
	{
		if(n%i == 0)return i;
	}
	
	return 0;
}

void jamcoin(int a[20], int index, int n, int j)
{
	if(done >= j)return;
	
	if(index == 0)
	{
		//Take 1
		a[index]=1;
		jamcoin(a, index+1, n, j);
		if(done >= j)return;
		
		return;
	}
	
	//Check if a valid jamcoin
	if(index == n-1)
	{
		//Take 1
		a[index]=1;
//		cout<<"The array formed: ";
//		for(int i=0;i<n;++i)printf("%d", a[i]);
//		cout<<endl;
		
		divisors.clear();
		
		for(int base=2;base<=10;++base)
		{
			num = get_rep(a, n, base);
			divi = isprime(num);
			
			if(divi == 0)return;
			
			//cout<<"Number in base "<<base<<" is "<<num<<" and divisor is "<<divi<<endl;
			divisors.push_back(divi);
		}	
		
		++done;
		for(int i=0;i<n;++i)printf("%d", a[i]);
		printf(" ");
		for(int i=0;i<9;++i)printf("%llu ", divisors[i]);
		printf("\n");
		//system("pause");
		
		return;
	}
	
	//Take 0
	a[index]=0;
	jamcoin(a, index+1, n, j);
	if(done >= j)return;
	
	//Take 1
	a[index]=1;
	jamcoin(a, index+1, n, j);
	if(done >= j)return;
}

int main()
{
	LL t, c, n, j;
	
	scanf("%lld\n", &t);
	c = 1;
	
	while(t--)
	{
		scanf("%lld %lld", &n, &j);
		
		int a[20];
		
		printf("Case #%lld:\n", c);
		++c;
		
		done = 0;
		jamcoin(a, 0, n, j);
	}
	
}
