#include<iostream>
#include<cmath>
#include<fstream>

using namespace std;

void sortHigh(int size, double*a);
void sortLow(int size, double*a);

int writeSummary(int numB, double* naom, double* ken);
int writeSummary2(int numB, double* naom, double* ken);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	cout.precision(2);
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		int numB;
		myfileIn >> numB;
		double *naom = new double[numB];
		for(int j = 0; j < numB; j++)
		{
			myfileIn >> naom[j];
		}
		double *ken = new double[numB];
		for(int j = 0; j < numB; j++)
		{
			myfileIn >> ken[j];
		}
		cout << "Case #" << (i+1) << ":  " << writeSummary(numB, naom, ken) << " " <<
			writeSummary2(numB, naom, ken) << endl;
		myfileOut << "Case #" << (i+1) << ": " << writeSummary(numB, naom, ken) << " " <<
			writeSummary2(numB, naom, ken) << endl;
		delete[]naom;
		delete[]ken;
	}
	return 0;
}


int writeSummary(int numB, double* naom, double* ken)
{
	int points = 0;
	while(numB > 0)
	{
		sortLow(numB, naom);
		sortLow(numB, ken);
		while(numB > 0 && naom[numB-1] > ken[numB-1])
		{
			numB--;
			points++;
		}
		sortHigh(numB, naom);
		sortLow(numB, ken);
		if(numB > 0 && naom[numB-1] < ken[numB-1])
		{
			numB--;
		}
	}
	return points;
}

int writeSummary2(int numB, double* naom, double* ken)
{
	int points = 0;
	
	while(numB > 0)
	{
		sortLow(numB, naom);
		sortLow(numB, ken);
		if(naom[numB-1] > ken[numB-1])
		{
			sortHigh(numB, ken);
			numB--;
			points++;
		}
		else
		{
			numB--;
		}
	}
	return points;
}
void sortHigh(int array_size, double*x)
{
	for (int passes = 0;  passes < array_size - 1;  passes++)
 {
  for (int j = 0;  j < array_size - passes - 1;  j++)
  {
   if (x[j] < x[j+1])
   {
    double hold = x[j];
    x[j] = x[j+1];
    x[j+1]=hold;

   }
  }
 }
}

void sortLow(int array_size, double*x)
{
	for (int passes = 0;  passes < array_size - 1;  passes++)
 {
  for (int j = 0;  j < array_size - passes - 1;  j++)
  {
   if (x[j] > x[j+1])
   {
    double hold = x[j];
    x[j] = x[j+1];
    x[j+1]=hold;

   }
  }
 }
}