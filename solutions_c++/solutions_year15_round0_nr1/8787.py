//small dataset could be counted. Greedy
//Large dataset?


#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int Solver();
int SMAX;
string people;//will be SMAX + 1

int main()
{
	int T,Case=0;
	cin>>T;
	ofstream fout("output.txt");

	while(Case++<T)
	{
		cin>>SMAX>>people;
		fout<<"Case #"<<Case<<": "<<Solver()<<endl;
	}
	return 0;
}


//Greedily Run through, Keep track of running sum and ensure it is equal or greater to the 
// index.
int Solver()
{
	int peopleAdded=0;
	int sum=0;
	for(int i=0;i<people.size();i++)
	{
		while(sum < i)
		{
			peopleAdded++;
			sum++;
		}

		sum += people[i]-'0';
	}

	return peopleAdded;
}