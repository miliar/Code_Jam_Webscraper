#include<cstdio>
#include<iostream>

using namespace std;

string str;
string aux;
int T;

int main()
{
	cin >> T;
	
	for(int it=0 ; it<T ; it++)
	{
		cin >> str;
		aux = str[0];
		for(int it_s=1 ; it_s<str.size() ; it_s++)
		{
			if(str[it_s] >= aux[0])
			{
				aux = str[it_s] + aux; 
			}
			else
			{
				aux = aux + str[it_s]; 
			}
		}
		
		cout << "Case #" << it+1 << ": " << aux << endl;
	}

return 0;
}