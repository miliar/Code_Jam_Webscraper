#include <iostream>
#include <fstream>
#include <string>
using namespace std;
std::pair<int, string> pobierz(fstream &fil, fstream &output); 
int main()
{
 
	fstream plik;
	fstream output;
	output.open("output");
	plik.open("A-small-attempt3.in"); // otwarty został plik.
	int T; // liczba testów
	plik >> T; // wprowadzona została liczba testów do T. 
	for(int i = 1; i<=T; i++)
	{
		output << "Case #" << i << ": ";
	std::pair<int, string> check = pobierz(plik, output);
	if(check.second == "correct")
		output << check.first;
	else
		output << check.second;
	output << std::endl;
	}
	output.close();
	plik.close();
	

					
	
	
	return 0;
}

std::pair<int, string> pobierz(fstream &fil, fstream&output)
{
	int tab_1[4][4]; // tworzymy tablicę 4x4
	int choice_1;
	int tab_2[4][4];
	int choice_2;
	int tab_pom[4];
	fil >> choice_1; // pobieramy ktory rząd nas interesuje 
	for(int i = 0;i<4; i++)
		for(int j = 0;j < 4; j++)
			fil >> tab_1[i][j]; // wypelniamy tablicę.
	for(int i = 0; i<4; i++) // wybrany rząd wprowadzamy do tablicy pomocniczej. 
		tab_pom[i] = tab_1[choice_1-1][i]; // rzad jest kopiowany i przetrzymywany. 
		
	
	fil >> choice_2; // pobieramy ktory rzad nas interesuje za drugim razem. 
	for(int i = 0;i<4; i++)
		for(int j = 0;j < 4; j++)
			fil >> tab_2[i][j]; // wypelniamy tablicę drugą. 
	int count = 0;
	int ans = 0; // domyslna wartosc
	for(int i = 0; i<4; i++)
	{
		for(int j = 0; j<4; j++)
			if(tab_2[choice_2-1][j] == tab_pom[i])
			{
				count++;
				ans = tab_pom[i];
			}
	}
	std::pair<int, string> answer;
	if(count >1)
		answer.second = "Bad magician!";
	if(count == 1)
	{
		answer.first = ans;
		answer.second = "correct";
	}
	if(count == 0)
	{
		answer.second = "Volunteer cheated!";
		
	}
 
return answer;

					
}




