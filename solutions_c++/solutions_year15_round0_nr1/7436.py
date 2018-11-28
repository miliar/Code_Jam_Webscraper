#include <iostream>
#include <memory>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>

using namespace std;

inline bool FEq(float x, float y, float epsilon = 1e-6)
	{
	if (-epsilon <= (x - y) && (x - y) <= epsilon)
		return true;

	if (- epsilon <= x && x <= epsilon ||
		- epsilon <= y && y <= epsilon)
		return false;

	float xy_x = (x - y) / x;
	float xy_y = (x - y) / y;
	return	(-epsilon <= xy_x && xy_x <= epsilon) ||
			(-epsilon <= xy_y && xy_y <= epsilon);
	}

class Processor
	{
public:
	void processStdin()
		{
		process(std::cin);
		}
	void processSmall()
		{
		processFile("A-small-attempt0.in");
		}
	void processLarge()
		{
		processFile("A-large.in");
		}

private:
	void processFile(const char *szFileName)
		{
		std::ifstream in(szFileName);
		if (in.is_open())
			process(in);
		in.close();
		}
	void process(std::istream &in)
		{
		int TC;
		char buffer[20];

		// first line is usually counts
		in >> TC;

		// skip a line
		in.getline(buffer, sizeof(buffer));

		for (int tc = 1; tc <= TC; ++tc)
			{
			int Smax;
			in >> Smax;
			string line;
			getline(in, line);
			auto val = solveTestCase(Smax, line.c_str() + 1);

			std::cout << "Case #" << tc << ": " << val << std::endl;
			}
		}
	int solveTestCase(int smax, const char *str)
		{
		int clappers = str[0] - '0';
		int req = 0;
		for (int i = 1; i <= smax; ++i)
			{
			if (clappers < i)
				{
				req += i - clappers;
				clappers = i;
				}
			clappers += str[i] - '0';
			}
		return req;
		}
	};

// real solution
int main7(int argc, char *argv[])
	{
	Processor p;
	p.processStdin();
	return 0;
	}

// small set
int main6(int argc, char *argv[])
	{
	Processor p;
	p.processSmall();
	return 0;
	}

// big set
int main(int argc, char *argv[])
	{
	Processor p;
	p.processLarge();
	return 0;
	}