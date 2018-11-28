#include <iostream>
#include <string>
#include <fstream>
using namespace std; 

fstream fichier("Text.txt", ios::in);

void DoIt(int caseN){
	int max; 
	int fr = 0;
	int standing = 0 ;
	string od;
	fichier >> max;
	fichier >> od;

	char k = od[0];
	standing += atoi(&k);
	for (int i = 1; i < od.length(); i++)
	{
		if (standing < i)
		{
			int u = i - standing;
			fr += u;
			standing += u;	
		}
		char c = od[i];
		standing += atoi(&c);
	}
	cout << "Case #" << caseN << ": " << fr << endl;
}

int main(){

	
	int cases; 
	fichier >> cases; 

	for (int i = 0; i < cases; i++)
	{
		DoIt(i + 1);
	}
	return 0; 
}