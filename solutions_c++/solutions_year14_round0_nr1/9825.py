#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>

using namespace std;

main() 
{
	bool first = 0;
	int line_num=0;
	const int N = 4;
	int total_cases, case_num=1, num;
	vector <int> row1, row2;
	int cards[N][N];
	string str;
	int r1, r2, r;
	bool second_row = 0;

	ifstream rfile("input");
	if (rfile.is_open()) {
	    while (getline(rfile, str)) {
			 line_num++;  // increase line number
			 stringstream ss(str);

		      if (!first) {
		        total_cases = atoi(str.c_str());
			   first = 1;
			 } else {
			   if (line_num == (case_num - 1)*10 + 2) {
                      ss >> r1; // read in the r1 th row
				  r = 0;
				  second_row = 0;
			   } else if (line_num == (case_num - 1)*10 + 7) {
                      ss >> r2; // read in the r1 th row
				  r = 0;
				  second_row = 1;
			   } else {
				  // read in row of matrix  
				  r++;
				  if (r == r1 && second_row == 0) {
					 // read first row
			           for (int j = 0; j < N; j++) {
				           ss >> num;
						 row1.push_back(num);
			           }
				  } else if (r == r2 && second_row == 1) {
			           for (int j = 0; j < N; j++) {
				           ss >> num;
						 row2.push_back(num);
			           }
				  }

				  if (second_row && r == N) {
					 second_row = 0;
					 sort(row1.begin(), row1.end());
					 sort(row2.begin(), row2.end());

					 vector <int> row;
					 set_intersection(row1.begin(), row1.end(),
							        row2.begin(), row2.end(),
								   back_inserter(row));

					 if (row.size() == 1) {
						cout << "Case #" << case_num << ": " << row[0] << endl;
					 } else if (row.size() > 1) {
						cout << "Case #" << case_num << ": Bad magician!" << endl;
					 } else {
						cout << "Case #" << case_num << ": Volunteer cheated!" << endl;
					 } 

					 //ostream_iterator< int > output( cout, " " );
					 //std::copy(row.begin(), row.end(), output);
					 row1.clear();
					 row2.clear();
					 row.clear();
					 case_num++; // go to the next case
				  } 
			   } // inner else
			 } // else 
	    } // while 
	    rfile.close();
	}
}
