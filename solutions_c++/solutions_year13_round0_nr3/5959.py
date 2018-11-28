#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int esPalin(int n)
{
	if(n<10) return true;
	if(n<100) return (n%10 == n/10);
	return (n%10 == n/100);
}

int main()
{
	freopen("cs.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int a,b;
		cin>>a>>b;
		int contador = 0;
		int pisoA = sqrt(a);
		if(pisoA * pisoA != a) pisoA++;
		int pisoB = sqrt(b);
		for(int i=pisoA;i<=pisoB;i++)
		{
			if(esPalin(i) && esPalin(i*i)) contador++;
		}
		cout<<"Case #"<<t+1<<": "<<contador<<endl;
	}
}
