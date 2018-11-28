#include <iostream>
#include <direct.h>
#include <assert.h>
#include <vector>
#include <algorithm>
using namespace std;

int ans1, ans2;
int v1[4][4], v2[4][4];

void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": ";
	cerr << "Case #" << Case+1 << endl;

	ans1--;
	ans2--;
	std::sort(v1[ans1], v1[ans1]+4);
	std::sort(v2[ans2], v2[ans2]+4);  

	vector<int> inter(4);
	vector<int>::iterator it = std::set_intersection(v1[ans1], v1[ans1]+4, v2[ans2], v2[ans2]+4, inter.begin());
	inter.resize(it - inter.begin()); 

	int size = inter.size();
	if (size == 1)
		cout << inter[0];
	else if (size > 1)
		cout << "Bad magician!";
	else 
		cout << "Volunteer cheated!";

	cout << endl;
}

void Run()
{
    int T;
    cin >> T;
	cerr << T << " cases" << endl;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> ans1;
		for (int y=0; y<4; y++)
			for (int x=0; x<4; x++)
				cin >> v1[y][x];

		cin >> ans2;
		for (int y=0; y<4; y++)
			for (int x=0; x<4; x++)
				cin >> v2[y][x];

		// Solve
        runCase(i);
    }
}


void main()
{
    _chdir(".\\Archive_Google");

	#define FILE_NAME "A-small-attempt0" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

    Run();

    //system("pause");
}

