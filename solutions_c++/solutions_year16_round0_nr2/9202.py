#include<iostream>
#include<string.h>
using namespace std;

int IsHappy(char *pancakes)
{
	int i=0;
	int no_of_pancakes=strlen(pancakes);
	while(i<no_of_pancakes)
	{
		if(pancakes[i] == '-')
			break;
		i++;
	}
	//cout<<"returning from the is happy"<<endl;
	//cout<<"i = "<<i<<endl;
	if(i<no_of_pancakes)
		return 0;

	return 1;
}

void flip_stack(char *pancakes)
{
	int no_of_pancakes,counter , i=0;
	char starting_char;
	no_of_pancakes = strlen(pancakes);
	starting_char=pancakes[0];
	while(starting_char == pancakes[counter])
		counter++;
	if(starting_char == '-')
		while(counter--)
		 	pancakes[counter] = '+';			
	else
		while(counter--)
		 	pancakes[counter] = '-';	
}

int main()
{
	int no_of_test_cases,no_of_finished_cases = 0,no_of_flips=0 , temp;
	char pancakes[1000];
	cin>>no_of_test_cases;
	
	while(no_of_test_cases > no_of_finished_cases)
	{
		no_of_finished_cases++;
		no_of_flips = 0;
		cin>>pancakes;
		while(IsHappy(pancakes)==0)
		{
			cout<<flush;
			flip_stack(pancakes);
			//cout<<pancakes<<endl;
			//cin>>temp;
			no_of_flips++;
		}
		/* printing results */
		cout<<"Case #"<<no_of_finished_cases<<": "<<no_of_flips<<endl;
	}
}