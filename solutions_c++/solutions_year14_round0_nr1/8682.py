#include <fstream>

using namespace std;

int main()
{
	int T;
	ifstream ifs("input.txt");
	ofstream ofs("out.txt");
	ifs >> T;
	int first_array[4][4];
	int second_array[4][4];
	int first_answer, second_answer;
	
	int answer = 0;
	for (int i = 0; i < T; i++)
	{
		int count = 0;
		ifs >> first_answer;
		for (int y = 0; y < 4; y++)
		{
			for (int z = 0; z < 4; z++)
			{
				ifs >> first_array[y][z];
			}
		}
		ifs >> second_answer;
		for (int y = 0; y < 4; y++)
		{
			for (int z = 0; z < 4; z++)
			{
				ifs >> second_array[y][z];
			}
		}
		second_answer--;
		first_answer--;
		for (int y = 0; y < 4; y++)
		{
			for (int z = 0; z < 4; z++)
			{
				if (first_array[first_answer][y] == second_array[second_answer][z])
				{
					count++;
					answer = second_array[second_answer][z];
				}
			}
		}
		switch (count)
		{
			case 1:
				ofs << "Case #" << (i+1) << ": " << answer<<endl;
				break;
			case 0:
				ofs << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
				break;
			default:
				ofs << "Case #" << (i + 1) << ": Bad magician!" << endl;
				break;
		}
	}
}
