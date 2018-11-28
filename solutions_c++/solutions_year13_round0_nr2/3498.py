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
		matrix = new int*[100];
		for (int i = 0; i < 100; i++)
			matrix[i] = new int[100];
		rij = new int[100];
		kolom = new int[100];
		next();
	}

	virtual ~CodeJamIO()
	{
		for (int i = 0; i < 100; i++)
			delete[] matrix[i];
		delete[] rij;
		delete[] kolom;
		delete[] matrix;
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
	int** matrix;
	int n;
	int m;
	int* rij;
	int* kolom;
public:

	void next()
	{
		//data
		sc >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				sc >> matrix[i][j];
		for (int i = 0; i < n; i++)
		{
			kolom[i] = matrix[i][0];
			for (int j = 1; j < m; j++)
				if (kolom[i] < matrix[i][j])
					kolom[i] = matrix[i][j];
		}
		for (int j = 0; j < m; j++)
		{
			rij[j] = matrix[0][j];
			for (int i = 1; i < n; i++)
				if (rij[j] < matrix[i][j])
					rij[j] = matrix[i][j];
		}
		index++;
	}

	void solve()
	{
		//calc
		bool inorde = true;
		int i = 0;
		while (i < n && inorde)
		{
			int j = 0;
			while (j < m && inorde)
			{
				inorde = (matrix[i][j] == kolom[i]) || (matrix[i][j] == rij[j]);
				j++;
			}
			i++;
		}
		ss << (inorde?"YES" : "NO");
		print();
	}
private:
	//data
};

using namespace std;

int main()
{
	CodeJamIO cd("B-large");
	cd.solve();
	while (cd.hasMore())
	{
		cd.next();
		cd.solve();
	}
	cd.close();
	return 0;
}
