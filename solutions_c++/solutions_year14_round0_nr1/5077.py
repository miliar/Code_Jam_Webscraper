#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
  int t = 0;;
  scanf("%d", &t);
  int c = 0;
  while (t--)
  {
        vector<int> row;
        int k = 0;
        int r1 = 0;
        int r2 = 0;
        scanf("%d", &r1);
        for (int i = 1; i < 5; i++)
            for (int j = 0; j < 4; j++) {
                scanf("%d", &k);
                if (i == r1)
                    row.push_back(k);
            }
       scanf("%d", &r2);
       k = 0;
       int cnt = 0;
       //vector<int> row1;
       int val = 0;
       for (int i = 1; i < 5; i++)
            for (int j = 0; j < 4; j++) {
                scanf("%d", &k);
                if (i == r2) {
                    for (int l = 0; l < 4; l++)
                       if (row[l] == k) {
                          cnt++;
                          val = k;
                       }

                }
            }
            c++;
      if (cnt == 0)
           cout << "Case #" << c << ": Volunteer cheated!" << endl;
      else if (cnt > 1)
           cout << "Case #" << c << ": Bad magician!" << endl;
      else if (cnt == 1)
            cout << "Case #" << c << ": " << val << endl;




  }

}
