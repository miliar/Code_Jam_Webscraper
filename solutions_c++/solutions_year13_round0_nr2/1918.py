#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("in.txt","r", stdin);
	freopen("out.txt", "w", stdout);
	int n = 0;
	cin >> n;

	int r,c = 0;
	vector<vector<int> > field = vector<vector<int> >();

	for(int i=0;i<n;i++)
	{
		field.clear();
		cin >> r >> c;
		for (int j = 0;j<r;j++)
		{
			vector<int> temp;
			for (int k=0;k<c;k++)
			{
				int tmp = 0;
				cin >> tmp;
				temp.push_back(tmp);
			}
			field.push_back(temp);
		}

		/*for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				cout << field.at(j).at(k) << " ";
			}
			cout << endl;
		}*/

		while(true)
		{
			int t = 0;
			while(t < field.size())
			{
				if(field.at(t).empty())
				{
					field.erase(field.begin() + t);
					continue;
				}
				t++;
			}

			if(field.empty())
				break;

			int mValue = 10000;
			int mR = 0;
			int mC = 0;

			for(int j=0;j<field.size();j++)
			{
				for (int k=0;k<field[0].size();k++)
				{
					if (mValue > field[j][k])
					{
						mValue = field[j][k];
						mR = j;
						mC = k;
					}
				}
			}

			//int nR = 0;
			//int nC = 0;
			bool moweRow = true;
			bool moweColumn = true;

			for(int j=0;j<field[mR].size();j++)
			{
				if(field[mR][j] != mValue)
					moweRow = false;
			}

			for(int j=0;j<field.size();j++)
			{
				if(field[j][mC] != mValue)
					moweColumn = false;
			}

			if (moweColumn == false && moweRow == false)
			{
				cout << "Case #" << i+1 << ": NO" << endl;
				break;
			}

			if(moweColumn)
			{
				for(int j=0;j<field.size();j++)
					field[j].erase(field[j].begin()+mC);
				continue;
			}
			else if (moweRow)
			{
				field.erase(field.begin()+mR);
				continue;
			}
		}

		if(field.size() != 0)
			continue;
		cout << "Case #" << i+1 << ": YES" << endl;
	}

	return 0;
}