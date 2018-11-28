#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;

int main() 
{
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int times = 0;
		
		int N, N_orig;
		cin >> N;
		N_orig = N;
		
		if (N == 0)
		{
			cout << "CASE #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		
		int found[10];
		for (int j = 0; j < 10; j++) found[j] = 0;
		
		int bool_found = 0;

		while (!bool_found)
		{
			ostringstream convert;
			string number_string;
			convert << N;
			number_string = convert.str();
			
			for (int j = 0; j < number_string.size(); j++)
			{
				found[number_string[j] - '0'] = 1;		
			}
			
			bool_found = 1;
			for (int j = 0; j < 10; j++) {
				if (!found[j]) bool_found = 0;
			}
			if (!bool_found){
				N = N + N_orig;			
			}
			
			
			// check if we've found all the chars.
			
		}
		
		cout << "Case #" << i+1 << ": " << N << endl;
		
	}
}