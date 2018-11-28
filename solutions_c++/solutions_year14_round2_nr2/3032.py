#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int A, B, K;
	for(int t = 0;t < T; t ++){
		cin >> A >> B >> K;
		//cout << A <<  " " << B <<  " " << K << endl;
		int MAX = A&B;
		//cout << "max: " << MAX <<endl; 
		vector<int> winningNumbers;
		int newNum;
		int sizeOfWinningSet =-1;
		int NumberOfPairs =0;
		for(int i = 0 ; i < A; i++){
			for(int j = 0; j < B; j++){
				bool unique = true;
				newNum = i&j;

				for(int x = 0; x < winningNumbers.size(); x++){
					if(winningNumbers[x] == newNum){
						unique = false;

						 break;
					}
				}
				
				if(unique && newNum < K){
					
						NumberOfPairs ++;
					
					
				}
			}
			
		}
		cout << "Case #" << t+1<< ": " << NumberOfPairs << endl;
		/*if(sizeOfWinningSet == -1){
			sizeOfWinningSet = winningNumbers.size();
		}
		cout << endl;
		int SWN = winningNumbers.size();
		cout << "Answer: " << SWN*sizeOfWinningSet* 2 - ((K<SWN)?K:SWN)<<endl;

*/

		
	} 

	return 0;
}