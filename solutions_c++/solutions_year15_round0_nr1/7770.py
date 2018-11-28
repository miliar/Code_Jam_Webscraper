#include <iostream>
#include <direct.h>
#include <assert.h>
using namespace std;

int Smax;
char S[1001];

int getNum(int idx)
{
	return S[idx]-'0';
}

void runCase(int Case)
{
	cerr << "Case #" << Case+1 << endl;

	int stand = getNum(0);
	int need = 0;
    for (int currS=1; currS<=Smax; currS++)
    {
		int numOfS = getNum(currS);

		if ((numOfS>0) && (stand < currS))
		{
			int currNeed = currS - stand;
			need += currNeed;
			stand += currNeed;
		}

		stand += numOfS;
    }

	cout << "Case #" << Case+1 << ": " << need;
    cout << endl;
}

void Run()
{
    int T;
    cin >> T;
	cerr << T << " cases" << endl;

	for (int i=0; i<T; i++)
	{
		cin >> Smax;
		cin >> S;
   
		// Solve
		runCase(i);
	}
}

void initIO_dir()
{
	string dir(__FILE__);
	dir.erase(dir.rfind("\\"));
	int ret = _chdir(dir.c_str());
	assert(ret == 0);
}

void main()
{
	initIO_dir();

	#define FILE_NAME "A-large" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

    Run();
}

