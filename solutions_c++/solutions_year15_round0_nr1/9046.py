# include <iostream>
# include <fstream>
# include <string>

using namespace std;

int main()
{
	int times = 0, t;
	ifstream read;
	ofstream write;
	read.open("input.txt");
	write.open("output.txt");

	read >> times;
	t = times;
	t++;
	while (times)
	{
		int maxshy;
		int total_standing = 0;
		int friends = 0;
		string level;

		read >> maxshy;
		read >> level;
		
		for (int i = 0; i <= maxshy; i++)
		{
			if ((level[i] - 48) == 0 && total_standing <= i )
			{
				friends++;
				total_standing++;
			}
			else
				total_standing += (level[i] - 48);
		}

		write << "Case #" << t - times << ": " << friends << endl;
		times--;
	}

	read.close();
	write.close();
	return 0;
}