#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <climits>
#include <bitset>
#include <algorithm>
#include <cassert>

using namespace std;

// typedef
typedef __int64 int64;
typedef unsigned __int64 uint64;
typedef unsigned int uint;

// define
#ifdef _DEBUG
#	define CHECK_DATA 1
#else
#	define CHECK_DATA 0
#endif

#ifdef    WIN32
#	define DIRECTORY_SEPARATOR '\\'
#else
#	define DIRECTORY_SEPARATOR '/'
#endif

#define DEFAULT_INPUT "test.txt"
#define DEFAULT_OUTPUT "result.txt"
#define DEFAULT_ANSWER "answer.txt"

//=========================================================================//
//     Problem Class
//=========================================================================//
class Problem{
private:
	const int _problem_index_;
	// input
	int R,C,M;
	// tmp
	// result
	bool success;
	vector<string> result;
public:
	//--------------------------------------------------------------------//
	//     Constructor
	//--------------------------------------------------------------------//
	Problem(const uint index): _problem_index_(index){}

	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> R >> C >> M;
	}
	//--------------------------------------------------------------------//
	//     Output for Debug
	//--------------------------------------------------------------------//
	void DebugOutput(ostream& out) const{

	}
	//--------------------------------------------------------------------//
	//     Solve
	//--------------------------------------------------------------------//
	void Solve(){
		success = false;
		result.resize(R);
		for(int i=0, size=result.size(); i<size; ++i)
		{
			for(int j=0; j<C; ++j){
				result[i] += '*';
			}
		}
		int m = R * C - M;
		if(R == 1){
			for(int i=0; i<m; ++i)
			{
				result[0][i] = '.';
			}
			result[0][0] = 'c';
			success = true;
		}
		else if(C == 1){
			for(int i=0; i<m; ++i)
			{
				result[i][0] = '.';
			}
			result[0][0] = 'c';
			success = true;
		}
		else if(m == 1){
			result[0][0] = 'c';
			success = true;
		}
		else if(m == 2){
		}
		else if(m % 2 == 0){
			if(m < 2 * C){
				for(int i=0; i<m/2; ++i){
					result[0][i] = '.';
					result[1][i] = '.';
				}
			}
			else{
				for(int i=0; i<C; ++i){
					result[0][i] = '.';
					result[1][i] = '.';
				}
				for(int i=2*C; i<m; ++i){
					int r = i / C,
						c = i % C;
					result[r][c] = '.';
				}
				if(m % C == 1){
					int r = m / C;
					result[r-1][C-1] = '*';
					result[r][1] = '.';
				}
			}
			result[0][0] = 'c';
			success = true;
		}
		else if(R >= 3 && C >= 3 && m == 9){
			for(int i=0; i<3; ++i){
				for(int j=0; j<3; ++j){
					result[i][j] = '.';
				}
			}
			result[0][0] = 'c';
			success = true;
		}
		else if(R >= 3 && C >= 3 && m > 9){
			for(int i=0; i<m; ++i){
				int r = i / C,
					c = i % C;
				result[r][c] = '.';
			}
			if(m % C == 1){
				if(m / C == 2){
					int r = m / C;
					result[r-1][C-1] = '*';
					result[r-2][C-1] = '*';
					result[r][1] = '.';
					result[r][2] = '.';
				}
				else{
					int r = m / C;
					result[r-1][C-1] = '*';
					result[r][1] = '.';
				}
			}
			result[0][0] = 'c';
			success = true;
			// x: 2,3,5,7
			// o: 1,4(2x2),6(2x3),8(2x4),9(3x3),10(2x5),11(3x3+2),12(3x4),13(3x3+4)
		}
	}

	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << endl;
		if(success)
		{
			int count = 0;
			for(int i=0; i<R; ++i){
				for(int j=0; j<C; ++j){
					if(result[i][j] == '*'){
						++count;
					}
				}
			}
			assert(count == M);

			for(int i=0, size=result.size(); i<size; ++i)
			{
				out << result[i] << endl;
			}
		}
		else
		{
			out << "Impossible" << endl;
		}
	}
};

