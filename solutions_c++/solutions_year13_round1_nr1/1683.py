#include<iostream>
#include<fstream>
#include<math.h>
#include<vector>

#define PI 3.14159265359


using namespace std;

unsigned long long int Bullseye(unsigned long long int r, unsigned long long int t)
{
	unsigned long long int counter = 0;

	while(1)
	{
		unsigned long long int temp = ((r+1)*(r+1) - r*r);
		if( t >= temp)
		{
			counter++;
			t -= temp;
			r += 2;
		}
		else
			break;
	}

	return counter;
}



int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	unsigned long long int T;
	inpFile>>T;
	unsigned long long int r, t;

	for(unsigned long long int i=0; i<T; i++)
	{
		inpFile>>r>>t;



		outFile<<"Case #"<<i+1<<": "<<Bullseye(r,t)<<endl;
	}
	

	

}