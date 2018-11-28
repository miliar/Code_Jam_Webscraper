#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int isWhiteSpace(char* str)
{
	int i=0;
	if(str[i] == '\0')
		return 1;

	while((str[i] == ' ') || (str[i] == '\t'))
	{
		i++;
		if(str[i] == '\0')
			return 1;
	}

	return 0;
} 

int tokenize(char* ptr, int* row)
{
	int i,j;
	int count = 0;

	i = 0;
	j = 0;

	while(1)
	{
		while((ptr[i] != '\0') && (ptr[i] != ' '))
		{
			i++;
		}

		if(ptr[i] == '\0')
		{
			row[count] = atoi(ptr + j);
			count++;
			return count;
		}
		ptr[i] = '\0';
		i++;
		row[count] = atoi(ptr+j);
		j = i;
		count++;
	}
}


int main()
{
	ifstream input;
	char* buffer = new char[20];
	input.open("A-small-attempt0.in");

	ofstream output;
	output.open("output");

	int numTest;
	int firstRow;
	int secondRow;

	int* f_row = new int[4];
	int* s_row = new int[4];

	input.getline(buffer,20);
	tokenize(buffer,&numTest);
//	cout << numTest << '\n';

	int test = 0;

	for(int test=0;test<numTest;test++)
	{
		input.getline(buffer,20);
		tokenize(buffer,&firstRow);
//		cout << firstRow << '\n';

		for(int i=0;i<firstRow;i++)
			input.getline(buffer,20);

		tokenize(buffer,f_row);

		for(int i=firstRow;i<4;i++)
			input.getline(buffer,20);
		
//		for(int j=0;j<4;j++)
//			cout << f_row[j] << '\t';
//		cout << '\n';

		input.getline(buffer,20);
		tokenize(buffer,&secondRow);
//		cout << secondRow << '\n';

		for(int i=0;i<secondRow;i++)
			input.getline(buffer,20);

		tokenize(buffer,s_row);

		for(int i=secondRow;i<4;i++)
			input.getline(buffer,20);

//		for(int j=0;j<4;j++)
//			cout << s_row[j] << '\t';
//		cout << '\n';

		int match = 0;
		int val;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(f_row[i] == s_row[j])
				{
					val = f_row[i];
					match++;
				}
			}
		}
		
		if(match == 1)
			output << "Case #" << test+1 << ": " << val << '\n';
		else
		{
			if(match == 0)
				output << "Case #" << test+1 << ": Volunteer cheated!\n";

			else
				output << "Case #" << test+1 << ": Bad magician!\n";
		}
				
	}

	input.close();
	output.close();

	return 0;
}

