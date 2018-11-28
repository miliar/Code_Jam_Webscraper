/* Code Jam 2014
@Author: Jugesh Sundram
*/

#include <iostream>
#include <conio.h>

using namespace std;

int main(){

  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A-small-attempt1.out", "w", stdout);
  
  int test_count;
  cin >> test_count;
  
  for (int test_index = 0; test_index < test_count; ++test_index) {

    int row, new_row, cards[4] = {0,0,0,0},new_cards[4] = {0,0,0,0}, dum;
	cin>>row;
  
	for (int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
		  (i == row-1) ? cin>>cards[j] : cin>>dum;
		   
    cin>>new_row;
    
    for (int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)

          (i == new_row-1) ? cin>>new_cards[j] : cin>>dum;
  
 
       
    int matches = 0 , result = 0;
    for (int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        if(cards[i] == new_cards[j])
          {result = cards[i]; matches++;}

    if(matches == 1)
      cout << "Case #" << test_index + 1 << ": "<<result<<endl;
    else if(matches >= 1)
      cout << "Case #" << test_index + 1 << ": Bad magician!"<<endl;
    else
      cout << "Case #" << test_index + 1 << ": Volunteer cheated!"<<endl;
      
	}
	

	return 0;
}
