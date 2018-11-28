/*
Copyright (c) 2013, David Liu
All rights reserved. Read the license for more information.
*/

#include <iostream>
#include <fstream>
#define WIN32_LEAN_AND_MEAN 1
#include <windows.h>
using namespace std;
char path[260];
LARGE_INTEGER freqs;
DWORD freq;
ifstream file;
ofstream output;
int count;

bool InitTime()
{
	if (!QueryPerformanceFrequency(&freqs))
	{
		cout << "Failed to initialize high-performance counter.\n";
		cin.get();
		return false;
	}
	freq = freqs.QuadPart / 1000;
	return true;
}

inline DWORD Time()
{
	QueryPerformanceCounter(&freqs);
	return freqs.QuadPart / freq;
}

/* Main */
int main(int argc, char** argv)
{
	// Initialization
	if (argc == 2)
		strcpy(path, argv[1]);
	else
		path[0] = '\0';
	if (!InitTime())
		return -1;
	// Load file
	int row, number, i, c, a, b;
	unsigned char result; // 0 - none found ___ 1 - found only one __ 2 - found more
	int load[4], possible[4];
	file.open("C:/a.txt");
	output.open("C:/output.txt");
	file >> count;
	for (i = 0;i < count;i++)
	{
		cout << i;
		result = 0;
		file >> row;
		for (c = 0;c < 4;c++)
		{
			file >> load[0] >> load[1] >> load[2] >> load[3];
			if (c + 1 == row)
			{
				possible[0] = load[0];
				possible[1] = load[1];
				possible[2] = load[2];
				possible[3] = load[3];
			}
		}
		file >> row;
		for (c = 0;c < 4;c++)
		{
			file >> load[0] >> load[1] >> load[2] >> load[3];
			if (c + 1 == row)
			{
				for (a = 0;a < 4;a++)
				{
					if (result == 2)
						break;
					for (b = 0;b < 4;b++)
					{
						if (possible[a] == load[b]) // Found a match
						{
							if (result == 0)
							{
								result = 1;
								number = possible[a];
							}
							else if (result == 1)
								result = 2;
							break;
						}
					}
				}
			}
		}
		if (result == 2)
			output << "Case #" << i + 1 << ": Bad magician!";
		else if (result == 0)
			output << "Case #" << i + 1 << ": Volunteer cheated!";
		else
			output << "Case #" << i + 1 << ": " << number;
		if (i < count - 1) // Last line
			output << "\n";
	}
	// Quit
	file.close();
	output.close();
	return 0;
}