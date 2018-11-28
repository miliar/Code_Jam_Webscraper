#include <iostream>
#include <string>
#include <locale>
#include <sstream>

using namespace std;

int main()
{
	int t;
	
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int a;
	    cin >> a;
		int j = 1;
		string restantes = "0123456789";
		
		if(a == 0)
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		else
		{
			while(restantes != "")
			{
				string b;
				ostringstream converte;
				converte << a*j;  
				b = converte.str();
				for(int k = 0; k<b.length(); k++)
				{
					for(int l = 0; l < restantes.length(); l++)
					{
						if(restantes[l] == b[k])
						{
							restantes.erase(l, 1);
						}
					}
				}
				j++;
			}
			cout << "Case #" << i+1 << ": " << a*(j-1) << endl;
		}
		
	}
}