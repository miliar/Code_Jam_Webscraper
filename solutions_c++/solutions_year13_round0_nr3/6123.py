
#include <iostream>
#include <string>
#include <iomanip>
#include <locale>
#include <sstream>
#include <cmath>
#include <fstream>

using namespace std;

string convertt(int n)
{
	string s;         
	ostringstream convert;   
	convert << n;     
	s = convert.str();
	return s;
}

string reverse (int Number) {
string s;         
ostringstream convert;   
convert << Number;     
s = convert.str();

string result=""; //create a new string and set it to the empty string

for (int i=0; i<s.length( ) ; i++) { //s.length( ) returns the length of a string
		result = s[ i ] + result ; //take the newest character and add it before what we have already
	}
return result;
}

int main()
{
	int n;
	cin >>n;
	ofstream output;
	output.open ("output.txt");
	int a, b;
	string rev , res;
	int counter=0;
	for (int i=0; i<n; i++)
	{
		cin >>a;
		cin >>b;
		counter =0;
		//int aint = atoi(a.c_str());
		//int bint = atoi(b.c_str());
		for (int j= a; j<= b ; j++)
		{
			res = convertt(j);
			rev = reverse(j);
			if (res == rev)
			{
				int val = atoi(rev.c_str());
				int hassqrt = sqrt(val);
				int check = pow(hassqrt , 2);
				if (val == check)
				{
					// kda el number 3ando sqrt w palindrome 3aiza a check el sqrt palindrome wala la2
					string pal = convertt(hassqrt);
					string invpal = reverse(hassqrt);
					if (pal == invpal)
					{
						// kda el check et7a2a2
						counter ++;
					}
				}
			}
		}
		output << "Case #"<< (i+1) <<": "<< counter<<endl;
	}

	output.close();
	return 0;
}