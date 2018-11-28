//Created by krever
//Google Codejam 2014

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

	ifstream practice;
	ofstream output;


int main()
{
	practice.open("B-large.in");
	output.open("output.txt");

	int cases;				//T
	int casecount(1);
	double Fcookierate;		//F
	double cookierate(2);
	double wincount;		//X
	double farm;			//C
	double timenow;
	double timeafter;
	int n(1);
	int counter(1);

	practice >> cases;
	while((!practice.eof()) && (casecount <= cases))
	{
		practice >> farm;
		practice >> Fcookierate;
		practice >> wincount;
		timenow= wincount/cookierate;
		timeafter= wincount/(cookierate+Fcookierate) + farm/cookierate;

		while( timenow > timeafter)
		{
			timenow = timeafter;
			timeafter = wincount/(cookierate+ (counter+1)*Fcookierate);
			
			while(counter>=0)
			{
				timeafter= timeafter + farm/(cookierate+ (counter*Fcookierate));
				counter--;
			}
			n++;
			counter=n;
				
		}
		

		output << "Case #" << casecount << ": ";
		output << setprecision(7) << timenow << endl;
		casecount++;
		timenow=0;
		timeafter=0;
		n=1;
		counter=1;
	}


	return 0;
}