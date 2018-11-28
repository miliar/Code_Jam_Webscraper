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
const double pi = acos(-1.0L);
int loop1,loop2,loop3,loop4;

/* Variables */
unsigned int size;
unsigned long long pos;
unsigned int* output;

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

int ReadToInt(unsigned long long* curpos)
{
	unsigned char count = 0;
	char object[20];
	int result;
	// Make sure to skip the whitespaces
	while (isspace(buf[(*curpos)]) != 0)
	{
		(*curpos)++;
	}
	// Read first number
	while (isspace(buf[(*curpos)]) == 0 && buf[(*curpos)] != '\0')
	{
		object[count] = buf[(*curpos)];
		(*curpos)++;
		count++;
	}
	object[count] = '\0';
	sscanf(object, "%i", &result);
	return result;
}

char* ReadToString(unsigned long long* curpos)
{
	unsigned int count = 0;
	unsigned long long savpos;
	char* object;
	// Make sure to skip the whitespaces
	while (isspace(buf[(*curpos)]) != 0)
	{
		(*curpos)++;
	}
	savpos = (*curpos);
	// Count
	while (isspace(buf[(*curpos)]) == 0 && buf[(*curpos)] != '\0')
	{
		(*curpos)++;
		count++;
	}
	object = new char[count + 1];
	count = 0;
	(*curpos) = savpos;
	// Read first number
	while (isspace(buf[(*curpos)]) == 0 && buf[(*curpos)] != '\0')
	{
		object[count] = buf[(*curpos)];
		(*curpos)++;
		count++;
	}
	object[count] = '\0';
	return object;
}

bool IsVowel(char a)
{
	if (a=='a'||a=='e'||a=='i'||a=='o'||a=='u')
		return true;
	return false;
}

void Process()
{
	// Setup
	pos = 0;
	size = ReadToInt(&pos);
	output = new unsigned int[size];
	// Code
	int n, namelen;
	int begin, end;
	bool substring;
	char* name;
	for (loop1 = 0;loop1 < size; loop1++)
	{
		output[loop1] = 0;
		name = ReadToString(&pos);
		namelen = strlen(name);
		n = ReadToInt(&pos);
		begin = 0;
		while (begin < namelen)
		{
			loop3 = 0;
			for (loop2 = begin;loop2 < namelen;loop2++)
			{
				if (!IsVowel(name[loop2]))
					loop3++;
				else
					loop3 = 0;
				if (loop3 == n)
				{
					for (loop4 = loop2;loop4 < namelen;loop4++)
					{
						output[loop1]++;
					}
					begin++;
					break;
				}
			}
			if (loop2 == namelen)
				begin++;
		}
		delete[] name;
	}
	// Cleaning
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