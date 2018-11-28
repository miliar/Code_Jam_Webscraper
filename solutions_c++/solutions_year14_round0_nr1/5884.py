#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isInVector(vector<int> vec, int a)
{
	if(vec.empty())
		return false;
	
	for(int i=0;i<vec.size();i++)
	{
		if(vec[i] == a)
			return true;
	}
	
	return false;
}

int main()
{
	int T;
	int M,N;
	int s;
	int temp;
	int result;
	bool result1;
	bool result2;
	vector<int> row1;
	vector<int> row2;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		result1 = false;
		result2 = false;
		cin >> M;
		if(M == 1)
		{
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row1.push_back(s);
			}
			for(int j=0;j<12;j++)
				cin >> temp;
		}
		else if(M == 2)
		{
			for(int j=0;j<4;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row1.push_back(s);
			}
			for(int j=0;j<8;j++)
				cin >> temp;
		}
		else if(M == 3)
		{
			for(int j=0;j<8;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row1.push_back(s);
			}
			for(int j=0;j<4;j++)
				cin >> temp;
		}
		else if(M == 4)
		{
			for(int j=0;j<12;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row1.push_back(s);
			}
		}
		cin >> N;
		if(N == 1)
		{
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row2.push_back(s);
			}
			for(int j=0;j<12;j++)
				cin >> temp;
		}
		else if(N == 2)
		{
			for(int j=0;j<4;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row2.push_back(s);
			}
			for(int j=0;j<8;j++)
				cin >> temp;
		}
		else if(N == 3)
		{
			for(int j=0;j<8;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row2.push_back(s);
			}
			for(int j=0;j<4;j++)
				cin >> temp;
		}
		else if(N == 4)
		{
			for(int j=0;j<12;j++)
				cin >> temp;
			for(int j=0;j<4;j++)
			{
				cin >> s;
				row2.push_back(s);
			}
		}
		for(int k=0; k<4;k++)
		{
			if(isInVector(row1, row2[k]))
			{
				result = row2[k];
				if(result1)
				{
					result2 = true;
				}
				result1 = true;
			}
		}
		if(!result1 && !result2)
			cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		else if(result1 && !result2)
			cout << "Case #" << i+1 << ": " << result << endl;
		else if(result1 && result2)
			cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		row1.clear();
		row2.clear();
	}

	return 0;
}
