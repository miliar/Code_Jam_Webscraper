// code.cpp : Defines the entry point for the console application.
//

#pragma warning (disable: 4786)


#include <iostream>
#include <typeinfo>
#include <string>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>

inline double round(double value)
{
	return floor(value + 0.5);
}

using namespace std;

const char out_name[]= "E:\\Desktop\\gcj\\data.out";
//const char out_name[]= "E:\\Desktop\\gcj\\large.out";

const char in_name[]= "E:\\Desktop\\gcj\\data.in";
//const char in_name[]= "E:\\Desktop\\gcj\\large.in";


/* Minimum and maximum macros */

#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

const unsigned int LINES= 1;
const bool WIN= true;

const char SEP= ' ';
//const char SEP= 0;

const double PI= acos(-1);

string operator^(string a, string b)
{
	string res;
	const unsigned int size= a.size();
	for (register unsigned int i = 0; i < size; ++i)
		res += '0' + ((a[i] - '0') ^ (b[i] - '0'));
	return res;
}

inline vector<string> s_convert(vector<const char*>& in)
{
	vector<string> out;
	const unsigned int max= in.size();
	for (register unsigned int i= 0; i < max; ++i) out.push_back(string(in[i]));
	return out;
};

inline vector<unsigned int> u_convert(vector<const char*>& in)
{
	vector<unsigned int> out;
	const unsigned int max= in.size();
	for (register unsigned int i= 0; i < max; ++i) out.push_back(atoi(in[i]));
	return out;
};

inline vector<int> convert(vector<const char*>& in)
{
	vector<int> out;
	const unsigned int max= in.size();
	for (register unsigned int i= 0; i < max; ++i) out.push_back(atoi(in[i]));
	return out;
};


class general_program
{
	ofstream out;
	unsigned int max_case;

protected:

	unsigned int _case;
	vector< vector<const char*> > argv;

public:
	general_program(): out(out_name, ios::out|ios::binary), _case (0), max_case (0) {};
	virtual ~general_program()
	{
		out.close();
	};

	virtual int input(char* buffer) = 0;
	virtual int output(const char* buffer)
	{
		if (_case) out <<"Case #" << _case << ":" << buffer << endl;
		else max_case= atoi(argv[0][0]);
//		cout <<"Case #" << _case << ": " << buffer << endl;
		return ++_case;
	};

	virtual void parse_with_spaces(char* buffer)
	{
		vector <const char*> tmp;
		tmp.push_back(buffer);
		argv.push_back(tmp);
	};
	virtual void parse(char* buffer)
	{
		vector <const char*> tmp;
		char* p= buffer;
		char* arg= buffer;
		while (*p)
		{
			if (*p == SEP)
			{
				*p= 0;
				tmp.push_back(arg);
				arg= p +1;
			}
			++p;
		}
		tmp.push_back(arg);
		argv.push_back(tmp);
	};
};

class program: public general_program
{
	unsigned int line_count;
	unsigned int lines_per_action;

	void Init();

public:

	program(): line_count(0), lines_per_action(LINES) {Init();};
	virtual ~program() {};

	int my_program();
	virtual int input(char* buffer)
	{
		parse(buffer);
//		parse_with_spaces(buffer);
		if (!_case) return output(buffer);

		++line_count;
		if (line_count == lines_per_action)
		{
			line_count= 0;
			my_program();
		}
		return 0;
	};

/*
	virtual int output() {return 0;};
*/
};

int main(int argc, const char* argv[])
{
//	if (argc == 2 && argv[1])
	{
//		ifstream file (argv[1], ios::in|ios::binary|ios::ate);
		ifstream file (in_name, ios::in|ios::binary|ios::ate);
		if (file.is_open())
		{
			streampos size = file.tellg();
			char* memblock = new char[size];

			file.seekg(0, ios::beg);
			file.read(memblock, size);
			file.close();
			
			char* line= memblock;
			char* buffer= line;
			char* last= memblock +size;

			program p;

			while (line < last)
			{
				if (WIN && *line == '\r' && line+1 < last && *(line+1) == '\n')
				{
					*line= 0;
					p.input(buffer);
					buffer= line +2;
					++line;
				}
				else if (*line == '\n')
				{
					*line= 0;
					p.input(buffer);
					buffer= line +1;
				}
				++line;
			}
			delete[] memblock;
		}
		else
		{
			cout << "Unable to open file" << endl;
			return 1;
		}
	}
	return 0;
}

map<char, const char*> seq;

void program::Init()
{
};



int program::my_program()
{
	static bool dynamic= false;
//	static unsigned int vi= 1;
	const unsigned int vi= 1+ (_case -1) * lines_per_action;

	static unsigned int remaining= 0;

/*
	if (!dynamic)
	{
		remaining= atoi(argv[vi][0]);
		++vi;

		lines_per_action = remaining;
		dynamic= true;
		return 0;
	}

	dynamic = false;
	lines_per_action = 1;
*/

	vector <unsigned int> input= u_convert(argv[vi]);

	unsigned int A= input[0];
	unsigned int B= input[1];
	unsigned int K= input[2];
	
	unsigned int count= 0;

	for (register unsigned int i= 0; i<A; ++i)
		for (register unsigned int j= 0; j<B; ++j)
		{
			if ((i&j) <K) ++count;
		}

	string out= " ";

	{
		char o[80]= {0};
		sprintf(o, "%u", count);
		out += o;
	}

//	vi += remaining;
	return output(out.c_str());
}
