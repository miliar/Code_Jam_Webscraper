// google code jam skeleton by tao zhou @ apr 2014 hkust
// basic file io and string operations...

// io and string
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
// sequence containers
#include <array>
#include <vector>
#include <deque>
#include <queue>
#include <forward_list>
#include <list>
#include <stack>
// associative containers
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
// algorithm
#include<algorithm>
#include<regex>

using namespace std;

// functions...
void OpenFileToRead(ifstream& ifs, string file_name);
void OpenFileToWrite(ofstream& ofs, string file_name);
void ReadIntVector(ifstream& ifs, vector<int>& integer_list, int integer_number);
void SplitLineToStrings(const string& s, char delim, vector<string>& elems);

// main
void main(int argc, char* argv[])
{
	// declaration part...
	ifstream input_file;	
	ofstream output_file;
	int case_number = 0;	
	int first_answer = 0;
	int second_answer = 0;
	string text_line;
	// open data file
	OpenFileToRead(input_file, "A-small-attempt0.in");
	OpenFileToWrite(output_file, "output_small_practice.out");
	// number of case
	input_file >> case_number;
	// getline(input_file, text_line);	 // just to make the get line function happy...
	
	// main loop
	for(int i = 0; i < case_number; i++)
	{	
		vector<vector<int>> first_arrangement(4, vector<int>(4));
		vector<vector<int>> second_arrangement(4, vector<int>(4));

		input_file >> first_answer;
		// first arrangement
		for(int m = 0; m < 4; m++)
		{
			for(int n = 0; n < 4; n++)
			{
				input_file >> first_arrangement[m][n];
			}
		}

		input_file >> second_answer;
		for(int m = 0; m < 4; m++)
		{
			for(int n = 0; n < 4; n++)
			{
				input_file >> second_arrangement[m][n];
			}
		}
		vector<int> answer;
		for(int m = 0; m < 4; m++)
		{
			for(int n = 0; n < 4; n++)
			{
				if(first_arrangement[first_answer - 1][m] == second_arrangement[second_answer - 1][n])
					answer.push_back(first_arrangement[first_answer - 1][m]);
			}
		}

		if(answer.size() == 1)		
			output_file << "Case #" << i + 1 << ": " << answer[0] << endl;
		else if(answer.size() > 1)
			output_file << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		else if(answer.size() == 0)
			output_file << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		// solver here...
		// output_file << "Case #" << i + 1 << ": ";
	}

	input_file.close();
	output_file.close();	
}

void OpenFileToRead(ifstream& ifs, string file_name)
{
	ifs.open(file_name.c_str(), ifstream::in);
	// check
	if(!ifs.is_open())
	{
		cout << "can not open file " << file_name.c_str() << " to read... exit..." << endl;
		exit(0);
	}
}

void OpenFileToWrite(ofstream& ofs, string file_name)
{
	ofs.open(file_name.c_str(), ifstream::out);
	// check
	if(!ofs.is_open())
	{
		cout << "can not open file " << file_name.c_str() << " to write... exit..." << endl;
		exit(0);
	}
}

void ReadIntVector(ifstream& ifs, vector<int>& integer_list, int integer_number)
{
	// clear list
	integer_list.clear();
	// read file... assume ifs is correct...
	for(int i = 0; i < integer_number; i++)
	{
		integer_list.push_back(0);
		ifs >> integer_list[i];
	}
	// just check...
	if(integer_list.size() != integer_number)
	{
		cout << "read integer list error... exit..." << endl;
	}
}

void SplitLineToStrings(const string& s, char delim, vector<string>& elems) 
{
	elems.clear();
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) 
	{
        elems.push_back(item);
    }
    
}


/************* split line of string into char array **************/
// getline(input_file, text_line);	 // just to make the get line function happy...
// vector<char> line_letter_list(text_line.begin(), text_line.end());

/*********** replace certain characters in string... *****************/
// replace(test_case_line.begin(), test_case_line.end(), '(', '[');

/***************** initialize vector with certain size ********/
// vector<string> dictionary(d);
// vector<vector<string> dict(d, vector<string>(0));

/****************** regular expression match ******************/
// regex_match(dictionary[j].c_str(), regex(test_case_line.c_str()))

/********************* template tree class **************/
/* template<class CItem> class CTree
{
public:
   // Tree Item properties
   CItem item;
   
   // Children items
   std::vector<CTree*> children;
};
*/
/********************** recursive tree construction ***********/
/*
void ConstructTree(vector<string>::iterator dir_curr, vector<string>::iterator dir_end, vector<CTree<string>*>& children, int flag, int* pt_count)
{

	int flag_existing = 0;
	for(vector<CTree<string>*>::iterator it = children.begin(); it != children.end(); it++)
	{
		if((*it)->item == *dir_curr) // if equal, go to the next string in the string vector recursively
		{
			dir_curr++;
			if(dir_curr != dir_end)
			{				
				ConstructTree(dir_curr, dir_end, (*it)->children, flag, pt_count);
				flag_existing = 1;
				break;
			}
			else
			{
				flag_existing = 1; // need to mark the string existing flag...
				break;
			}
		}
	}
	if(flag_existing == 0)
	{
		// need to new a memory...
		children.push_back(new CTree<string>());	
		(children.back())->item = *dir_curr;		
		if(flag)
			(*pt_count)++;
		dir_curr++;
		if(dir_curr != dir_end)
		{			
			ConstructTree(dir_curr, dir_end, (children.back())->children, flag, pt_count);
		}		
	}	
}
*/