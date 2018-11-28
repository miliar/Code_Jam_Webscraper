#include <iostream>
#include <fstream>
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
unsigned long pos = 0;
bool* output;
unsigned char* hmap;

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

void Process()
{
	unsigned int temp, temp2, temp3, temp4, sizem, sizen;
	bool hline,vline;
	size = ReadToInt(&pos);
	// Assign data to hmap
	output = new bool[size];
	for (temp = 0; temp < size; temp++)
	{
		// Allocate
		sizen = ReadToInt(&pos);
		sizem = ReadToInt(&pos);
		hmap = new unsigned char[sizen * sizem];
		for (temp2 = 0; temp2 < sizen * sizem; temp2++)
		{
			hmap[temp2] = ReadToInt(&pos);
		}
		// Check if possible or not
		output[temp] = true;
		for (temp2 = 0; temp2 < sizen; temp2++)
		{
			for (temp3 = 0; temp3 < sizem; temp3++)
			{
				// Select one point in this "grid", check if the 2 lines crossing it are possible. If one of them is, it passes. Else entire heightmap is impossible.
				hline = true;
				for (temp4 = 0; temp4 < sizem; temp4++)
				{
					if (hmap[temp2 * sizem + temp4] > hmap[temp2 * sizem + temp3])
					{
						hline = false;
						break;
					}
				}
				vline = true;
				for (temp4 = 0; temp4 < sizen; temp4++)
				{
					if (hmap[temp4 * sizem + temp3] > hmap[temp2 * sizem + temp3])
					{
						vline = false;
						break;
					}
				}
				if (!vline && !hline)
				{
					output[temp] = false;
					break;
				}
			}
			if (!output[temp])
				break;
		}	
		// Delete
		delete[] hmap;
	}
	delete[] buf;
}

void Output(char*path)
{
	unsigned int temp = 0;
	char msg[23];
	strcat(path,".out");
	ofstream file(path);
	if (file.is_open())
	{
		while (file.good() && temp < size)
		{
			if (output[temp])
				strcpy(msg, "YES");
			else
				strcpy(msg, "NO");
			file << "Case #" << (temp+1) << ": " << msg;
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