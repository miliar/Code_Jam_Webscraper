#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>
using namespace std;
class Cookie
{
private:
	char *filename;
public:
	Cookie(char* Name)
	{

		filename = new char[100];
#pragma warning(disable: 4996) 
		strcpy(filename, Name);
#pragma warning(default: 4996)
		ifstream fin;
		ofstream Cookiess("Cookies1.txt");
		fin.open(filename);
		while (fin.fail())
		{
			cout << "File doesnt exist write the correct file name" << endl;
			cin >> *filename;
			fin.open(filename);
		}
		double rate = 2;
		double C;
		double F;
		double X;
		int cases;
		fin >> cases;
		int check = 0;
		while (check<cases)
		{

			fin >> C;
			fin >> F;
			fin >> X;
			double time = 0;
			while (((C / rate) + (X / (rate + F)) < (X / rate)))
			{
				time = time + (C / rate);
				rate = rate + F;
			}
			time = time + (X / rate);
			Cookiess << fixed << setprecision(7);
			Cookiess << "Case #" << check + 1 << ": " << time << "\n";
			rate = 2;
			check++;
		}
	}
};
void main()
{
	//I have created a class in which if you pass the name of a file of the given format it will give you the required
	// questions output
	Cookie check("Goo.txt");



}