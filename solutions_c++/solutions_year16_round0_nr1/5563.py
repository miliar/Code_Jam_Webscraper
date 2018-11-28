#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<string>

using namespace std;

long long int T;
long long int value;
int c[20];
int cont;
long long int it, aux;
string result;

void evaluate(long long int v)
{
	while( v>0 )
	{
		if(c[v%10] == 0)
		{
			cont ++;
			c[v%10] = 1;
		}
		v /= 10;
	}
	
	return;
}

int main()
{

	cin >> T;
	
	for(int j=0 ; j<T ; j++)
	{
		cont = 0;
		it = 1;
		for(int r=0 ; r<10 ; r++)
		{
			c[r] = 0;
		}
		result = "INSOMNIA";
		
		cin >> value;
		if(value > 0)
		{
			while(cont < 10)
			{
				aux = value * it;
				evaluate(aux);
				it ++;
			}
			result = std::to_string(aux);
		}
		
		cout << "Case #" << j+1<< ": " << result << endl;
	}

return 0;
}