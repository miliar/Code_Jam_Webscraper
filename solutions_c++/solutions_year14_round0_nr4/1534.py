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
void ReadDoubleVector(ifstream& ifs, vector<double>& double_vector, int vector_size);
void SplitLineToStrings(const string& s, char delim, vector<string>& elems);
void DeceitfulWar(vector<double>& vector_naomi, vector<double>& vector_ken, vector<double>::iterator naomi_begin, vector<double>::iterator naomi_end, vector<double>::iterator ken_begin, vector<double>::iterator ken_end, int* pt_points);
void War(vector<double>::iterator naomi_begin, vector<double>::iterator naomi_end, vector<double>::iterator ken_begin, vector<double>::iterator ken_end, int* pt_points);

bool descend(double i, double j) {return (i > j);}
// main
void main(int argc, char* argv[])
{
	// declaration part...
	ifstream input_file;	
	ofstream output_file;
	int case_number = 0;	
	int num_block = 0;
	string text_line;
	// open data file
	OpenFileToRead(input_file, "D-large.in");
	OpenFileToWrite(output_file, "D-large.out");
	// number of case
	input_file >> case_number;
	// getline(input_file, text_line);	 // just to make the get line function happy...
	
	// main loop
	for(int i = 0; i < case_number; i++)
	{		
		// solver here...
		input_file >> num_block;
		vector<double> weights_naomi(num_block);
		vector<double> weights_ken(num_block);
		ReadDoubleVector(input_file, weights_naomi, num_block);
		ReadDoubleVector(input_file, weights_ken, num_block);

		sort(weights_naomi.begin(), weights_naomi.end(), descend);
		sort(weights_ken.begin(), weights_ken.end(), descend);

		int deceitful_war_points = 0;
		int war_points = 0;
		vector<double> tmp_naomi(weights_naomi.size());
		vector<double> tmp_ken(weights_ken.size());
		for(int m = 0; m < weights_naomi.size(); m++)
		{
			tmp_naomi[m] = weights_naomi[m];
			tmp_ken[m] = weights_ken[m];
		}
		// main solution
		DeceitfulWar(tmp_naomi, tmp_ken, tmp_naomi.begin(), tmp_naomi.end(), tmp_ken.begin(), tmp_ken.end(), &deceitful_war_points);
		War(weights_naomi.begin(), weights_naomi.end(), weights_ken.begin(), weights_ken.end(), &war_points);

		output_file << "Case #" << i + 1 << ": " << deceitful_war_points << " " << war_points << endl;
	}

	input_file.close();
	output_file.close();	
}

void DeceitfulWar(vector<double>& vector_naomi, vector<double>& vector_ken, vector<double>::iterator naomi_begin, vector<double>::iterator naomi_end, vector<double>::iterator ken_begin, vector<double>::iterator ken_end, int* pt_points)
{
	int flag_return = 1;
	vector<double>::iterator it_naomi = naomi_begin;
	vector<double>::iterator it_ken = ken_begin;
	for(int i = 0; i < vector_naomi.size(); i++)
	{
		if(*it_naomi < *it_ken)
		{
			flag_return = 0;
			break;
		}
		else
		{
			it_naomi++;
			it_ken++;
		}
	}
	if(flag_return)
		*pt_points = vector_naomi.size();
	else
	{
		vector<double>::iterator it_naomi_back = vector_naomi.end();
		vector<double>::iterator it_ken_back = vector_ken.end();		
		it_naomi_back--;
		it_ken_back--;		
		while(*(it_ken_back) < *(it_naomi_back))
		{			
			it_naomi_back--;
			it_ken_back--;
		}
		vector_naomi.erase(it_naomi_back);
		vector_ken.erase(vector_ken.begin());
		if(vector_naomi.size() > 0)
		{
			DeceitfulWar(vector_naomi, vector_ken, vector_naomi.begin(), vector_naomi.end(), vector_ken.begin(), vector_ken.end(), pt_points);
		}

	}
}

void War(vector<double>::iterator naomi_begin, vector<double>::iterator naomi_end, vector<double>::iterator ken_begin, vector<double>::iterator ken_end, int* pt_points)
{
	if(*naomi_begin > *ken_begin)
	{
		(*pt_points)++;		
		naomi_begin++;
		ken_end--;
		if(naomi_begin != naomi_end && ken_begin != ken_end)
			War(naomi_begin, naomi_end, ken_begin, ken_end, pt_points);		

	}
	else
	{
		naomi_begin++;
		ken_begin++;
		if(naomi_begin != naomi_end && ken_begin != ken_end)
			War(naomi_begin, naomi_end, ken_begin, ken_end, pt_points);		
	}
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

void ReadDoubleVector(ifstream& ifs, vector<double>& double_vector, int vector_size)
{
	// clear list
	if(double_vector.size() != vector_size)
	{
		cout << "vector size incorrect... " << endl;
		exit(0);
	}
	// read file... assume ifs is correct...
	for(int i = 0; i < vector_size; i++)
	{
		ifs >> double_vector[i];
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