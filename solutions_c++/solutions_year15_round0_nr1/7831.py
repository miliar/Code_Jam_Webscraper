#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int* toIntArray(string& in)
{
	int length = in.length();
	int *result = new int[length];
	for (int i = 0; i < length; ++i)
	{
		result[i] = in[i] - '0';
	}

	return result;
}

int main(int argc, char** argv)
{
	ifstream *in = new ifstream("input.txt", fstream::in);
	ofstream *out = new ofstream("output.txt", fstream::out);

	int T, maxShyness;
	string line;
	int standing, required, diff;

	*in >> T;

	for (int i = 0; i < T; ++i)
	{
		*in >> maxShyness;
		*in >> line;

		required = 0;
		int *audience = toIntArray(line);
		standing = audience[0];

		for (int i = 1; i < maxShyness + 1; ++i)
		{						
			if (audience[i] != 0 && standing < i)
			{
				diff = i - standing;
				required += diff;
				standing += diff;
			}
			standing += audience[i];
		}
		
		*out << "Case #" << i + 1 << ": " << required << endl;
		delete audience;
	}

	in->close();
	delete in;	
}