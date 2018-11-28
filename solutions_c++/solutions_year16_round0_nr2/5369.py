#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int resolver(vector<char> vec)
{
	if (vec.size() == 1)
	{
		if (vec.at(0) == '-')
		{	return 1; }
		else if (vec.at(0) == '+')
			return 0;
	}
	else if (vec.size() == 2)
		{
			if ((vec.at(0) == '-') && (vec.at(1) == '+'))
			{	return 1; }
			else if ((vec.at(0) == '+') && (vec.at(1) == '-'))
				return 2;
			
		}
		else
		{
			char ult = vec.back();
			vec.pop_back();
			char antult = vec.back();
			vec.pop_back();
			
			if ((ult == '-') && (antult == '+'))
			{
				vec.push_back(antult);
				return 2 + resolver(vec);
			} 
			else if ((ult == '+') && (antult == '-'))
			{
				vec.push_back(antult);
				return resolver(vec);
			}
			
			
		}
	
}

int main(void) {
    /* number of test cases */
    int t;
    long n;
    char c,ant;
    string linea;
    cin >> t;

	getline(cin,linea); // para consumir la primera linea de T

    for(int i=1; i <= t; i++) { //loops for each case
        vector<char> vc;
		getline(cin,linea);
		ant = linea.at(0);
		vc.push_back(ant);
		
		for (int j=1; j<linea.length(); j++)
		{
			if (linea.at(j)!=ant) 
			{
				ant = linea.at(j);
				vc.push_back(ant);
			}
        }
        
        int cantidad = resolver(vc);
        
		cout << "Case #" << i << ": " << cantidad << endl;
        
    }

    return 0;

}

