#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>

using namespace std;

unsigned long long calc(unsigned long long r, unsigned long long t);
unsigned long long calcNeeded(unsigned long long r);

int main(int argc, char const *argv[])
{
	streambuf *iBackup = NULL , *oBackup = NULL;
	ofstream output;
	ifstream input;

	// backsup input/output
	iBackup = cin.rdbuf();
	oBackup = cout.rdbuf();
	
	input.open(argv[1]);
	
	if( input.fail()){
		cout << "input failed." << endl;
		return 1;
	}
	cin.rdbuf(input.rdbuf());
	
	output.open(argv[2]);
	if( output.fail()){
		cout << "output failed." << endl;
		return 1;
	}
	cout.rdbuf(output.rdbuf());
	
	//////////////////////////////////////// STAART OF CODE ////////////////////
	int T=0;
	cin >> T;

	for(int i=1;i<=T;i++)
	{
		unsigned long long r,t;
		cin >> r >> t;
		cout << "Case #" << i << ": " << calc(r,t) << endl;
	}
	
	input.close();
	cin.rdbuf(iBackup);
	output.close();
	cout.rdbuf(oBackup);

	return 0;
}

unsigned long long calc(unsigned long long r, unsigned long long t)
{
	unsigned long long c = 0;

	while(t > 0)
	{

		unsigned long long needed = 2*r+1;
		if( needed <= t)
		{
			c++;
			t = t - needed;
			r += 2;
		}
		else
		{
			break;
		}
	}
	return c;
}