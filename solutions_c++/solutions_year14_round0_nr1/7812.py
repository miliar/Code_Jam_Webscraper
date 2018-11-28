#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;

int intersection(vector<int>&, vector<int>&, vector<int>&);


int main()
{
	
	ifstream fin("A-small-attempt0.in");
	ofstream fout("res.txt");
	int t;
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		
		fout << "Case #" << i << ": ";
		int first, second;
		fin >> first;
		vector<int> arr1(4);
		vector<int> arr2(4);
		int temp;
		for (int j = 1; j < first; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				fin >> temp;
			}
		}
		for (int j = 0; j < 4; j++)
		{
			fin >> arr1[j];
		}
		for (int j = first; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				fin >> temp;
			}
		}
		fin >> second;
		for (int j = 1; j < second; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				fin >> temp;
			}
		}
		for (int j = 0; j < 4; j++)
		{
			fin >> arr2[j];
		}
		for (int j = second; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				fin >> temp;
			}
		}
		sort(arr1.begin(), arr1.end());
		sort(arr2.begin(), arr2.end());
		vector<int> v(4);
		temp = intersection(arr1, arr2, v);
		if (temp == 1)
		{
			fout << v[0];
		}
		else if (temp < 1)
		{
			fout << "Volunteer cheated!";
		}
		else
		{
			fout << "Bad magician!";
		}
		fout << endl;

	}
	fin.close();
	fout.close();
	
	return 0;
}


int intersection(vector<int>& a, vector<int>& b, vector<int>& c)
{
	int i, j;
	int count = 0;
	for (i = 0, j = 0; i < a.size() && j < b.size();)
	{
		if (a[i] == b[j])
		{
			c[count] = a[i];
			count++;
			if (count > 1)
			{
				break;
			}
			i++;
			j++;
		}
		else if (a[i] < b[j])
		{
			i++;
		}
		else
		{
			j++;
		}
	}
	return count;
}