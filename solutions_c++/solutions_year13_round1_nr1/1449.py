#include <iostream>
#include <cmath>
#include <list>

using namespace std;

void runTest()
{
	long long r;
	long long t;
	cin >> r >> t;
	
	long long count = 0;
	while(t >= 0)
	{
		//cout << r << "  " << t << endl;
		t -= 2 * r + 1;
		count++;
		r += 2;
	}
	cout << count - 1 << endl;
}


int main(int argc, const char * argv[])
{
	(void) argc;
	(void) argv;
	int numTests;
	cin >> numTests;
	
	for(int i =0;i < numTests;i++)
	{
		cout << "Case #" << i + 1 << ": ";
		runTest();
	}
}
