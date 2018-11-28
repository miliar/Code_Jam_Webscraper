#include<stdio.h>
#include<queue>
#include<iostream>
using namespace std;
int number_of_steps;
string substring_input_string(string input_string)
{
	while(input_string[input_string.length()-1]=='+')
	input_string=input_string.substr(0,input_string.length()-1);
	return input_string;
}

string reverse_string(string input_string)
{
	char temp;
	for(int i=0;i<input_string.length()/2;i++)
	{
			temp=input_string[i];
			input_string[i]=input_string[input_string.length()-1-i];
			input_string[input_string.length()-1-i]=temp;
	}
	if(input_string[input_string.length()-1]=='+')
	{
			input_string=substring_input_string(input_string);
			number_of_steps++;
	}
	for(int i=0;i<input_string.length();i++)
	{

			if(input_string[i]=='+')
			input_string[i]='-';
			else
			input_string[i]='+';
	}
	return input_string;
}


int main()
{
	int test_case=0;
	cin>>test_case;

	for(int i=0;i<test_case;i++)
	{
		string input_string;
		number_of_steps=0;
		cin>>input_string;
		while(input_string.length()>0)
		{
				input_string=substring_input_string(input_string);
				input_string=reverse_string(input_string);
				number_of_steps++;
		}

		cout<<"Case #"<<i+1<<": "<<number_of_steps-1<<endl;
	}
	return 0;
}
