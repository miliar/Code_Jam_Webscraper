#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std; 


void read_file( map<int,int> &M, ifstream &file);



int main(int argc, char **argv)
{
	ifstream file("A-small-attempt2.in", ifstream::in);
	ofstream out("output.in", ofstream::out);

	int T; 

	file >> T; 


	for(int i=0; i<T; i++)
	{
		
		map<int,int> M;
		vector<int> results; 

		for(int j=0; j<16; j++)
		{
			M[j]=0;
		}

		read_file( M, file);
		read_file( M, file);

		for(map<int,int>::iterator it = M.begin(); it!=M.end(); it++)
		{
			if(it->second == 2)
			{
				results.push_back(it->first);
			}
		}


		if(results.empty())
		{
			out << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		}
		else 
		{
			if(results.size() == 1)
			{
				out << "Case #" << i+1 << ": " << results[0] << endl;
			}
			else
			{
				out << "Case #" << i+1 << ": Bad magician!" << endl;
			}
		}


	}






	return 0; 
}





void read_file( map<int,int> &M, ifstream &file)
{
	int row; 
	file >> row; 

	
		switch(row)
		{
		case 1:
		 for(int k=0; k<4; k++)
		 {
			 int temp;
			 file >> temp; 
			 M[temp]++;
		 }	 
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 break; 

		case 2:
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );

		 for(int k=0; k<4; k++)
		 {
			 int temp;
			 file >> temp; 
			 M[temp]++;
		 }
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );

		 break;

		case 3:
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 for(int k=0; k<4; k++)
		 {
			 int temp;
			 file >> temp; 
			 M[temp]++;
		 }
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 break;

		case 4:
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
		 file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );

		for(int k=0; k<4; k++)
		 {
			 int temp;
			 file >> temp; 
			 M[temp]++;
		 }
		 
		 break;
		}


}

