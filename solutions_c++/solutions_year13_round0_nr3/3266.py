#include <iostream> 
#include <fstream>
#include <math.h>
using namespace std;
bool judge(int k)
{
	int temp = k;
	int t = 0;
	while (temp >0)
	{
		t = (t*10)+temp %10;
		temp /= 10;
	}
	if (t == k) return true;
	return false;
}
int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	int A, B;
	int min, max;
	fin >> t;
	for (int i=0; i<t; i++) 
	{
		fin >> A >> B;
		fout << "Case #" << i+1;
		fout << ": ";
		int num = 0;
		min = (int)sqrt(A)-1;
		max = (int)sqrt(B)+1;
	//	cout << min << " " << max << endl; 
		for (int j= min; j<=max; j++)
		{
			if (judge(j)) 
			{
				int temp = j*j;
				if ((temp >= A)&&(temp <= B))
				{
					if (judge(temp))	num ++;
				}
			}
		}
		fout << num << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
