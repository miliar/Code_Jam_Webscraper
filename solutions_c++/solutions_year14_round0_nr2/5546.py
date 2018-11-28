#include <iostream>
#include <direct.h>
#include <assert.h>
using namespace std;

double C, F, X;

void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": ";
	cerr << "Case #" << Case+1 << endl;

	double prod = 2;
	double totalTime = 0;

	while (true)
	{
		double time2C = C / prod;
		double time2X = X / prod;
		double time2nextX = X / (prod + F);

		if (time2X - time2nextX < time2C)	// stop point - no need to advance
		{
			totalTime += time2X;
			break;
		}
		else 
		{
			totalTime += time2C;
			prod += F;
		}
	}

	printf("%.7lf \n", totalTime);
	//cout << endl;
}

void Run()
{
    int T;
    cin >> T;
	cerr << T << " cases" << endl;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> C;
		cin >> F;
		cin >> X;

		// Solve
        runCase(i);
    }
}


void main()
{
    _chdir(".\\Archive_Google");

	#define FILE_NAME "B-large" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

    Run();

    //system("pause");
}

