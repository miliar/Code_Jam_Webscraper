#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;


int main(int argc, char ** argv)
{
	int S_max        =0;
	int case_number  =1;	
	int total_cases	 =0;
	string input_string;
	int Person_standing=0;
	int Friends_to_invite=0;
	
	getline(cin,input_string);	
	total_cases = atoi(input_string.c_str() );
		
	for(;case_number <= total_cases; ++case_number)
	{
		Person_standing=0;
		Friends_to_invite=0;
		cin >> S_max;
		++S_max;
		cin >> input_string;
			
		for(int i=0; i<S_max;++i)
		{
			if( input_string[i] != '0')
			{
				Person_standing += input_string[i]-0x30;
			}
			
			while( Person_standing < i+1)
			{
				++Friends_to_invite;
				++Person_standing;
			}
		}
					
		cout << "Case #" << case_number <<": ";
		cout << Friends_to_invite <<endl;
	}	
}
