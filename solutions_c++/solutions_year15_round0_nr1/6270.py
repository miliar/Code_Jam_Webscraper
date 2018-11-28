#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int T;
	int friends, people, shy;
	char stringa [1001];
	in >> T;

	for (int i = 0; i < T; ++i)
	{
		in >> skipws >> shy;

		for (int k = 0; k <= shy; k++)
		{
			in >> stringa[k];
		}
		friends = 0;
		people = 0;
		for (int j = 0; j <= shy; ++j)
		{

			if(people < j)
			{
				friends += j - people;
				people += j - people;
			}
			people += stringa[j] - 48;
		}
		out << "Case #" << i+1 <<": "<< friends << endl;
	}
}

