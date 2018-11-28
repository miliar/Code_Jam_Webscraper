#include <iostream>
#include <algorithm>
#include <string>

/* PRIMA DONNA:

The problem essentially boils down to reading in a string
and converting it to an array. Going through the array, if
the sum of the number of people previously seen is less than
the index, we need to add more external people. Then we can
add those people liberated to applause to the sum.

A Greedy strategy works because a person will not applause until
enough people applause to match shyness, so more people must be added
to make them applaud. */

using namespace std;

int main(void){



  //Read in the number of cases, and for each case:
  int cases;
  cin >> cases;
  for(int c = 1; c <= cases; c++){
    int maxShy;
    cin >> maxShy;
    maxShy++;

    string shyString;
    cin >> shyString;

    int friends = 0;
    int applaudingCount = 0;
    int shynessCount = 0;
    //record how many people of each shyness level
    for(int i = 0; i < maxShy; i++){

      shynessCount = shyString[i]-'0';

      //If there are not enough people applauding, add friends to applaud
      if(applaudingCount < i){
        friends += i - applaudingCount;
        applaudingCount = i;
      }
      applaudingCount += shynessCount;
    }

    cout << "Case #" << c << ": " << friends << endl;

  }
}
