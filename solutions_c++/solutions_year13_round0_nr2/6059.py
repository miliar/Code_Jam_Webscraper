#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


int main()
{
	ifstream in("B-small-attempt3.in");
	ofstream out("B-small-attempt3.out");

	int T;
	in>>T;

	for (int Case = 0; Case < T; Case++)
	{
		string answer = "YES";
		int m;
		int n;
		in>>m>>n;

		vector< vector<int> > lawn(m);
		int max = 0;

		for (int i = 0; i < lawn.size(); i++)
		{
			lawn[i].resize(n);
			for (int j = 0; j < lawn[i].size(); j++)
			{
				in>>lawn[i][j];
				if(lawn[i][j] > max)
					max = lawn[i][j];
			}
		}
		//check vertical
		for (int j = 0; j < lawn[0].size(); j++)
		{
			if(lawn[0][j] != max)
			{
				bool right = true;
				for (int i = 0; i < lawn.size(); i++)
				{
					if(lawn[i][j] == max)
					{	
						right = false;
						break;
					}
				}
				if (right)
				{
					for (int i = 0; i < lawn.size(); i++)
					{
						lawn[i][j] = 0;
					}  
				}
			}
		}
		//check horizontal
		for (int i = 0; i < lawn.size(); i++)
		{
			if(lawn[i][0] != max)
			{
				bool right = true;
				for (int j = 0; j < lawn[i].size(); j++)
				{
					if(lawn[i][j] == max)
					{	
						right = false;
						break;
					}
				}
				if (right)
				{
					for (int j = 0; j < lawn[i].size(); j++)
					{
						lawn[i][j] = 0;
					}  
				}
			}
		}
		//last check
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if(lawn[i][j] != max && lawn[i][j] != 0)
				{
					answer = "NO";
					break;
				}
			}
		}
		
		out<<"Case #"<<Case + 1<<": "<<answer<<endl;
	}

	in.close();
	out.close();

	return 0;
}