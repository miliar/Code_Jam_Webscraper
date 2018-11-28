#include <iostream>
#include <string>
#include <fstream>


using namespace std;


bool flags[10];
int true_count = 0;
void resetFlags()
{
	true_count = 0;

	for(int i=0; i<10; i++)
		flags[i] = false;
}

void updateFlags(int number)
{
	while(number != 0)
	{
		int digit = number % 10;

		if(!flags[digit])
		{
			true_count++;
			flags[digit] = true;
		}

		number /= 10;
	}
}

int calc(int number)
{
	resetFlags();

	if(number == 0)
		return -1;


	int current = number;


	while(true)
	{
		updateFlags(current);

		if(true_count == 10)
			return current;

		current += number;
	}

	return -1;

}

int main()
{
	ifstream in("A-large.in.txt");
	ofstream out("A-large-out.txt");
	int case_count; 
	in >> case_count;

	for(int i=0; i<case_count; i++)
	{
		int number;
		in >> number;

		int result = calc(number);

		out << "Case #" << i+1 << ": ";

		if(result == -1)
			out << "INSOMNIA";
		else
			out << result;
		out << endl;

	}


	// for(int i=0; i<100; i++)
	// 	cout << i << ":" << calc(i) << endl;


}