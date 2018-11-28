#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("haha.txt");
	int T;
	string dataset;
	int index = 1;
	ifs >> T;
	char first;
	string res;
	while (index <= T)
	{
		res = "";
		ifs >> dataset; 
		int size = dataset.size();
		first = dataset[0];
		res.push_back(first);
		string temp;
		for (int i = 1; i < size; i++)
		{
			temp.push_back(dataset[i]);
			if (dataset[i] >= first)
			{
				res = temp + res;
				first = dataset[i];
			}
			else
			{
				res = res + temp;
			}
			temp = "";
		}
		ofs << "Case #" << index++ << ": " << res << endl;
	}
	ifs.close();
	ofs.close();
}