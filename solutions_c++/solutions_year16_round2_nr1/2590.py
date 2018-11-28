#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	ifstream myfile;
	//myfile.open("testA.in");
	myfile.open("A-large.in");
	char num[][6] = {"ZERO", "FOUR", "TWO", "THREE", "FIVE", "SIX", "SEVEN", "EIGTH", "NINE","ONE"};
	int numero[] = {0, 4, 2, 3, 5, 6, 7, 8, 9, 1};
	
	int T;
	myfile >> T;
	string line;
	getline(myfile, line);
	for (int t=0; t<T; t++)
	{
		
		

		getline(myfile, line);
		string mynum;
		//cout << line; getchar();
		
		while (line.size()>1)
		{
			
			for (int n = 0; n<10; n++)
			{
				string line2=line;
				int j = 0;
				for (j=0; j<strlen(num[n]);j++)
				{
					int res = line2.find(num[n][j]);
					if (res!=-1)
						line2.erase(res,1);
					else break;
				}
				if (j == strlen(num[n]))
				{
					char mychar = numero[n]+'0';
					mynum.append(&mychar,1);
					//cout << mynum;
					line = line2;
					//cout << << line; getchar()
					break;
				}
			}
		}
		sort(mynum.begin(), mynum.end());
		cout << "Case #" << t+1 << ": " << mynum << std::endl;
		
		
	}
}
