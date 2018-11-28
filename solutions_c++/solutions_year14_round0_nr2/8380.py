#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

void main()
{


	long double cookieNumber = 2;
	long double cookieincrement;
	long double CookieValue;
	long double FarmCost;

	int caseNumber = 0;

	long double cookietime1 = 0;
	long double cookietime2 = 0;
	long double nextcookie1 = 0;
	long double nextcookie2 = 0;


	fstream myFile;
	fstream out;
	string currentLine;

	int lineFlag = 0;

	myFile.open("read.in");
	out.open("secondoutput.txt");

	cout.precision(10);

	while (getline(myFile, currentLine))
	{
		myFile >> FarmCost >> cookieincrement >> CookieValue;


		while (true)
		{
			cookietime1 = 0 + nextcookie2 + (CookieValue / cookieNumber);

		mkl:

			nextcookie1 = (FarmCost / cookieNumber);


			cookietime2 = 0 + nextcookie2 + nextcookie1 + (CookieValue / (cookieNumber + cookieincrement));


			if (cookietime1 < cookietime2)
			{
				caseNumber = caseNumber + 1;

				out << "Case #" << caseNumber << ": " << setprecision(10) << cookietime1 << endl;

				goto nextLine;
			}

			else
			{
				cookieNumber = cookieNumber + cookieincrement;

				nextcookie2 = cookietime2 - (CookieValue / cookieNumber);

				cookietime1 = cookietime2;


				goto mkl;

			}
		}
	nextLine:

		cookietime1 = 0;
		cookietime2 = 0;
		nextcookie2 = 0;
		nextcookie1 = 0;
		cookieNumber = 2;

		continue;
	}




	myFile.close();
	out.close();

	getchar();
}
