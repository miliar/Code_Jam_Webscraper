#include<iostream>
#include<fstream>
using namespace std;

int Maximum_Value_Index(float* arr, int length)
{
	int index = 0;
	float value = arr[0];
	for (int j = 1; j < length; j++)
	{
		if (arr[j]>value)
		{
			value = arr[j];
			index = j;
		}
	}
	return index;
}

int Minimum_Value_Index(float* arr,int length)
{
	int min_index = 0;
	float minimum = arr[0];
	
	for (int j=1; j < length; j++)
	{
		if (arr[j] < minimum)
		{
			minimum = arr[j];
			min_index = j;
		}
	}
	return min_index;
}

int Greater_Than_Parameter_Index(float* arr,int length,float param)
{
	int max_index = -1;
	float maximum;
	bool check = false;
	for (int j = 0; j < length; j++)
	{
		if (!check)
		{
			if (arr[j]>param)
			{
				check = true;
				maximum = arr[j];
				max_index = j;
			}
			continue;
		}
		if (arr[j] > param && arr[j] < maximum)
		{
			maximum = arr[j];
			max_index = j;
		}
	}
	return max_index;
}

int main()
{
	int count,length,length1,temp,i,j;
	float *Naomi, *Ken,*arr1,*arr2,call,swap;
	int War = 0, D_War = 0;
	int Ken_Chosen;

	ifstream fin("D-large.in");
	ofstream fout("output_D_Large.txt");
	
	fin >> count;
	for (i = 0; i < count; i++)
	{
		fin >> length;
		Naomi = new float[length];
		Ken = new float[length];
		arr1 = new float[length];
		arr2 = new float[length];

		for (j = 0; j < length; j++)
		{
			fin >> Naomi[j];
			arr1[j] = Naomi[j];
		}
		for (j = 0; j < length; j++)
		{
			fin >> Ken[j];
			arr2[j] = Ken[j];
		}
		length1 = length;

		for (j = 0; j < length; j++)
		{
			Ken_Chosen = Maximum_Value_Index(arr2, length1);
			temp = Greater_Than_Parameter_Index(arr1, length1,arr2[Ken_Chosen]);
			if (temp>-1)
			{
				Ken_Chosen = Minimum_Value_Index(arr2, length1);
				temp = Greater_Than_Parameter_Index(arr1, length1, arr2[Ken_Chosen]);
				++D_War;
			}
			else
			{
				temp = Maximum_Value_Index(arr1, length1);
				Ken_Chosen = Greater_Than_Parameter_Index(arr2, length1, arr1[temp]);
				temp = Minimum_Value_Index(arr1, length1);
			}
			
			swap = arr1[temp];
			arr1[temp] = arr1[length1 - 1];
			arr1[length1 - 1] = swap;
			swap = arr2[Ken_Chosen];
			arr2[Ken_Chosen] = arr2[length1 - 1];
			arr2[length1 - 1] = swap;
			--length1;
		}

		length1 = length;
		for (j = 0; j < length; j++)
		{
			call = Naomi[j];
			temp = Greater_Than_Parameter_Index(Ken, length1, call);
			if (temp < 0)
			{
				temp = Minimum_Value_Index(Ken, length1);
				++War;
			}

			--length1;
			swap = Ken[temp];
			Ken[temp] = Ken[length1];
			Ken[length1] = swap;
		}

		fout << "Case #" << i + 1 << ": " << D_War << " " << War << endl;;
		War = 0;
		D_War = 0;
		delete[]Naomi;
		delete[]Ken;
		delete[]arr1;
		delete[]arr2;
	}
	
	return 0;
}