//=========================================================================//
//     Open Files
//=========================================================================//
int OpenFiles(const int argc, const char *argv[], ifstream *in_file, fstream *out_file){
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;

	in_file->open(input_file_name.c_str());
	if(!in_file->is_open()){
		cout << "Input File Open Error: [" << input_file_name << "]" << endl;
		return -1;
	}

	out_file->open(output_file_name.c_str(), ios::in | ios::out | ios::trunc);
	if(!out_file->is_open()){
		cout << "Output File Open Error: [" << output_file_name << "]" << endl;
		return -1;
	}

	return 0;
}

int OpenFiles(const int argc, const char *argv[], ifstream *result_file, ifstream *answer_file){
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;
	string answer_file_name = (argc > 1)? argv[2]: DEFAULT_ANSWER;

	result_file->open(output_file_name.c_str());
	if(!result_file->is_open()){
		cout << "Result File Open Error: [" << input_file_name << "]" << endl;
		return -1;
	}

	answer_file->open(answer_file_name.c_str());
	if(!answer_file->is_open()){
		//cout << "Result File Open Error: [" << input_file_name << "]" << endl;
		//return -1;
	}

	return 0;
}

//=========================================================================//
//     Compare Result
//=========================================================================//
void CompareResult(ifstream *result, ifstream *answer){
	if(!answer->is_open()){
		return;
	}

	string line1, line2;
	uint count = 0;
	bool ok = true;
	while(!result->eof() || !answer->eof()){
		++count;

		if(result->eof() && !answer->eof()){
			cout << "Answerには" << count << "行目がありません。" << endl;
			ok = false;
			break;
		}
		else if(!result->eof() && answer->eof()){
			cout << "Resultには" << count << "行目がありません。" << endl;
			ok = false;
			break;
		}

		getline(*result, line1);
		getline(*answer, line2);

		if(line1 != line2){
			cout << count << "行目が異なります。" << endl
				<< "	" << line1 << endl
				<< "	" << line2 << endl;
			ok = false;
		}
	}

	if(ok){
		cout << "Correct" << endl;
	}
	else{
		cout << "InCorrect" << endl;
	}
}

//=========================================================================//
//     Get All Stream Content
//=========================================================================//
template<typename Stream>
void GetAll(string *buf, Stream *stream){
	char c;
	while(!stream->eof()){
		*stream >> c;
		*buf += c;
	}
}

//=========================================================================//
//     Main
//=========================================================================//
int main(const int argc, const char *argv[]){
	// Get File Name
	ifstream in_file;
	fstream out_file;
	if(OpenFiles(argc, argv, &in_file, &out_file) != 0){
		return -1;
	}

	// Get Start Time
	clock_t start, end;
	start = clock();

	// Get number of problems
	uint number_of_problems;
	in_file >> number_of_problems;
	getline(in_file, string());
	
	cout << "=====[Result]===============" << endl;
	for(uint i=0; i<number_of_problems; ++i){
		Problem problem(i+1);
		// Get Input
		problem.GetInput(in_file);
		// Solve
		problem.Solve();
		// Output
		out_file << "Case #" << (i+1) << ":";
		cout << "Case #" << (i+1) << ":";
		problem.OutputResult(cout);
		problem.OutputResult(out_file);
#if CHECK_DATA
		problem.DebugOutput(cout);
#endif
	}

	// Get End Time
	end = clock();

	// File Close
	in_file.close();
	out_file.close();

	// Result Open
	ifstream result_file, answer_file;
	OpenFiles(argc, argv, &result_file, &answer_file);

	cout << endl;
	cout << "=====[Info]=================" << endl;
	cout << "time: "
	     << setprecision(2) << setiosflags(ios::fixed)
	     << (end - start) << "sec" << endl;
	CompareResult(&result_file, &answer_file);
	cout << endl;

	

	return 0;
}