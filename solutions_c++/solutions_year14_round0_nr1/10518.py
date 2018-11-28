#include <iostream>

using namespace std;

int TestCase, ChooseOne, ChooseTwo, StartIndexOne, StartIndexTwo;
int ArrOne[16], ArrTwo[16], Answer;
int TestCount;

int main()
{
	int count = 0, i, j, ii, jj, temp;
	cin >> TestCase;
	while(TestCase--){
		cin >> ChooseOne;
		for(i = 0; i < 16; i++){
			cin >> ArrOne[i];
		}
		cin >> ChooseTwo;
		for(j = 0; j < 16; j++){
			cin >> ArrTwo[j];
		}
		// One -  Row
		if(ChooseOne == 1)
			StartIndexOne = 0;
		else if(ChooseOne == 2)
			StartIndexOne = 4;
		else if(ChooseOne == 3)
			StartIndexOne = 8;
		else
			StartIndexOne = 12;

		// Two - Row
		if(ChooseTwo == 1)
                        StartIndexTwo = 0;
                else if(ChooseTwo == 2)
                        StartIndexTwo = 4;
                else if(ChooseTwo == 3)
                        StartIndexTwo = 8;
                else
                        StartIndexTwo = 12;
		temp = StartIndexTwo;
		for(ii = 0, StartIndexOne; ii < 4; ii++, StartIndexOne++){
			for(jj = 0, StartIndexTwo; jj < 4; jj++, StartIndexTwo++){
				if(ArrOne[StartIndexOne] == ArrTwo[StartIndexTwo]){
					count++;
					Answer = ArrOne[StartIndexOne];
				}
			}
			StartIndexTwo = temp;
		}
		if(count == 0)
			cout << "Case #" << ++TestCount << ": " << "Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << ++TestCount << ": " << Answer << endl;
		else
			cout << "Case #" << ++TestCount << ": " << "Bad magician!" << endl;
		
		count = 0;
	}
	return 0;
}
