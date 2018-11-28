#include <cstring>
#include <fstream>
#include <sstream>
#include <string>

using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;

class CodeJamIO
{
private:

	string append(const char* a, const char* b)
	{
		string c(a);
		c += b;
		return c;
	}
public:

	CodeJamIO(const char* naam) : sc(append(naam, ".in").c_str()), ps(append(naam, ".out").c_str())
	{
		if (!sc.is_open() || !ps.is_open())
			throw "foutje";
		index = 0;
		sc >> size;
		//init
		next();
	}

	virtual ~CodeJamIO()
	{
	}

	void print()
	{
		ps << "Case #" << index << ": " << ss.str() << std::endl;
		ss.str("");
	}

	bool hasMore()const
	{
		return index < size;
	}

	void close()
	{
		sc.close();
		ps.close();
	}

private:
	ifstream sc;
	ofstream ps;
	stringstream ss;
	int index;
	int size;
	static int list[];
	int a;
	int b;
public:

	void next()
	{
		//data
		sc >> a >> b;
		index++;
	}

	void solve()
	{
		//calc
		int i = 0;
		while (list[i] < a)
			i++;
		int c = i;
		while (list[i] <= b)
			i++;
		ss << ( i-c);
		print();
	}
private:
	//data
};

using namespace std;
int CodeJamIO::list[] = {0, 1, 4, 9, 121, 484, 10201};

int main()
{
	CodeJamIO cd("C-small-attempt0");
	cd.solve();
	while (cd.hasMore())
	{
		cd.next();
		cd.solve();
	}
	cd.close();
	return 0;
}