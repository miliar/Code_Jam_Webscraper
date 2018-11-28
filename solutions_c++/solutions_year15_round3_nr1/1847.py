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

inline vector<__int64> i64_convert(vector<const char*>& in)
{
	vector<__int64> out;
	const unsigned int max= in.size();
	for (register unsigned int i= 0; i < max; ++i) out.push_back(_atoi64(in[i]));
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


inline unsigned int gcd(unsigned int a, unsigned int b)
{
    if(a %b == 0)
    {
        return b;
    }
    return gcd(a, a %b);
}

inline unsigned int gcd(vector<unsigned int>& num)
{
	unsigned int gcd_c= 0;
	for (register unsigned int i= 0; gcd_c != 1 && i < num.size() -1; ++i)
	{
		gcd_c= gcd_c? gcd(num[i +1], gcd_c): gcd(num[i +1], num[i]);
	}
	return gcd_c;
};

inline unsigned int lcm(unsigned int a, unsigned int b)
{
	return a * b / gcd (a, b);
};

inline unsigned int lcm(vector<unsigned int>& num)
{
/*	unsigned int gcd_c= gcd(num);
	unsigned int lcm= gcd_c;
	for (register unsigned int i= 0; i < num.size(); ++i)
	{
		lcm *= num[i] /gcd_c;
	}
	return lcm;
*/

	unsigned int lcm_c= 0;
	for (register unsigned int i= 0; i < num.size() -1; ++i)
	{
		lcm_c= lcm_c? lcm(num[i +1], lcm_c): lcm(num[i +1], num[i]);
	}
	return lcm_c;
}


int program::my_program()
{
	const unsigned int vi= 1+ (_case -1) * lines_per_action;

/*	static unsigned int remaining= 0;
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

	register unsigned int i= 0;

	unsigned int count= 0;

	unsigned int R= atoi(argv[vi][0]);
	unsigned int C= atoi(argv[vi][1]);
	unsigned int W= atoi(argv[vi][2]);

	unsigned int sunk= 0;

	for (i= 0; i< R -1; ++i)
	{
		count += (C -1) / W +1;
	}
	for (; i< R; ++i)
	{
		count += (C -1) / W;
	}

	count += W;
	string out= " ";

	char temp[256]= {0};

	sprintf(temp, "%u", count);

	out += temp;


//	vi += remaining;


	return output(out.c_str());
}

























