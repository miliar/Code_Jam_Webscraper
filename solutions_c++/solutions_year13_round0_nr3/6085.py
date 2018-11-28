#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

// compiled on OSX with: clang++ -std=c++11  -stdlib=libc++ C.cpp

using namespace std;

typedef unsigned long long bigint; 

bool is_palindrome(bigint input)
{
	string str = std::to_string(input);
	
	for(int i=0; i<str.size()/2; i++)
	{
		if(str[i] != str[str.size()-1-i]) return false;
	}
	
	return true;
}

int main()
{
	ifstream fin;
	ofstream fout; 
	
	fin.open("input.txt");
	fout.open("output.txt");
	
	
	int N;
	bigint low, high, count;
	fin >> N;
	
	
	for(int i=0; i<N; i++)
	{
		fin >> low >> high;
		count = 0;
		for(int i=low; i<=high; i++)
		{
			if(int(sqrt(i))*int(sqrt(i))==i && is_palindrome(i) && is_palindrome(int(sqrt(i))))
			{
				count++;
			}
		}
		fout << "Case #" << (i+1) << ": " << count << endl;
	}
	
	fin.close();
	fout.close();
	
	
	return 0;
}