
#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <set>
#include <list>
#include <cassert>
#include <memory>
#include <sstream>
#include <set>
#include <map>

using namespace std;

int testCount = 0;
shared_ptr<fstream> sp_file;

class InputReader
{
	fstream m_fileStream;
	char* m_pBuffer;
	static const int BufferSize = 1024 * 1024;

public:
	InputReader(const char* fileName)
		: m_fileStream(fileName)
	{
		if (!m_fileStream)
			throw "File not found!";

		m_pBuffer = new char[1024 * 1024];
	}

	~InputReader()
	{
		delete m_pBuffer;
		m_pBuffer = nullptr;
	}

	bool IsEof() const
	{
		return m_fileStream.eof();
	}

	string GetNextLine()
	{
		m_fileStream.getline(m_pBuffer, BufferSize);
		return string(m_pBuffer);
	}
};

int ReadNumberFromLine(const string& line)
{
	return atoi(line.c_str());
}

bool IsPalyndrome(long long number)
{
	char buffer[1000];
	sprintf(buffer, "%d", number);
	int size = strlen(buffer);

	int start = 0;
	int end = size - 1;
	while (start < end)
	{
		if (buffer[start] != buffer[end])
			return false;

		start++;
		end--;
	}

	return true;
}

bool IsFairAndQuare(long long number)
{
	if (!IsPalyndrome(number))
		return false;

	long double squareRoot = sqrt(static_cast<long double> (number));
	long long intSquareRoot = (long long) squareRoot;
	
	if (intSquareRoot * intSquareRoot != number)
		return false;

	return IsPalyndrome(intSquareRoot);
}


int Solve(int start, int end)
{
	long long i = start;
	int count = 0;

	while (i <= end)
	{
		if (IsFairAndQuare(i))
			count++;
		i++;
	}

	return count;
}

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		cout << "must inform the file name in the command line" << endl;
		return -1;
	}
	
	InputReader reader(argv[1]);

	string line = reader.GetNextLine();
	int testCount = ReadNumberFromLine(line);

	for (int i = 0; i < testCount; i++)
	{
		line = reader.GetNextLine();
		istringstream stream(line);

		int start;
		stream >> start;

		int end;
		stream >> end;

		int solution = Solve(start, end);

		cout << "Case #" << (i + 1) << ": " << solution << endl;
	}

	return 0;
}
