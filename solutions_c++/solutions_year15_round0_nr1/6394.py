#include<fstream>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

int main(int argc, char *argv[])
{



 	ifstream ip;
	ip.open(argv[1]);

	ofstream op;
	op.open("A-output.txt"); 
	
	int t;
	ip>>t;

	for(int iter=1; iter<=t; iter++)
	{
		op<<"Case #"<<iter<<": ";
		
		int s_max;
		string test_string;
		
		ip>>s_max;
		ip >> test_string;
		
		char test[1002];
		strcpy(test, test_string.c_str());
		
		int standing=0;
		int additional=0;
		
		for(int shyness=0; shyness<=s_max; shyness++)
		{
			int current_people = test[shyness]-48;
			if(standing + additional >= shyness)
			{
				standing = standing + current_people;
			}
			else
			{
				additional += ((shyness) - (standing + additional));
				standing = standing + current_people;
			}
		}
		
		op<<additional<<endl;
		
	}

	
	return 0;
}
