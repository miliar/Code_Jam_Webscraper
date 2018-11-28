#include <iostream>
#include <string>
#include <stack>
#include <cstdlib>
#include <sstream>
#include <cmath>

using namespace std;

int TEST_CASES;
int A,B;
int quadrati[1000];

bool is_palindromo(int n)
{
	ostringstream o;
	o << n;
	string s = o.str();
	int dim = s.size();
	for (int i = 0; i < dim/2; i++)
		if (s.at(i) != s.at(dim -i -1))
			return 0;
	return 1;
}

void crea_quadrati()
{
	for (int i = 1; i < 31; i++)
		quadrati[i*i] = 1;
}
			
	
int main()
{
    cin >> TEST_CASES;
    crea_quadrati();
    int cont;
    for (int c = 0; c < TEST_CASES; c++)
    {
		cin >> A >> B;
		cont = 0;
		for ( int i = A; i <= B; i++)
			if (quadrati[i] && is_palindromo(i) && is_palindromo((int)sqrt(i)))
			{
				cont++;
				//cout << i << endl;
			}
		cout << "Case #" << c+1 << ": "<< cont << endl ;
    }
    return 0;
}
