#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
   unsigned int testCases;
   cin >> testCases;
   for( size_t i = 1; i <= testCases; ++i ) {
      unsigned int numberOfNumbers;
      cin >> numberOfNumbers;
      vector<unsigned int> numbers(numberOfNumbers);
      for( size_t j = 0; j < numberOfNumbers; ++j ) {
	 unsigned int temp;
	 cin >> temp;
	 numbers.at(j) = temp;
      }

      //Main Logic method 1
      unsigned int total1 = 0;
      unsigned int total2 = 0;
      unsigned int current = numbers.at(0);
      for( size_t j = 1; j < numberOfNumbers; ++j ) {
	 unsigned int next = numbers.at(j);
	 if(next < current)
	    total1 += current - next;
	 current = next;
      }
      unsigned int biggestDifference = 0;
      for( size_t j = 0; j < numberOfNumbers - 1; ++j ) {
	 if (numbers.at(j) > numbers.at(j+1)) {
	    if ((numbers.at(j) - numbers.at(j+1)) > biggestDifference) {
	       unsigned int difference = numbers.at(j) - numbers.at(j+1);
	       biggestDifference = difference;
	    }
	 }
      }
      total2 = biggestDifference * (numberOfNumbers-1);
      for( size_t j = 0; j < numberOfNumbers-1; ++j ) {
	 if( numbers.at(j) < biggestDifference ) {
	    total2 -= (biggestDifference - numbers.at(j));
	    //cout << total2 << ' ' << biggestDifference << endl;

	 }
      }

      cout << "Case #" << i << ": " << total1 << ' ' << total2  << endl;
   }
   return 0;
}
