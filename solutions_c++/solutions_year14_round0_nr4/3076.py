#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int testcase, i, j, datanum, awin, bwin;
	double num;
	vector<double> a,b;
	vector<double> ap,bp;

	ifstream infile("D-large.in");
	ofstream outfile("outfile.out");
	if(infile && outfile)
	{
		infile >> testcase;
		for(i = 0; i < testcase; i++)
		{
			infile >> datanum;
			awin = 0;
			bwin = 0;
			a.clear();
			b.clear();
			ap.clear();
			bp.clear();
			for(j = 0; j < datanum; j++)
			{
				infile >> num;
				a.push_back(num);
			}
			for(j = 0; j <datanum; j++)
			{
				infile >> num;
				b.push_back(num);
			}
			ap.assign(a.begin(), a.end());
			bp.assign(b.begin(), b.end());

			sort(a.begin(), a.end());
			sort(b.begin(), b.end());
			sort(ap.begin(), ap.end());
			sort(bp.begin(), bp.end());

			for(vector<double>::iterator it1 = a.begin(); it1 != a.end(); it1++)
			{
				for(vector<double>::iterator it2 = b.begin(); it2 != b.end(); it2++)
				{
					if(*it1 > *it2)
					{
						++awin;
						b.erase(it2);
						break;
					}
				}
			}
			for(vector<double>::iterator it3 = bp.begin(); it3 != bp.end(); it3++)
			{
				for(vector<double>::iterator it4 = ap.begin(); it4 != ap.end(); it4++)
				{
					if(*it3 > *it4)
					{
						++bwin;
						ap.erase(it4);
						break;
					}
				}
			}
			
			outfile << "Case #" << i+1 << ": " << awin << " " << datanum - bwin << endl;
		}
		infile.close();
		outfile.close();

	}
	return 0;
}