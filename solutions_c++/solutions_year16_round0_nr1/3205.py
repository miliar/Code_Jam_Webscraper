#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <stack>

using namespace std;

// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile);



int main()
{

	// open input & output data files
	ifstream infile;
	ofstream outfile;
	openFiles(infile, outfile);

	cout << "Reading the input file..." << endl;


	string line;

	int num;
	infile >> num;
	getline(infile, line);
	int input = 0;
	for (int x = 1; x <= num; x++) {
		bool arr[10] = { false,false,false,false,false,false,false,false,false,false};
		bool completed = false;
		bool negative = false;
		int w = 0;
		outfile << "Case #" << x << ": ";
		infile >> input;
		if (input == 0) {
			outfile << "INSOMNIA" << endl;
		}
		else if (input < 0) {
			negative = true;
			input = -1 * input;
		}
		else for (w = 1; !completed; w++) {
			size_t left = input*w;
			completed = true;
			while (left != 0) {
				size_t right = left % 10;
				arr[right] = true;
				left = left / 10;
			}
			for (int y = 0; completed && y < 10; y++) {
				if (!arr[y])
				{
					completed = false;
				}
			}
		}
		if (negative)
		{
			input = input*-1;
		}
		if (completed) {
			outfile << (w-1)*input << endl;
		}
	}









	// close the files
	infile.close();
	outfile.close();

	cout << "Done." << endl;
	
}


// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile)
{

	// open input data file
	string inFileName;
	cout << "Enter the name of the input file: ";
	cin >> inFileName;
	infile.open(inFileName.c_str());
	if (infile.fail()) {
		cout << "Error opening input data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

	// open output data file
	string outFileName;
	cout << "Enter the name of the output file: ";
	cin >> outFileName;
	outfile.open(outFileName.c_str());
	if (outfile.fail()) {
		cout << "Error opening output data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

}

