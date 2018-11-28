#include <iostream>
#include <cstdio>
#include <vector>
int min (int a, int b)
{
	if(a<b) return a;
	return b;
}

int main()
{
	int numOfCases, countCases, rowNum, colNum;
	int arr[100][100];
	int maxRow[100];
	int maxCol[100];
	int i,j;
	bool exists;
	std::vector<bool> output;

	scanf("%d", &numOfCases);
	countCases = 0;
	while(countCases < numOfCases){
		countCases++;
		exists = true;
		scanf("%d", &rowNum);
		scanf("%d", &colNum);

		for(i = 0; i < rowNum; i++){
			maxRow[i] = 1;
			for(j = 0; j < colNum; j++){
				scanf("%d", &arr[i][j]);
				if(arr[i][j] > maxRow[i])
					maxRow[i]= arr[i][j];
			}
		}
		for(j = 0; j < colNum; j++){
			maxCol[j] = 1;
			for(i = 0; i < rowNum; i++){
				if(maxCol[j] < arr[i][j])
					maxCol[j] = arr[i][j];
			}
		}

		for(i = 0; i < rowNum; i++){
			for(j = 0; j < colNum; j++){
				if(arr[i][j] != min(maxRow[i], maxCol[j])){
					exists = false;
					break;
				}

			}
		}
		output.push_back(exists);
	}
	for(size_t i = 0; i < output.size(); i++){
		if(output[i])
			std::cout << "Case #" << i+1 << ": YES\n";
		else
			std::cout << "Case #" << i+1 << ": NO\n";
	}
}

