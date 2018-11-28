#include<stdio.h>
#include<iostream>
 
using namespace std;
int main(){
	int T = 0;
	cin >> T;
	int nFr;
	int curCnt;
	int Smax;
	char *arr = NULL;

	for(int i=0; i<T; i++){
		 arr = NULL;
		 nFr = 0;
		 curCnt = 0;
		 Smax = 0;

		cin >> Smax;

		arr = (char *)calloc(Smax+2, sizeof(char));
		cin >> arr;
		for(int j =0; j<=Smax; j++){

			if(curCnt < j && ((arr[j] - '0')>0)){
				nFr += j - curCnt;
				curCnt = j;
			}

			curCnt += arr[j] - '0';

		}
		free(arr);
		cout << "Case #" << i+1 << ": " << nFr <<endl;
	}

	return 0;
}