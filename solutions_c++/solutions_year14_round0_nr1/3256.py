// Google Code Jam 2014
// Qualification Round problem 1: Magic Trick
// --
// Compile with -std=c++11 flag, if any C++11 features are used.

#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	int num_problems, sel_a, sel_b;
	int *grid_a, *grid_b;
	int *row_a, *row_b;
	ifstream file_in;
	ofstream file_out;

	// Check args
	if(argc < 2)
	{
		cout << "Argument required: Name of input file." << endl;
		return 1;
	}

	// Open file
	file_in.open(argv[1], ios::in);

	if(!file_in.is_open())
	{
		cerr << "Error opening input file: " << argv[1] << endl;
		return 1;
	}

	// File is open, start reading problem set
	file_in >> num_problems;
	cout << "Number of problems: " << num_problems << endl;

	// Open output file
	file_out.open("output.txt", ios::out);
	if(!file_out.is_open())
	{
		cerr << "Error opening output file 'output.txt'" << endl;
		return 1;
	}

	for(int problem = 0; problem < num_problems; problem++)
	{
		file_in >> sel_a;
		cout << endl << "Volunteer chose " << sel_a << " from first setup..." << endl;
		
		grid_a = new int[16];
		grid_b = new int[16];
		row_a = new int[4];
		row_b = new int[4];

		for(int i = 0; i < 4; i++)
		{
			file_in >> grid_a[i*4] >> grid_a[i*4+1] >> grid_a[i*4+2] >> grid_a[i*4+3];
		}

		// Read second selection

		file_in >> sel_b;
		cout << endl << "Volunteer chose " << sel_b << " from second setup..." << endl;

		// Read second grid
		for(int i = 0; i < 4; i++)
		{
			file_in >> grid_b[i*4] >> grid_b[i*4+1] >> grid_b[i*4+2] >> grid_b[i*4+3];
		}

		cout << "Board is initially set up like so:" << endl;
		for(int i = 0; i < 4; i++)
		{
			cout << grid_a[i*4+0] << " " << grid_a[i*4+1] << " " << grid_a[i*4+2] << " " << grid_a[i*4+3] << " " << endl;
		}
		cout << "Board in second state:" << endl;
		for(int i = 0; i < 4; i++)
		{
			cout << grid_b[i*4+0] << " " << grid_b[i*4+1] << " " << grid_b[i*4+2] << " " << grid_b[i*4+3] << " " << endl;
		}

		// Grab the row that the volunteer chose so we can compare it later
		// Quick sanity check:
		if(sel_a > 4 || sel_a < 1) 
		{
			cerr << "Row A out of bounds!" << endl;
			return 1;
		}
			if(sel_b > 4 || sel_b < 1) 
		{
			cerr << "Row B out of bounds!" << endl;
			return 1;
		}

		int s1 = (sel_a-1)*4;
		int s2 = (sel_b-1)*4;
		int j = 0;
		for(int i = s1; i < s1+4; i++, j++)
			row_a[j] = grid_a[i];
		
		j = 0;
		for(int i = s2; i < s2+4; i++, j++)
			row_b[j] = grid_b[i];

		cout << "Row that the volunteer selected the first time: " << row_a[0] << "," << row_a[1] << "," << row_a[2] << "," << row_a[3] << endl;
		cout << "Row that the volunteer selected the second time: " << row_b[0] << "," << row_b[1] << "," << row_b[2] << "," << row_b[3] << endl;

		// OK, what we're doing here is searching for the intersection of the 'set' we're dealing with. In this case, the two rows
		// that the volunteer chooses.
		// If there is no intersection, the volunteer is lying. If there is more than one intersection, the magician is not rearranging
		// the cards properly.

		int num_intersects = 0;
		int last_intersect = -1;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(row_a[i] == row_b[j])
				{
					num_intersects++;
					last_intersect = row_a[i];
				}
			}
		}

		if(num_intersects == 0) 
			cout << "Volunteer cheated!" << endl;
		else if(num_intersects > 1)
			cout << "Bad magician!" << endl;
		else 
			cout << "Card: " << last_intersect << endl;

		// --
		// Final output to file
		file_out << "Case #" << problem+1 << ": ";

		if(num_intersects == 0) 
			file_out << "Volunteer cheated!" << endl;
		else if(num_intersects > 1)
			file_out << "Bad magician!" << endl;
		else 
			file_out << last_intersect << endl;


		delete [] grid_a;
		delete [] grid_b;
		delete [] row_a;
		delete [] row_b;
	}

	file_in.close();
	file_out.close();
	return 0;
}
