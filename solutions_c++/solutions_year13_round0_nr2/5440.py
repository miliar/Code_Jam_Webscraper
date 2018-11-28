#include <stdio.h>
#include <vector>

bool CutHorizon(std::vector< std::vector<int> > &arr, int nRow, int nCol);
bool CutVertical(std::vector< std::vector<int> > &arr, int nRow, int nCol);

void main()
{
	FILE *fp = NULL;
	FILE *fwp = NULL;

	fp = fopen("B-Large.in", "r");
	fwp = fopen("output.in", "w");
	if( fp == NULL)
		return;
	
	int nCase = 0;
	fscanf(fp, "%d", &nCase);

	for(int i=0; i < nCase; i++)
	{
		std::vector< std::vector<int> > arr;
		std::vector< std::vector<bool> > arrCheck;
		
		int nRow = 0;
		int nCol = 0;
		fscanf(fp, "%d", &nRow);
		fscanf(fp, "%d", &nCol);

		int value = 0;
		int minValue = 1;
		int maxValue = 1;
		for(int j=0; j < nRow; j++)
		{
			std::vector<int> rowData;
			std::vector<bool> rowCheckData;
			for(int k=0; k < nCol; k++)
			{
				fscanf(fp, "%d", &value);

				if( minValue > value )
					minValue = value;

				if( maxValue < value )
					maxValue = value;

				rowData.push_back(value);
				rowCheckData.push_back(false);
			}
			arr.push_back(rowData);
			arrCheck.push_back(rowCheckData);
		}

		for(int j=0; j < arr.size(); j++)
		{
			for(int k=0; k < arr.at(j).size(); k++)
			{
				if( CutHorizon(arr, j, k) || CutVertical(arr, j, k))
					arrCheck.at(j).at(k) = true;
			}
		}

		bool isAvailable = true;
		for(int j=0; j < arrCheck.size(); j++)
		{
			for(int k=0; k < arrCheck.at(j).size(); k++)
			{
				if( arrCheck.at(j).at(k) == false )
				{
					isAvailable = false;
					break;
				}
			}
		}

		if(isAvailable)
			fprintf(fwp, "Case #%d: YES\n", i + 1);
		else
			fprintf(fwp, "Case #%d: NO\n", i + 1);
	}
}

bool CutHorizon(std::vector< std::vector<int> > &arr, int nRow, int nCol)
{
	for(int i=0; i < arr.at(nRow).size(); i++)
	{
		if( arr.at(nRow).at(i) > arr.at(nRow).at(nCol) )
			return false;
	}
	return true;
}

bool CutVertical(std::vector< std::vector<int> > &arr, int nRow, int nCol)
{
	for(int i=0; i < arr.size(); i++)
	{
		if( arr.at(i).at(nCol) > arr.at(nRow).at(nCol) )
			return false;
	}
	return true;
}