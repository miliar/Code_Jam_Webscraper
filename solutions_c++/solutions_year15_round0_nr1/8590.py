#include<fstream>
#include <string>
using namespace std;

int main()
{
	ifstream f("A-small-attempt0.in");
	ofstream g("A-small-attempt0.out");

	int T;
	f >> T;
	for (int i = 1; i <= T; i++)
	{
		int s;
		string dataset;
		f >> s >> dataset;
		
		int noFriends = 0;
		int audience = dataset[0] - '0';

		for (int j = 1; j < dataset.length(); j++)
		{
			int aditionalFriends = 0;
			if (audience < j && dataset[j] != '0')
			{
				aditionalFriends = j - audience;
				noFriends += aditionalFriends;
			}
			audience = audience + aditionalFriends + (dataset[j] - '0');
		}
		g << "Case #" << i << ": " << noFriends << '\n';
	}

	f.close();
	g.close();

	return 0;
}