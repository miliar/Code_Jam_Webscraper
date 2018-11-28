#include <iostream>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <math.h>
#include <bitset>
#include <string>

using namespace std;

int main() {
	
	string line;

	getline(cin, line); // get n case

	int nCase = 1;

	while(getline(cin, line)) // actual cases
	{
		cout << "Case #" << nCase << ": ";

		int cnt = 0;
		for(int i=line.length()-1;i>=0;i--)
		{
			if (line[i]=='-')
			{
				cnt++;
				for(int o=0;o<=i;o++)
				{
					if(line[o]=='-')
						line.replace(o,1,1,'+');
					else
						line.replace(o,1,1,'-');
				}

				i=line.length();
			}
		}
		cout << cnt;

		cout << endl;
		
		nCase++;
	}

	return 0;
}