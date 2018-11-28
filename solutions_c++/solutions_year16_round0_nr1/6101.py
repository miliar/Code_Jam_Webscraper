#include <iostream>
#include <bitset>
using namespace std;
unsigned long long n, ini, copia;
bitset <10> mibitset;
int digitos=10;

bool verdigitos()
{
	copia=n;
	while (copia)
	{
		if ( not mibitset[copia%10] )
		{	
			mibitset[copia%10]=true;
			--digitos;
		}
		copia /=10;
	}
	return digitos!=0;
}

int main()
{	
	int t, i;
	cin>>t;
	for (i=1; i<=t; ++i)
	{
		cin>>ini;
		if (not ini)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		mibitset.reset();
		n=0;
		digitos=10;
		do {n+=ini;}
		while ( verdigitos() );
		
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
}