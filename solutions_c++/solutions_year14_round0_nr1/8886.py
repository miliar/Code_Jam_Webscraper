#define A
#ifdef A

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void readCards(int cards[], int row)
{
   int temp;
   for ( int i = 0; i < 4; i++ )
      {
         if ( row == i )
            for ( int j = 0; j < 4; j++ )
               cin >> cards[j];
         else
            for ( int j = 0; j < 4; j++ )
               cin >> temp;
      }
}


int main() {
	int T, t = 0, row;
   cin >> T;
   int firstCards[4], secondCards[4];

	while ( t++ < T ) {
      cin >> row;
      row--;
      readCards(firstCards, row);
      sort(firstCards, firstCards+4);

      cin >> row;
      row--;
      readCards(secondCards, row);
      sort(secondCards, secondCards+4);

      vector<int> results(4);
      std::vector<int>::iterator it;

      it = set_intersection(firstCards, firstCards+4, secondCards, secondCards+4, results.begin());
      results.resize(it-results.begin());

      cout << "Case #" << t << ": ";
      if ( results.size() == 0 )
         cout << "Volunteer cheated!";
      else if ( results.size() > 1 )
          cout << "Bad magician!";
      else
         cout << results[0];
      cout << endl;
	}
	return 0;
}
#endif