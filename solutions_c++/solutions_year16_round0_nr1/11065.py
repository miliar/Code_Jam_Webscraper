#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int testcases;
	int input;
	int current;
	int original;
	int individual;
	int count;
	bool tracker [10];
	bool done = false;
	bool insomnia;
	ofstream fout;
	fout.open ("output.txt");
	cin >> testcases;
	
	for(int j=0; j<testcases; j++)
	{	
		for(int i=0; i<10; i++)
		{
			tracker[i]=false;
		}
		done = false;
		insomnia = false;
		count = 1;
		cin >> input;
		current = input;
		original = input;
		while(!done)
		{
			current = original * (count);
			input = current;
			
			do
			{
				individual = input%10;
				//cout << individual << endl;
				tracker[individual] = true;
				input/=10;
			}
			while(input > 0);
			
			done = true;
			
			for(int k=0; k<10; k++)
			{
				//cout << k << " " << tracker[k] << endl;
				if(tracker[k] == false)
					done = false;
			}
			count ++;
			if(count > 1000)
			{
				insomnia = true;
				done = true;
			}
			
		}
		
		if(insomnia)
		{
			fout << "Case #" << j+1 << ": INSOMNIA" << endl;
		}
		else
		{
			fout << "Case #" << j+1 << ": " << current << endl;
		}
	}
	
	fout.close();
}