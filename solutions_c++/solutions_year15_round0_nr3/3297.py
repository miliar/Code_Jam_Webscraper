#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#define INPUT_FILE_NAME "D:/C-small-attempt0.in"
#define OUTPUT_FILE_NAME "D:/fout.out"

enum QuatVal
{
	i,
	j,
	k,
	one,
	_i,
	_j,
	_k,
	_one
};

class Quat
{
public:
	QuatVal val1;
	QuatVal val2;
	QuatVal result;

	static QuatVal mul(QuatVal v1 , QuatVal v2)
	{
		int numOfneg = 0;
		if (v1 == _i)
		{
			v1 = i;
			numOfneg++;
		}
		else if (v1 == _j)
		{
			v1 = j;
			numOfneg++;
		}
		else if (v1 == _k)
		{
			v1 = k;
			numOfneg++;
		}
		else if (v1 == _one)
		{
			v1 = one;
			numOfneg++;
		}
				
		//
		if (v2 == _i)
		{
			v2 = i;
			numOfneg++;
		}
		else if (v2 == _j)
		{
			v2 = j;
			numOfneg++;
		}
		else if (v2 == _k)
		{
			v2 = k;
			numOfneg++;
		}
		else if (v2 == _one)
		{
			v2 = one;
			numOfneg++;
		}

		QuatVal r;
		if (v1 == QuatVal::one&& v2 == QuatVal::one )
		{
			r = QuatVal::one;
		}
		else if (v1 ==QuatVal::one && v2 == QuatVal::i)
		{
			r = QuatVal::i;
		}
		else if (v1 == QuatVal::one && v2 == QuatVal::j)
		{
			r = QuatVal::j;
		}
		else if (v1 == QuatVal::one && v2 == QuatVal::k)
		{
			r = QuatVal::k;
		}
		else if (v1 == QuatVal::i && v2 == QuatVal::one)
		{
			r = QuatVal::i;
		}
		else if (v1 == QuatVal::i && v2 == QuatVal::i)
		{
			r = QuatVal::_one;
		}
		else if (v1 == QuatVal::i && v2 == QuatVal::j)
		{
			r = QuatVal::k;
		}
		else if (v1 == QuatVal::i && v2 == QuatVal::k)
		{
			r = QuatVal::_j;
		}
		else if (v1 == QuatVal::j && v2 == QuatVal::one)
		{
			r = QuatVal::j;
		}
		else if (v1 == QuatVal::j && v2 == QuatVal::i )
		{
			r = QuatVal::_k;
		}
		else if (v1 == QuatVal::j && v2 == QuatVal::j )
		{
			r = QuatVal::_one;
		}
		else if (v1 == QuatVal::j && v2 == QuatVal::k)
		{
			r = QuatVal::i;
		}
		else if (v1 == QuatVal::k && v2 == QuatVal::one)
		{
			r = QuatVal::k;
		}
		else if (v1 == QuatVal::k && v2 == QuatVal::i)
		{
			r = QuatVal::j;
		}
		else if (v1 == QuatVal::k && v2 == QuatVal::j )
		{
			r = QuatVal::_i;
		}
		else if (v1 == QuatVal::k && v2 == QuatVal::k )
		{
			r = QuatVal::_one;
		}

		if (numOfneg == 2 || numOfneg == 0)
		{
			return r;
		}
		else 
		{
			if (r == i)
			{
				return _i;
			}
			else if(r == j)
			{
				return _j;
			}
			else if(r == k)
			{
				return _k;

			}
			else if(r == one)
			{
				return _one;
			}
			else if(r == _i)
			{
				return i;
			}
			else if(r == _j)
			{
				return j;

			}
			else if(r == _one)
			{
				return one;
			}
			else if(r == _k)
			{
				return k;
			}
		}
	}
};


int nj = 0;
int nk = 0;
int ni = 0;

using namespace std;

void parse_input(int x, string values,vector<QuatVal>& output)
{
	output.clear();
	QuatVal value;
	nk = 0;
	ni = 0;
	nj = 0;
	for (int j=0 ; j<x ;j++)
	{		

		for (int i=0 ; i<values.size(); i++)
		{
			if (values[i] == 'i')
			{
				value = QuatVal::i;
			}
			else if (values[i] == 'j')
			{
				value = QuatVal::j;
			}
			else if (values[i] == 'k')
			{
				value = QuatVal::k;
			}

			output.push_back(value);
			if (values[i] == 'i')
			{
				ni++;
			}
			else if (values[i] == 'j')
			{
				nj++;
			}
			else if (values[i] == 'k')
			{
				nk++;
			}
		}
	}
}

bool get_answer(vector<QuatVal>values)
{
	int index = 0;
	int valuessize = values.size();
	QuatVal temp = QuatVal::one;
	QuatVal val;
	int i_end = 0;
	int j_end = 0;
	int k_end = 0;
	while (index < valuessize)
	{
		val = values[index++];
		temp = Quat::mul(temp,val);
		if (temp == QuatVal::i)
		{
			i_end = index-1;
			break;
		}
	}
	if (index == valuessize)
	{
		return false;
	}
	else
	{
		temp = QuatVal::one;
		while (index < valuessize)
		{
			val = values[index++];
			temp = Quat::mul(temp,val);
			if (temp == QuatVal::j)
			{
				j_end = index-1;
				break;
			}
		}
		if (index == valuessize)
		{
			return false;
		}
		else
		{
			temp = QuatVal::one;
			while (index < valuessize)
			{
				val = values[index++];
				temp = Quat::mul(temp,val);
			}
			if (temp == QuatVal::k && index == valuessize)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
	}
}

int main()
{
	// the fstream
	fstream fileInput(INPUT_FILE_NAME,fstream::in);
	fstream fileOutput(OUTPUT_FILE_NAME,fstream::out);

	int t = 0;
	fileInput>>t;
	string temp;
	getline(fileInput,temp);

	long int l,x;
	for (int i=0 ; i<t ; i++)
	{
		fileInput>>l>>x;
		getline(fileInput,temp);
		getline(fileInput,temp);

		vector<QuatVal> values;

		parse_input(x,temp,values);

		bool answer = get_answer(values);

		if (answer)
		{
			fileOutput<<"Case #"<<i+1<<": YES"<<endl;
		}
		else
		{
			fileOutput<<"Case #"<<i+1<<": NO"<<endl;
		}
	}
	return EXIT_SUCCESS;
}