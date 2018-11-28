#include <iostream>
using namespace std;
int main(){
     int N = 0;
     cin >> N;
     int n = 0;
while(N-->0){
   n++;
   int selectedNums[8] = {0};
	int k = 0;
     for(int j = 0 ; j < 2; j++) {
	int cards[4][4] = {0};
        int num = 0;
	int lineNum = 0;
	cin >> lineNum;
	lineNum = lineNum - 1;
	int nums = 16;
	for(int i = 0 ; i < 4;i++) {
	  for(int j = 0 ; j < 4; j++) {
	    cin >> cards[i][j];
          }
	}
	for(int i = 0; i < 4;i++) {
	  selectedNums[k++] = cards[lineNum][i];
	}
      }
	int sameCard = 0;
	int same = 0;
	for(int i = 0 ; i < 4;i++) {
	  for(int j = 3 ; j < 8;j++) {
	    if(selectedNums[i] == selectedNums[j] && i!=j) {
		   same = selectedNums[i];
		   sameCard++;
             }
 	  }
        }
	cout << "Case #" << n << ": ";
	if(sameCard == 0)
	  cout << "Volunteer cheated!";
	if(sameCard == 1)
	  cout << same;
	if(sameCard > 1)
	  cout << "Bad magician!";
	cout << "\n";
}
	return 0; 
}
