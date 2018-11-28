
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>


using namespace std;




int main()
{
	int T;

	//ifstream fin("C:\\weilin\\Competition\\GCJ20141A\\GCJ20141A\\input.txt");
	ifstream fin("C:\\weilin\\Competition\\GCJ20141A\\GCJ20141A\\A-small-attempt0.in");
	ofstream fout("output.txt");

	fin >> T;

	long long total = 0;


	for (int i = 0; i < T; i++)
	{
		int N;

		fin >> N;
		vector<string> st;
		vector<vector<int> > vec;
		for (int j = 0; j < N; j++)
		{
			string ts;
			fin >> ts;
			st.push_back(ts);
			vector<int> tmp;
			vec.push_back(tmp);
		}
		
		string base; char pre = 0;
		int len = 0;
		for (int j = 0; j < st[0].size(); j++)
		{
			if (st[0][j] != pre) {
				base += st[0][j];
				if (len)
				   vec[0].push_back(len);
				len = 1;
			}
            else 
			    len++;
			pre = st[0][j];
		}

		vec[0].push_back(len);

		bool ok = true;

		for (int j = 1; j < st.size(); j++)
		{
			string b1; char pre = 0;
			len = 0;
			for (int k = 0; k < st[j].size(); k++)
			{
				if (st[j][k] != pre) {
					b1 += st[j][k];
					if (len)
					  vec[j].push_back(len);
					len = 1;
				}
                else
				   len++;
				pre = st[j][k];
			}
			if (base != b1)
			{
				ok = false;
				break;
			}
			vec[j].push_back(len);
		}

		int total = 0;
		if (ok)
		{

			for (int j = 0; j < vec[0].size(); j++)
			{
				int len = 0;
				for (int k = 0; k < vec.size(); k++)
				{
					len += vec[k][j];
				}
				int al = len / N;
				for (int k = 0; k < vec.size(); k++)
				{
					total += abs(vec[k][j] - al);
				}
			}

		}


		if (!ok)
			fout << "Case #" << i + 1 << ": " << "Fegla Won" << endl;
		else
			fout << "Case #" << i + 1 << ": " << total << endl;

	}
	return 0;
}