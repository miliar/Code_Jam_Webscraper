#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

int main(int argc, char *argv[]){

	int cases = 0;
	int sum = 0;
	string smax = "";
	int max = 0;
	int i = 0, j = 0;
	char num;
	int friends = 0;

	cin >> cases;
	cout << "cases: " << cases << endl;
	
	for(i = 0; i < cases; i++){
		sum = 0;
		friends = 0;
		cin >> smax;
		max = atoi(smax.c_str());

		int arr[max];
		for(j = 0; j < max + 1; j++){

			cin >> num;
			arr[j] = num - 48;		//convert char to int
		}

		sum += arr[0];
		if(sum == 0){
			sum++;
			friends++;
		}
		for(j = 1; j < max + 1; j++){
			sum += arr[j];

			if(j >= sum){
				sum++;
				friends++;
			}

		}

		cout << "Case #" << i+1 << ": " << friends << endl;
	}


	return 0;
}