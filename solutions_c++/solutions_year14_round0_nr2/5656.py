#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

void main()
{

	
	long float numberOfCookies = 2;
	long float cookieIncrementValue;
	long float targetCookieValue;
	long float cookieFarmCostValue;


	int totalTimeByCurrentCookie;
	int totalTimeByNextCookie;
	
	int caseNumber = 0;

	long float timeTakenByCurrentCookie = 0;
	long float timeTakenByNextCookie = 0;
	long float timeTakenToGenerateNextCookie = 0;
	long float timetakenToGenerateCurrentCookie =0;


	fstream data;
	fstream write;
	string currentLine;

	int lineFlag = 0;

	data.open("read2.txt");
	write.open("output2.txt");

	cout.precision(10);

	while (getline(data,currentLine))
	{
		data >> cookieFarmCostValue >> cookieIncrementValue >> targetCookieValue;

		
		while (true)
		{
			timeTakenByCurrentCookie = 0 + timetakenToGenerateCurrentCookie + (targetCookieValue / numberOfCookies);

			mkl:

			timeTakenToGenerateNextCookie = (cookieFarmCostValue / numberOfCookies);

			
			timeTakenByNextCookie = 0 + timetakenToGenerateCurrentCookie + timeTakenToGenerateNextCookie + (targetCookieValue / (numberOfCookies + cookieIncrementValue));


			if (timeTakenByCurrentCookie < timeTakenByNextCookie)
			{
				caseNumber = caseNumber + 1;

				write << "Case #" << caseNumber << ": " << setprecision(10) << timeTakenByCurrentCookie << endl;

				goto nextLine;
			}

			else
			{
				numberOfCookies = numberOfCookies + cookieIncrementValue;

				timetakenToGenerateCurrentCookie = timeTakenByNextCookie - (targetCookieValue / numberOfCookies);

				timeTakenByCurrentCookie = timeTakenByNextCookie;
				

				goto mkl;
				
			}
		}
	nextLine:

		timeTakenByCurrentCookie = 0;
		timeTakenByNextCookie = 0;
		timetakenToGenerateCurrentCookie = 0;
		timeTakenToGenerateNextCookie = 0;
		totalTimeByCurrentCookie = 0;
		totalTimeByNextCookie = 0;
		numberOfCookies = 2;

		continue;
	}
	

	

	data.close();
	write.close();

	getchar();
}
