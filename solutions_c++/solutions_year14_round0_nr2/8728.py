#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main () {
	
	
	ifstream fin ("B-large.in");
	
	//Validate file first
	if (!fin){
		return 1; //exit from main
	} 
	

	ofstream fout ("B-large.out");
	
	//Validate file first

	if (!fout)  
	{
		return 1; //exit from main
	}

	int num_var;
	
	fin >> num_var;

	if (num_var < 1 || num_var > 100){
		return 1; //exit 
	}
	

	int i = 0;

	while (i < num_var) {
		

		long double C,  
					F, 
					X,
					R = 2;

		fin >> C; 
		if (C < 1 || C > 10000){
			return 1;
		}

		fin >> F;
		if (F < 1 || F > 100){
			return 1;
		}

		fin >> X;
		if (X < 1 || X > 100000){
			return 1;
		}

		long double _timeElapsed = C / R; //calculating the time
		
		long double _cTemp = C; 
			

		//starting the operations
		while (_cTemp != X) {

            if ((X / (R + F)) < ((X - C) / R)) {		
				R = R + F;
				_timeElapsed = _timeElapsed + C / R;
				_cTemp = C;
            }
            else {
			
				_timeElapsed = _timeElapsed + (X - C) / R;
                _cTemp = X;

            }
        }

		fout << "Case #" << i + 1 << ": " << setprecision (7) << showpoint << fixed << _timeElapsed << endl;
		i++;
	}
	//Now closing the files
	fout.close ();
	//now closing infile
	fin.close (); 
	//exit finally
	return 0;
}