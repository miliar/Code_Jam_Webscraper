#include <fstream>
using namespace std;

int Find(int * mass, int num, int current);

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	int i;

	int T;
	fin >> T;

	int diners[5000];
	for (int t = 0; t < T; t++)
	{
		int otherresult = 0;
		int num;
		fin >> num;
		for (i = 0; i < num; i++)
		{
			fin >> diners[i];
			if (diners[i] > otherresult)
				otherresult = diners[i];
			//fout << diners[i] << " ";
		}
		//fout << endl;

		//otherresult = Find(diners, num, 0); 
		int result = 0;

		while (true)
		{
			int maxi = -1;
			int maxcount = 0;
			int max2 = -1;
			for (i = 0; i < num; i++)
			{
				if (maxi == -1 || diners[maxi] < diners[i])
					maxi = i; 
			}

			if (otherresult > result + diners[maxi])
				otherresult = result + diners[maxi];
			for (i = 0; i < num; i++)
			{
				if (diners[i] == diners[maxi])
					maxcount++;
				if (diners[i] < diners[maxi])
				{
					if (max2 == -1 || diners[max2] < diners[i])
						max2 = i;
				}
			}


			int goodwork = diners[maxi] / 2;
			//if (diners[maxi] == 9)
			//	goodwork = 3;
			if (diners[maxi] == 9 && maxcount == 1)
			{
				if (max2 == -1 || diners[max2] <= 3 || diners[max2] == 6)
					goodwork = 3;
			}
			if (diners[maxi] <= 2)
				break;

			result++;
			
			diners[num] = diners[maxi] - goodwork;
			diners[maxi] = goodwork;
			num++;
		}

		int maxi = -1;
		for (i = 0; i < num; i++)
		{
			if (maxi == -1 || diners[maxi] < diners[i])
				maxi = i;
		}
		result += diners[maxi];

		if (otherresult < result)
			fout << "Case #" << (t + 1) << ": " << otherresult << endl;
		else
			fout << "Case #" << (t+1) << ": " << result << endl;
	}

	return 0;
}


int Find(int * mass, int num, int current)
{
	return 0;
}