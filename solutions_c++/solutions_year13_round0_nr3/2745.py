#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

typedef set<int> SetInt;

int main(int argc, char** argv) {
	int casen = 0;
	ifstream ifile;
	ofstream ofile;
	//ifile.open("sample.txt");
	ifile.open("C-small-attempt1.in");
	ofile.open("output.txt");
	ifile >> casen;
	for (int c=0; c<casen; c++)
	{
		int y = 0;
		int a, b;
		ifile >> a;
		ifile >> b;
		for (int i=1;i<=100;i++)
		{
			int sqr = i*i;
			if (sqr>b) break;
			if (sqr>=a)
			{
				if (sqr<10)
				{
					cout << sqr << ",";
					y++;
				}
				else
				{
					int npd = 0;
					{
						char buffer[1000];
						char* pt = itoa(i, buffer, 10);
						const string& str = &buffer[0];
						int len = str.size();
						for (int j=0;j<len&&npd==0;j++)
						{
							if (pt[j]!=pt[len-1-j]) npd=1;
						}
					}
				
					char buffer[1000];
					char* pt = itoa(sqr, buffer, 10);
					const string& str = &buffer[0];
					int len = str.size();
					for (int j=0;j<len&&npd==0;j++)
					{
						if (pt[j]!=pt[len-1-j]) npd=1;
					}

					if (npd==0)
					{
						cout << sqr << ",";
						y++;
					}
				}
			}
		}
		cout << endl;
		
		cout << "Case #" << c+1 << ": " << y << endl;
		ofile << "Case #" << c+1 << ": " << y << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}
