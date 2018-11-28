#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void dorder(double *arr,int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = i+1; j < size; j++)
		{
			if (arr[j]>arr[i])
			{
				double temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}
void Iorder(double *arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = i + 1; j < size; j++)
		{
			if (arr[j]<arr[i])
			{
				double temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}
int findmax(double *arr,int size)
{
	double largest = arr[0];
	int index = 0;
	
	for (int i = 0; i < size; i++)
	{
		if (arr[i] > largest)
		{
			largest = arr[i];
			index = i;
		}
	}
	return index;
}


int main()
{
	int inc = 0;
	int count = 0,count1=0;
	int n = 0;
	int woods = 0;
	double *arr1,*arr2;
	
	fstream f("D-large.in", ios::in);
	fstream s("output.txt", ios::out);
	f >> n;
	
	

	for (int i = 0; i < n ; i++)
	{
		s << "Case #" << i + 1 << ": ";
		f >> woods;
		arr1 = new double[woods];
		arr2 = new double[woods];
		for (int j = 0; j < woods;j++)
		{
			f >> arr1[j];
		}
		for (int k = 0; k < woods; k++)
		{
			f >> arr2[k];
		}
		dorder(arr1, woods);
		dorder(arr2, woods);
		for (int q = 0; q < woods; q++)
		{
			
			for (int w = inc; w < woods; w++)
			{

				if (arr2[w] < arr1[q])
				{
					count++;
					inc++;
					break;

				}
				else
					inc++;
				
			}

		}
		inc = 0;

		s << count  << " ";
		count = 0;


		Iorder(arr2, woods);
		for (int z = 0; z < woods; z++)
		{
			int index = findmax(arr2, woods);
			if (arr2[index] > arr1[z])
			{
				arr2[index] = -0.1;
			}
			else
			{
				count1++;
			}

		}

		s << count1 << " ";
		
		count1 = 0;
		s << "\n";
	}
	s.close();
	f.close();
	return 0;
}