#include "Libs.h"

using namespace std;

int nTests;

int main()
{
	ofstream out("output.txt");
	ifstream in("input.txt");

	in >> nTests;

	for (int i = 0; i < nTests; ++i)
	{
        string word, str = "";
        in >> word;
        str = word[0];

        for (int j = 1; j < word.length(); ++j)
        {
            if (word[j] >= str[0])
                str = word[j] + str;
            else
                str = str + word[j];
        }
        out << "Case #" << (i + 1) << ": " << str << endl;
	}

	return 0;
}