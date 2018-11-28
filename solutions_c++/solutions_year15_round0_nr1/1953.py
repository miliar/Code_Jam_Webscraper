#include <fstream>
#include <unordered_map>
#include <string>
using namespace std;

int shy[1005];

int main()
{
	int t;
	ifstream infile("F:\\A-large.in");
	ofstream outfile("F:\\A-large.out");
	infile >> t;
	for (int i = 1; i <= t;i++)
	{
		int mindex;
		string s;
		infile >> mindex>>s;
		int xiabiao=0;
		for (string::iterator it=s.begin(); it!=s.end(); ++it)
		{
			shy[xiabiao]=*it-'0';
			xiabiao++;
		}
		int invite=0;
		int current=shy[0];
		for(int j=1;j<=mindex;++j)
		{
			if(shy[j]==0)
				continue;
			if(current>=j)
				current+=shy[j];
			else
			{
				int need=j-current;
				invite+=need;
				current+=need+shy[j];
			}
		}

		outfile << "Case #" << i << ": " <<invite<< endl;
	}
	infile.close();
	outfile.close();
	return 0;
}