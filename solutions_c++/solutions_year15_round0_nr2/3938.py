#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int getMinutes(vector<int> plates);
int main(int argc, char* argv[])
{
	ifstream inFile;
	if (argc > 0)
		inFile.open(argv[1]);
	else
		inFile.open("in.in");
	ofstream outFile("out.txt");

	int cases;
	inFile >> cases;
	for (int c = 1; c <= cases; ++c)
	{
		cout << "case: " << c << endl;
		int D;
		inFile >> D;
		vector<int> plates;
		int size = D;
		for (int i = 0; i < size; ++i)
		{
			int val;
			inFile >> val;
			plates.push_back(val);
		}
		int ans = getMinutes(plates);
		cout << "ans: " << ans << endl;
		outFile << "Case #" << c << ": " << ans << endl;
		//system("pause");
	}
	inFile.close();
	outFile.close();
}

void splitPlate(int arr[2], int plate, bool half)
{
	if (plate == 1)
	{
		arr[0] = 1;
		arr[1] = 0;
	}
	else if(plate == 2)
	{
		arr[0] = 1;
		arr[1] = 1;
	}
	else if (plate == 3)
	{
		arr[0] = 2;
		arr[1] = 1;
	}
	else if (half)
	{
		arr[0] = plate / 2;
		arr[1] = plate - arr[0];
	}
	else
	{
		arr[0] = plate / 2 - 1;
		arr[1] = plate - arr[0];
	}
}

int getMinutes(vector<int> plates)
{
	
	if (plates.size() == 0)
		return 0;
	sort(plates.begin(), plates.end());
	for (int i = 0; i < plates.size(); ++i)
	{
		if (plates[i] == 0)
		{
			plates.erase(plates.begin() + i);
			--i;
		}
		else
			break;
	}
	
	if (plates[plates.size() - 1] == 1)
		return 1;
	if (plates[plates.size() - 1] == 2)
		return 2;
	if (plates[plates.size() - 1] == 3)
		return 3;
	vector<int> testplates;
	for (int i = 0; i < plates.size(); ++i)
		testplates.push_back(plates[i]);
	for (int i = 0; i < testplates.size(); ++i)
	{
		testplates[i] -= 1;
		if (testplates[i] == 0)
		{
			testplates.erase(testplates.begin() + i);
			--i;
		}
	}
	vector<int> solutions;
	solutions.push_back(1 + getMinutes(testplates)); //one solution is to have a regular minute

	//find the number and how much
	int largest;
	int amtLargest;
	int leastLargestIndex;
	for (int i = plates.size() - 1; i >= 0; --i)
	{
		if (i - 1 == -1 || plates[i - 1] != plates[i])
		{
			largest = plates[i];
			leastLargestIndex = i;
			amtLargest = plates.size() - i;
			break;
		}
	}
	if (amtLargest >= 4 && largest == 9)
		return 9;
	if (amtLargest >= 4 && largest == 8)
		return 8;
	if (largest > 2)
	{
		plates.erase(plates.begin() + leastLargestIndex);
		int arr1[2];
		int arr2[2];
		splitPlate(arr1,largest, true);
		splitPlate(arr2,largest, false);
		plates.push_back(arr1[0]);
		plates.push_back(arr1[1]);
		solutions.push_back(1 + getMinutes(plates));
		if (!(arr2[0] == arr1[0] && arr2[1] == arr1[1]))
		{
			plates[plates.size() - 2] = arr2[0];
			plates[plates.size() - 1] = arr2[1];
			solutions.push_back(1 + getMinutes(plates));
		}
	}
	
	sort(solutions.begin(), solutions.end());
	return solutions[0];
}
/*
int getMinutes(vector<int> plates)
{
	for (int i = 0; i < plates.size(); ++i)
	cout << plates[i] << " ";
	cout << endl;
	sort(plates.begin(), plates.end());
	
	if (plates[0] != plates[plates.size() - 1]) // there is a number larger than the first
	{
		//find the number and how much
		int largest;
		int amtLargest;
		int nextLargest;
		int leastLargestIndex;
		for (int i = plates.size() - 1; i >= 0; --i)
		{
			if (plates[i - 1] != plates[i])
			{
				largest = plates[i];
				leastLargestIndex = i;
				nextLargest = plates[i - 1];
				amtLargest = plates.size() - i;
				break;
			}
		}
		int sol0 = -1;
		vector<int> testplates;
		for (int i = 0; i < plates.size(); ++i)
			testplates.push_back(plates[i]);
		for (int i = 0; i < testplates.size(); ++i)
			{
			testplates[i] -= 1;
			if (testplates[i] == 0)
				{
				testplates.erase(testplates.begin() + i);
					--i;
				}
			}
		sol0 = 1 + getMinutes(testplates);

		//figure out if it is feasible to split and what to split into
		int half1, half2;
		int arr[2];
		splitPlate(arr,largest, false);
		half1 = arr[0];
		half2 = arr[1];
			int oldSize = plates.size();
			plates.erase(plates.begin()+plates.size() - 1);
			int point;
			for (int i = 0; i < plates.size(); ++i)
			{
				if (plates[i] >= half1 || i == plates.size()-1)
				{
					plates.insert(plates.begin()+i,half1);
					point = i-1;
					break;
				}
			}
			for (int i = point; i < plates.size(); ++i || i == plates.size() - 1)
			{
				if (plates[i] >= half2)
				{
					plates.insert(plates.begin() + i, half2);
					break;
				}
			}
			int sol1 = 1 + getMinutes(plates);
			int sol2 = largest;
			int smallest = (sol1 < sol2) ? sol1 : sol2;
			if (sol0 != -1)
				smallest = (smallest < sol0) ? smallest : sol0;
			return smallest;
	}
	else
	{
		int sol0 = -1;
		if (plates.size() + plates[0] / 2 < plates[0])
		{
			vector<int> testplates;
			for (int i = 0; i < plates.size(); ++i)
				testplates.push_back(plates[i]);
			int half1, half2;
			half1 = testplates[0] / 2;
			if (testplates[0] % 2 == 0)
				half2 = half1;
			else
				half2 = half1 + 1;
			int oldsize = testplates.size();
			for (int i = 0; i < oldsize; ++i)
				testplates[i] = half1;
			for (int i = 0; i < oldsize; ++i)
				testplates.push_back(half2);
			sol0 = testplates.size() / 2 + getMinutes(testplates);
		}
		int sol1 = plates[0];
		int smallest = sol1;
		if (sol0 != -1)
			smallest = (smallest < sol0) ? smallest : sol0;
		return smallest;
	}
}*/
