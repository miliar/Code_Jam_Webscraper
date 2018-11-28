#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("A-large.in");

	ofstream out("A-large.out");
	int T;
	in >> T;
	for (int i = 0; i < T; i++)
	{
		int maxShy;
		in >> maxShy;

		string audience;
		in >> audience;

		int toInvite = 0;

		int standing = audience.at(0) - 48;

		for (int k = 1; k < audience.size(); k++)
		{
			if (standing < k)
			{
				toInvite += k - standing;
				standing += k - standing;
			}
			standing += audience.at(k) - 48;
		}
		out << "Case #" << i + 1 << ": " << toInvite << endl;
	}


	return 0;
}