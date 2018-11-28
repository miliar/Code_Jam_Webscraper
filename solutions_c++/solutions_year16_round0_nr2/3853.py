#include "Libs.h"
#define OUTPUT cout
#define INPUT in

using namespace std;

int nTests;

int main()
{
	ofstream out("output.txt");
	ifstream in("B-large.in");

	in >> nTests;

	for (int i = 1; i <= nTests; ++i)
	{
        int changes = 0;
        string pancakes;
        in >> pancakes;

        for (int i = 0; i < pancakes.size(); ++i)
        {
            if (pancakes[i] != pancakes[max(0, i - 1)]) changes++;
        }

       if (pancakes[pancakes.size() - 1] == '-') changes++;

        out << "Case #" << i << ": " << changes << endl;
	}

	return 0;
}