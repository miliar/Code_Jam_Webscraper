#include <iostream>
#include <fstream>

using namespace std;

int main()
{

	int cases;
	int a;
	int b; 
	int k;
	int ans;
	ofstream output;
	
	output.open("answers.txt");
	ifstream stream;
	stream.open("input.txt");
	stream >> cases;
	for (int casenum = 1; casenum <= cases; casenum++)
	{
		ans = 0;
		stream >> a >> b >> k;
		for (int i = 0; i < a; i++)
		{
			for (int n = 0; n < b; n++)
			{
				int iclone = i;
				int nclone = n;
				iclone &= nclone;
				if (iclone < k)
					ans++;
			}
		}
		//calculate();
		//analyze();
		output << "Case #" << casenum << ": " << ans << endl;
	}


}

void calculate()
{

	
}



