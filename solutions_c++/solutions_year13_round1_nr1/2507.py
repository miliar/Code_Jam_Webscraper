
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
#include <cmath>

using namespace std;

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

long long Solve(long long r, long long t)
{
	long long rings = 0;
	long long nextRingRadius = r;
	long double paintRemaining = t;
	const long double pi = 3.14159265358979323846;
	while(true)
	{

		long double area = (nextRingRadius + 1) * (nextRingRadius + 1);
		area -= (nextRingRadius) * (nextRingRadius);

		long double paintNeeded = area;
		paintRemaining -= paintNeeded;
		if (paintRemaining < 0)
			break;
		rings++;
		nextRingRadius += 2;
	}

	return rings;
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

		long long r;
		stream >> r;

		long long t;
		stream >> t;

		int solution = Solve(r, t);

		cout << "Case #" << (i + 1) << ": " << solution << endl;
	}

	return 0;
}
