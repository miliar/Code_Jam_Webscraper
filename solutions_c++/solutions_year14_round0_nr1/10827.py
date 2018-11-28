/*
get all the numbers in the selected row from the first trial
if only one overlap then that number
if more than one overlap shitty magician
if none overlap then cheated

*/

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <iterator>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

bool exists(vector<int> first, int value){
	vector<int>::iterator val = find(first.begin(), first.end(), value);
	if (val == first.end()) return false;
	else return true;
}
int main() {
	freopen("a0.in", "r", stdin);
    freopen("a0.out", "w", stdout);

    int t;
    cin >> t;
    //for each test case
    for (int i = 1; i <= t; ++i)
    {
    	// read the first set
	   	int row, col;
	   	int values;
		vector <int> first;
		cin >> row;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> values;
				if(j + 1 == row) first.push_back(values);
			}
		
		}

		//read the second set
		cin >> col;

		int count = 0, tmp;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> values;
				if (j + 1 == col){
					if(exists(first, values)){ 
						count++;
						tmp = values;
					}
				}	
			}
		
		}		
		if(count == 0){
			printf("Case #%d: Volunteer cheated!", i);
		}
		else if(count == 1) {
			printf("Case #%d: %d", i, tmp);
			}
		else {
			printf("Case #%d: Bad magician!", i);
		}

		printf("\n");
    }
    
}