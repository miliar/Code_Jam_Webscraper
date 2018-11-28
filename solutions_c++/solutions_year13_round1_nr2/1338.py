#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <stack>

using namespace std;

int calc(int E, int curE, int R, stack<int> v);
int long calcNeeded(int long r);

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
		int E,R,N;
		int tmp;
		cin >> E >> R >> N;
		stack<int> v;
		for(int j=0;j<N;j++)
		{
			cin >> tmp;
			v.push(tmp);
		}
		cout << "Case #" << i << ": " << calc(E,E,R,v) << endl;
	}
	
	input.close();
	cin.rdbuf(iBackup);
	output.close();
	cout.rdbuf(oBackup);

	return 0;
}

int calc(int E, int curE, int R, stack<int> v)
{
	if(v.empty())
	{
		return 0;
	}
	if(curE > E)
	{
		curE = E;
	}

	int value = v.top();
	v.pop();
	int max = -1;
	for(int i=0;i<=curE;i++)
	{
		if(curE - i < 0)
		{
			break;
		}
		int gain = value*i + calc(E,curE-i+R,R,v);
		if( gain > max )
		{
			max = gain;
		}
	}
	return max;
}