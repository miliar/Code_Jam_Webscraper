#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	ofstream outfile("results.out");
	ifstream infile("B-large.in");    // infile is a name of our choosing
	if (!infile)		        // Did opening the file fail?
	{
		cerr << "Error: Cannot open input file!" << endl;
		return (1);
	}
	if (!outfile)		   // Did the creation fail?
	{
		cerr << "Error: Cannot create output file!" << endl;
		return (1);
	}

	int numCases;
	infile >> numCases;
	//infile.ignore(10000, '\n');


	outfile.setf(ios::fixed);    
	outfile.precision(7);

	for (int caseNum = 0; caseNum < numCases; caseNum++)
	{
		
		double cookiesPerSec = 2;
		double cookiesIHave = 0;
		double seconds = 0;

		double CookiesNeededToBuyFarm;
		double FarmExtraCookiePerSec;
		double XWinCookieNum;

		double secsUntilNextFarm;
		double secsUntilIWinWithNumCookiesNow;
		double secsUntilIWinAfterNextFarm;


		infile >> CookiesNeededToBuyFarm;
		infile >> FarmExtraCookiePerSec;
		infile >> XWinCookieNum;

		double zeroCookiesInstantAfterBuyingFarm = 0.0;
		secsUntilNextFarm = CookiesNeededToBuyFarm / cookiesPerSec;
		secsUntilIWinWithNumCookiesNow = (XWinCookieNum - cookiesIHave) / cookiesPerSec;
		secsUntilIWinAfterNextFarm = secsUntilNextFarm + (XWinCookieNum - zeroCookiesInstantAfterBuyingFarm) / (cookiesPerSec + FarmExtraCookiePerSec);


		//cout << "CookiesNeededToBuyFarm " << CookiesNeededToBuyFarm << endl;
		//cout << "FarmExtraCookiePerSec " << FarmExtraCookiePerSec << endl;
		//cout << "XWinCookieNum " << XWinCookieNum << endl;


		//cout << "secsUntilNextFarm" << secsUntilNextFarm << endl;
		//cout << "secsUntilIWinWithNumCookiesNow" << secsUntilIWinWithNumCookiesNow << endl;
		//cout << "secsUntilIWinAfterNextFarm" << secsUntilIWinAfterNextFarm << endl << endl;


		while (secsUntilIWinWithNumCookiesNow > secsUntilIWinAfterNextFarm)  // when should we just stop buying farms and wait

		{
			//buy farm
			seconds += secsUntilNextFarm;
			cookiesPerSec += FarmExtraCookiePerSec;

			secsUntilNextFarm = CookiesNeededToBuyFarm / cookiesPerSec;
			secsUntilIWinWithNumCookiesNow = (XWinCookieNum - cookiesIHave) / cookiesPerSec;
			secsUntilIWinAfterNextFarm = secsUntilNextFarm + (XWinCookieNum - zeroCookiesInstantAfterBuyingFarm) / (cookiesPerSec + FarmExtraCookiePerSec);

			//cout << "secsUntilNextFarm" << secsUntilNextFarm << endl;
			//cout << "secsUntilIWinWithNumCookiesNow" << secsUntilIWinWithNumCookiesNow << endl;
			//cout << "secsUntilIWinAfterNextFarm" << secsUntilIWinAfterNextFarm << endl << endl;

		}

		//secs to win
		seconds += secsUntilIWinWithNumCookiesNow;


		cout << "Case #" << caseNum + 1 << ": " << seconds << endl;

		outfile << "Case #" << caseNum + 1 << ": " << seconds << endl;
	}

	return 0;
}