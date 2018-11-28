#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::ostringstream;

using std::vector;

#define NUM_PARAMS 1

//Fair and square

bool roundSquare(int n, int& resulting) {
	if (n < 0)
		return false;
	int root(sqrt(n));
	resulting = root;
	if(n == root*root)
		return true;
	else
	{
		return false;
	}
	
}

int reverseint(int num)
{
	int new_num = 0;
	while(num > 0)
	{
		new_num = new_num*10 + (num % 10);
		num = num/10;
	}
	return new_num;
} 


template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

vector<int> StrToIntArr(string& _str)
{
	vector<int> myVec;

	char *dup = _strdup(_str.c_str());
	
	char * pch;
	pch = strtok (dup," ");
	

	while (pch != NULL)
	{
		myVec.push_back(atoi(pch));
		pch = strtok (NULL, " ");
	}
	free(dup);
	return myVec;
}

int Solve(vector<int> numRange);

string parseCase(int curCase, string* params)
{
	std::string res;
	res.append("Case #");
	res.append(tostr(curCase));
	res.append(": ");
	
	vector<int> numRange = StrToIntArr(params[0]);

	int solution = Solve(numRange);
	

	res.append(tostr(solution));

	res.append("\n");	
	return res;

}

int Solve(vector<int> numRange)
{
	int counter = 0;
	for(int i = numRange[0]; i<numRange[1]+1; i++)
	{
		int resulting = 0;
		if(roundSquare(i, resulting))
		{
			if(reverseint(i) == i)
			{
				if(reverseint(resulting) == resulting)
				{
					++counter;
				}
				
			}

		}
	}	

	return counter;
}



int main(int argc, char* argv[]) 
{ 
	ifstream fin;
	ofstream fout;
		
		fin.clear();
		fout.clear();
			
		fin.open("c.in");
		fout.open("c.out", std::ios::trunc);
	
		//Number of cases
		string numCases;
		getline(fin, numCases);
		cout<<numCases<<endl;

		int curCase = 1;

		string curLine[NUM_PARAMS];

		while(!fin.eof())
		{					
			for(int i = 0; i < NUM_PARAMS; i ++)
			{
				getline(fin,curLine[i]);
			}
			string caseres = parseCase(curCase, curLine);

		
			cout<<caseres;
			fout<<caseres;
			++curCase;
		}

		fin.close();		
		fout.close();

		
    return 0; // return 0 for no errors
}