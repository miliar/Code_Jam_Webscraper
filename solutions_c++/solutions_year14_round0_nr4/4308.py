// war main
#include "GCODE.h"
ifstream in;
ofstream out;

string solvePuzzle(int numblocks, int probnum)
{
	double *hers = new double[numblocks];
	double *his = new double[numblocks];
	
	double temp;
	for(int i=0; i < numblocks; i++)
	{	in >> temp; hers[i] = temp; }
	for(int i=0; i < numblocks; i++)
	{	in >> temp; his[i] = temp; }

	int small = 0;
	double store;
	double smallest = hers[0];
	
	for(int i=0; i< numblocks; i++)
	{
		smallest = hers[i];
		small = i;
		for(int j=i; j<numblocks; j++)
		{
			if(smallest > hers[j])
			{	
				smallest = hers[j];
				small = j;
			}
		}
		store = hers[i];
		hers[i] = hers[small];
		hers[small] = store;
		
	}// hers is sorted
	
	small = 0;
	smallest = his[0];
	
	for(int i=0; i< numblocks; i++)
	{
		smallest = his[i];
		small = i;
		for(int j=i; j<numblocks; j++)
		{
			if(smallest > his[j])
			{	
				smallest = his[j];
				small = j;
			}
		}
		store = his[i];
		his[i] = his[small];
		his[small] = store;
		
	}// his is sorted
	
	int hertail = 0;
	int histail = 0;
	int hishead = numblocks-1;
	int won = 0;
	int herhead = numblocks-1;
	
	// honest
	for(int i=numblocks-1; i>=0; i--)
	{
		if(hers[i] > his[hishead])// bottom of list she wins
		{
			histail++;
			won++;
		}
		if(hers[i] < his[hishead]) // top of list she looses
		{
			hishead--;
		}
	}
	int honestwins = won;
	
	hertail = 0;
	histail = 0;
	hishead = numblocks-1;
	won = 0;
	herhead = numblocks-1;

	// lie
	for(int i=0; i < numblocks; i++)
	{
		//under
		if(hers[i] < his[histail]) // not win
		{
			hishead--;
		}
		//over
		if(hers[i] > his[histail]) // wins 
		{
			histail++;
			won++;
		}
	}
	int liewins = won;
	out << "Case #" << probnum << ": " ;
	out << liewins << " " << honestwins << "\n";
	
	return "whatever";
}

int main()
{
	int numprob = 0;
	
	in.open("D-large.in", ios_base::in);
	in >> numprob;
	out.open("output.txt",  (ios_base::out | ios_base::app));
	cout << numprob << '\n';

	int numblocks;
	

	for(int i=1; i <=numprob;i++)
	{
		in >> numblocks;
		solvePuzzle(numblocks, i);
	}
	
	
	return 0;
}