/* David Stenzel
 * Google Code Jam  2014*/
#include <iostream>

using namespace std;

void readInSet(int (&set)[4][4]);
void compRows(int (&row1)[4], int (&row2)[4]);

int main()
{
  int T, row1, row2;
  int set1[4][4];
  int set2[4][4];
  cin >> T;
  for (int i = 1; i <= T; ++i)
    {
      cin >> row1;
      readInSet(set1);
      cin >> row2;
      readInSet(set2);
      cout << "Case #" << i << ": ";
      compRows(set1[row1-1], set2[row2-1]);
    }
  return 0;
}

void readInSet(int (&set)[4][4])
{
  for (int b = 0; b < 4; ++b)
    {
      for (int a = 0; a < 4; ++a)
	{
	  cin >> set[b][a];
	}
    }
}

void compRows(int (&row1)[4], int (&row2)[4])
{
  int found = -1;
  bool badMagician = false;
  for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
	{
	  if (row1[i] == row2[j])
	    {
	      if (found == -1)
		{
		  found = row1[i];
		}
	      else
		{
		  badMagician = true;
		  break;
		}		  
	    }
	}
    }
  if (badMagician)
    {
      cout << "Bad magician!" << endl;
    }
  else if (found != -1)
    {
      cout << found << endl;
    }
  else
    {
      cout << "Volunteer cheated!" << endl;
    }
}
