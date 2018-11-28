#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef vector< vector<int> > matrix;

int findMax(matrix& iMat, const int colIdx, const int rowIdx) 
{
	int currMax = 0;
	if (colIdx >=0)
	{
		// col max
		for (int i=0; i<iMat.size(); ++i)
		{
			if (iMat[i][colIdx] > currMax)
			{
				currMax = iMat[i][colIdx];
			}
		}
	}
	else if (rowIdx >=0)
	{
		// row max
		for (int i=0;i<iMat[rowIdx].size();++i)
		{
			if (iMat[rowIdx][i] > currMax)
			{
				currMax = iMat[rowIdx][i];
			}
		}
	}
	return currMax;
}



int main()
{
	int numTests;
	cin >> numTests;
	cin.ignore(); // flush input stream

	for (int i=0; i<numTests; ++i)
	{
		int N, M;
		cin >> N;
		cin >> M;
		cin.ignore();
		const int Mc = M, Nc = N;
		matrix lawn;
		bool output[Nc][Mc];
		int tmp;
		for (int n=0;n<N;++n)
		{
			vector<int> newRow;
			for (int m=0;m<M;++m)
			{
				cin >> tmp;
				newRow.push_back(tmp);
			}
			lawn.push_back(newRow);
			cin.ignore();
		}

		// check rows
		for (int n=0;n<N;++n)
		{

			int rowMax = findMax(lawn,-1,n);
			for (int m=0;m<M;++m)
			{
				
				if (lawn[n][m] < rowMax)
				{
					output[n][m]=0;
				}
				else
				{
					output[n][m]=1;
				}

			}
		}


		// check columns
		for (int m=0;m<M;++m)
		{

			int colMax = findMax(lawn,m,-1);
			for (int n=0;n<N;++n)
			{
				
				if (lawn[n][m] < colMax)
				{
					output[n][m]= 0 | output[n][m];
				}
				else
				{
					output[n][m]= 1;
				}
	
			}
		}

		// cycle through output to see if there are any zeros
		bool success = true;
		for (int n=0;n<N && success ;++n)
		{
			for (int m=0;m<M;++m)
			{
				if (!output[n][m])
				{
					success = false;
					break;
				}
			}
		}

		string result = "NO";
		if (success)
		{
			result = "YES";
		}
		cout << "Case #" << i+1 << ": " <<  result << endl;


	}

}