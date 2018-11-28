#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;
double count(fstream &plik);
int main()
{
	fstream input;
	input.open("B-large.in");
	
	double result;
	int T;// liczba prob
	input >> T; // wczytujemy ja do pliku
	
	for(int i = 1; i<=T; i++)
	{
		cout << "Case #" << i << ": "; // gotowe
		result = count(input);
		printf("%.7lf", result);
		printf("\n");
	}
	
	return 0;
}
double count(fstream &plik)
{
	double cps = 2;
	double help;
	double cookies = 0;
	double farm_cost;
	double extra_cps; // dodatkowe CPS ktore dostajemy za farmę
	double fin_cookies;
	plik >> farm_cost;
	plik >> extra_cps;
	plik >> fin_cookies;
	double seconds_sum = 0;
	double seconds_temp = 0;
	while(cookies<fin_cookies)
	{
		help = fin_cookies/(cps+extra_cps) + farm_cost/cps; // czas potencjalny 
		if((fin_cookies/cps < help) || fin_cookies<farm_cost) // jesli czas zebrania wszystkich ciastek jest krotszy niz czas zebrania na farmę + czas zebrania wszystkich ciastek 
		                                                      // lub po prostu farma kosztuje wiecej niz zebrac musimy ciastek
			{
				seconds_temp += (fin_cookies - cookies)/cps;
				return seconds_temp;
			}
		else
		{
			seconds_temp += farm_cost/cps; // budujemy farmę
			cps+=extra_cps;
			cookies = 0; // zerujemy ilość ciastek
		}
				
	} // wychodząc z tej pętli mamy juz odpowiednia ilosc ciastek. 
	return seconds_temp;
}
