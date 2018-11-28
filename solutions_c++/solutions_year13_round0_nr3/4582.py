#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

/*
All the code below is written by me.
None of the code has been copied from any sources.
*/

/* Globals */
bool quit = false;
char fullpath[301];
char* buf;

/* Variables */
unsigned int size;
unsigned long pos;
unsigned short* output;

/* Functions */
bool Read(const char* path)
{
	ifstream file(path, ios::binary);
	if (file.is_open()) // Successfully opened
	{
		// Get size of file
		unsigned long beg, end, length;
		beg = file.tellg();
		file.seekg(0, ios::end);
		end = file.tellg();
		length = end - beg;
		file.seekg(0, ios::beg);
		if (length>0)
		{
			// Allocate array
			buf = new char[length+1];
			// Read file
			file.read(buf, length);
			file.close();
			buf[length]='\0';
			if (file)
			{
				cout << "Successfully read file." << endl;
				return true;
			}
			else
			{
				cout << "Failed to extract all data successfully." << endl;
				delete[] buf;
			}
		}
		else
			cout << "Reading an empty file." << endl;
	}
	else
		cout << "Failed to open this file." << endl;
	return false;
}

unsigned int ReadToInt(unsigned long* curpos)
{
	unsigned char count = 0;
	char object[11];
	int result;
	// Make sure to skip the whitespaces
	while (isspace(buf[*curpos]) != 0)
	{
		(*curpos)++;
	}
	// Read first number
	while (isspace(buf[*curpos]) == 0 && buf[(*curpos)] != '\0')
	{
		object[count] = buf[(*curpos)];
		(*curpos)++;
		count++;
	}
	object[count] = '\0';
	sscanf(object, "%d", &result);
	return result;
}

bool IsPalindrome(unsigned int value)
{
	bool fair = true;
	unsigned int temp;
	unsigned char length;
	char object[11];
	// Is it a fair number?
	sprintf(object, "%d", value);
	length = strlen(object);
	for (temp = 0; temp < (unsigned int)floor((float)length/2.0f); temp++)
	{
		if (object[temp] != object[(unsigned int)length - temp - 1])
		{
			fair = false;
			break;
		}
	}
	return fair;
}

void Process()
{
	unsigned int temp, temp2, temp3, tmin, tmax;
	bool fair, square;
	pos = 0;
	size = ReadToInt(&pos);
	// Assign data to chests
	output = new unsigned short[size];
	for (temp = 0; temp < size; temp++)
	{
		// Retrieve data
		tmin = ReadToInt(&pos);
		tmax = ReadToInt(&pos);
		// Check
		output[temp] = 0;
		for (temp2 = tmin; temp2 <= tmax; temp2++)
		{
			// Is it a fair number?
			fair = IsPalindrome(temp2);
			// Is it a square of a fair number?
			if (fair)
			{
				temp3 = 0;
				square = false;
				while (temp3 * temp3 <= temp2)
				{
					temp3++;
					if (IsPalindrome(temp3))
					{
						if (temp2 == temp3 * temp3)
						{
							square = true;
							break;
						}
					}
				}
			}
			// Add to the counter
			if (fair && square)
			{
				cout << temp2 << endl;
				output[temp]++;
			}
		}
	}
	delete[] buf;
}

void Output(char*path)
{
	unsigned int temp = 0;
	strcat(path,".out");
	ofstream file(path);
	if (file.is_open())
	{
		while (file.good() && temp < size)
		{
			file << "Case #" << (temp+1) << ": " << output[temp];
			if (temp < size - 1)
				file << endl;
			temp++;
		}
		file.close();
		cout << "Successfully exported output file." << endl;
	}
	else
		cout << "Failed to create output file." << endl;
	// Clear memory
	delete[] output;
}

/* Main */
int main()
{
	while (!quit)
	{
		cout << "Enter full path of file:" << endl;
		cin >> fullpath;
		if (Read(fullpath))
		{
			Process();
			Output(fullpath);
		}
		cout << "Process another file? (Y/N)" << endl;
		cin >> fullpath;
		if (fullpath[0] == 'N')
			quit = true;
	}
	return 0;
}