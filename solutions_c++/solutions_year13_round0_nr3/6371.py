#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool palindrome_test(string word) 
{
	int len ; 
	len = word.length();
	bool a = false;
	for(int i = 0 ; i<len ; i++)
	{
		if(word[i] == '.')
		
		{
			word[i] = '\0';
			word.erase (word.begin()+i,word.end());		
			a = true;
	}
	if (a) break;		
		
	}
	bool x = true ;
	if(word.size() == 1)
		return true;
	len = word.size();
	for(int i = 0 ; i <= len-1 ; i++)
	{
		if(i < (len-1-i))
		{
			if(word[i] != word[len-i-1])
			{
				x = false ;	
			}
		}
		else break ;
	}
	return x ;
}

int main()
{
	string infile_name = "D:\\A-small-practice.in";
	fstream infile(infile_name,fstream::in);
	fstream outfile("D:\\output1.out",fstream::out);
	string temp , state ;
	getline(infile,temp);
	int num_test_cases = atoi(temp.c_str());
	vector <string> store;
	for(int i = 1 ; i <= num_test_cases ; i++)
	{
		int A, B , count;
		count = 0 ;
		getline(infile,temp);
		char * tempchar = new char[temp.size() + 1];
		copy(temp.begin(), temp.end(), tempchar);
		tempchar[temp.size()] = '\0'; 
		char *p = strtok (tempchar, " ");
		A = atoi(p);
		p = strtok (NULL, " ");
		B = atoi(p);
		delete[] tempchar;
		string thenumber;
		for(int i = A ; i <= B ; i++)
		{
			thenumber = to_string(i);
			if(palindrome_test(thenumber))
			{// fair

				if(sqrt(i) == floor(sqrt(i)))
				{
					if(palindrome_test(to_string(sqrt(i))))  // and square
						count++;
				}
			}
		}

		outfile<<"Case #"<<i<<": "<<count<<endl;

	}

	return 0;
}
