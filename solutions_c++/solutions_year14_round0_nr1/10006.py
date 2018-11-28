#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream output;
	output.open ("output01.in");
	int T,n,m, num;
	int x[4]={};
	cin >> T;
	for (int i=0; i<T; ++i)
	{
		int count = 0;
		cin >> n;
		for(int j=0; j<4; ++j)
		{
			for (int k=0; k<4; ++k)
			{
				cin >> m;
				if (j+1 == n)
				{
					x[k] = m;
				}
			}
		}
		cin >> n;
		for(int j=0; j<4; ++j)
		{
			for (int k=0; k<4; ++k)
			{
				cin >> m;
				if (j+1 == n)
				{
					for (int l=0; l<4; ++l)
					{
						if (x[l] == m)
						{
							num = m;
							++count;
						}
					}
				}
			}
		}
		if (count>1)
			output << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		else if(count<1)
			output << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		else
			output << "Case #" << i+1 << ": " << num << endl;
	}
	return 0;
}