#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;


bool at_least(int n, string str)
{
	bool ant = false;
	if( (int)str.size() < n )
	{
		return false;
	}

	int count = 0;
	for (int i = 0; i < (int)str.size(); ++i)
	{
		if (ant == false)
		{
			count = 0;
		}

		if(str[i] != 'a' and str[i] != 'e' and str[i] != 'i' and str[i] != 'o' and str[i] != 'u' )
		{
			count++;
			ant = true;
		}
		else
			ant = false;
		if(count >= n)
		{
			return true;
		}
	}
	return false;
}

void solve(int num_caso)
{
	int n; 
	string nombre, subnombre;
	int ocurrences = 0;

	cin >> nombre >> n;
	//cout << nombre << " " << n << "\n";

	int len_nombre = nombre.size();


	for (int i = 0; i < len_nombre; ++i)
	{
		for (int j = i+1; j <= len_nombre; ++j)
		{
			subnombre = nombre.substr(i,j-i);
			//cout << subnombre << "\n";
			if (at_least(n, subnombre) == true)
			{
				ocurrences++;
				//cout << "-----\n";
			}
		}
	}

	printf("Case #%d: %d\n", num_caso, ocurrences );
}


int main()
{
	int casos;
	scanf("%d", &casos);
	for(int i=1; i<=casos; ++i)
	{
		solve(i);
	}
}