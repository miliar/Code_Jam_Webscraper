//============================================================================
// Name        : roundOneCFirst.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void findFirstAndSecondMax(int *rowData, int N, int &first, int & second)
{
	first = 0;
	second = 0;

	for(int i = 0; i < N; i++){
		if(rowData[i] > rowData[first]){
			first = i;
		}
	}

	for(int i = 0; i < N; i++){
		if(rowData[i] >= rowData[second] && rowData[i] <= rowData[first] && i != first){
			second = i;
		}
	}

}

void processEachCase(int *rowData, int N, int c_id, int total)
{
	cout<< "Case #" << (c_id + 1) <<":";
	while(total > 0){
		int first = 0, second = 0;
		findFirstAndSecondMax(rowData, N, first, second);
		if(total == 3){
			//delete one first.
			rowData[first]--;
			total = total - 1;

			char firstChar = 'A' + first;
			cout<< " "<<firstChar;
		}
		if(total == 1){
			cout<<"=======error======"<<endl;
		}

		if(rowData[first] - rowData[second] >= 2){
			//delete two first.
			rowData[first]--;
			rowData[first]--;
			total = total -2;

			char firstChar = 'A' + first;
			cout<< " "<< firstChar<< firstChar;
//			if(total > 0){
//				cout<<" ";
//			}

		}
		else if(rowData[first] - rowData[second] == 1 || rowData[first] - rowData[second] == 0){
			//delete one first and one second
			rowData[first]--;
			rowData[second]--;
			total = total -2;

			char firstChar = 'A' + first;
			char secondChar = 'A' + second;
			cout<<" " <<firstChar<< secondChar;
//			if(total > 0){
//				cout<<" ";
//			}
		}
	}

	cout<<endl;
}

int main() {
	int T = 0;//TEST cases
	int N = 0;
	int *rowData = NULL;

	cin>>T;
	for(int i = 0; i < T; i++){
		cin >> N;
		rowData = new int[N];
		int total = 0;
		for(int j = 0; j < N; j++){
			cin>>rowData[j];
			total += rowData[j];
		}
		processEachCase(rowData, N, i, total);

		delete [] rowData;
	}


	return 0;
}
