#include <windows.h>
#include <iostream>
#include <fstream>
using namespace std;
char path[260], temp[260];

bool CAbsolutePath(char* storage, size_t size)
{
	// Path
	int bytes;
	storage[size - 2] = '\0'; //memset(storage, 0, size);
	bytes = GetModuleFileName(NULL, storage, size);
	if (bytes == 0)
		return false;
	int i;
	bytes--;
	for (i = bytes;i > 0;i--)
	{
		if (storage[i] == '/' || storage[i] == '\\')
			break;
		else if (i == 0)
			return false;
	}
	storage[i + 1] = '\0';
	return true;
}

/* Process variables */
unsigned int T, i, i1;
unsigned int V, S, s, n;
char c, a;
/* */

int main()
{
	// Init
	if (!CAbsolutePath(path, 260))
	{
		cout << "Path error." << endl;
		while (true);
	}
	else
		cout << "Process path:\n" << path << endl;
	// Process
	ifstream data;
	data.open(strcat(strcpy(temp, path), "in.txt"));
	ofstream file;
	file.open(strcat(strcpy(temp, path), "out.txt"));
	if (data.is_open() && data.good() && file.is_open() && file.good())
	{
		data >> T;
		for (i = 1;i <= T;i++)
		{
			n = 0;
			V = 0;
			data >> S;
			data.get(c);
			for (i1 = 0;i1 <= S;i1++)
			{
				if (i1 > 0 && n < i1)
				{
					V += i1 - n;
					n = i1;
				}
				data.get(c);
				s = c - '0';
				n += s;
			}
			data.get(c);
			file << "Case #" << i << ": " << V;
			if (i < T)
				file << "\n";
		}
		file.close();
		data.close();
	}
	else
	{
		cout << "File stream error." << endl;
		while (true);
	}
	return 0;
}