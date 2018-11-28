// reading a text file
#include <iostream>
// #include <fstream>
// #include <sstream>
// #include <string>
// #include <algorithm>
// #include <vector>
#include <cmath>
// #include <climits>

using namespace std;

int main () {
	// define variables
	int numTC;
	int N;

	// ifstream myfile ("sample-1-2016.in");
	// ofstream savefile ("sample-1-2016.out");
	
	// if(!myfile.is_open())
		// cout << "File not found";

	cin >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		cin >> N;
		
		if(N == 0)
		{
			cout << "Case #" << (t + 1) << ": INSOMNIA" << endl;
			continue;
		}
		
		int* checked = new int[10];
		
		for(int k = 0; k < 10; k++)
			checked[k] = 0;
			
		int count = 0;
		int multiplier = 1;
		int n;
		
		while(count < 10)
		{
			n = N * multiplier;
			
			while(n > 0)
			{
				int r = n % 10;
				n = n / 10;
				
				if(!checked[r])
				{
					count++;
					checked[r] = 1;
				}
			}
			
			multiplier++;
		}
		
		cout << "Case #" << (t + 1) << ": " << N*(multiplier - 1) << endl;
			
		delete [] checked;	
	}

	// myfile.close();
	// savefile.close();

	return 0;
}


