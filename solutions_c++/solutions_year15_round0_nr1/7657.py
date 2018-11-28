#include<fstream>
#include<string>
using namespace std;
int main(void)
{
	ifstream fin;
	ofstream fout;
	fin.open("1.in");
	int i,j;
	int cases,*levels,**seq;
	int friends,stand,total;
	string temp;
	fin>>cases;
	levels = new int[cases];
	seq = new int *[cases];
	for (i = 0; i < cases; i++)
	{
		fin>>levels[i];
		seq[i] = new int[levels[i]+1];
		fin>>temp;
		for (j = 0; j <= levels[i]; j++)
		{

			*(seq[i]+j) = temp[j] - 48;
		}
	}
	fin.close();
	fout.open("1.out");
	for (i = 0; i < cases; i++)
	{
		friends = 0;
		stand = 0;
		total = 0;
		for (j = 0; j <= levels[i]; j++)
		{
			total += *(seq[i]+j);
			if (stand >= j)
			{
				stand += *(seq[i]+j);
			}
			else 
			{
				friends += j - stand;
				total += j - stand;
				stand += *(seq[i]+j) + j - stand;
			}
		}
		fout<<"Case #"<<i+1<<": "<<friends<<endl;
	}
	fout.close();

	return 0;
}