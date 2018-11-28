#include <fstream>
#include <iostream>
using namespace std;

int main()
{
  fstream in, out;
  in.open("A-small-attempt0.in.txt", fstream::in);
  out.open("out.txt", fstream::out);
  int num_cases, row1, row2, val;
  int outindex;
  int found = 0, foundmore = 0;
  int arr1[4][4];
  int arr2[4][4];
  in >> num_cases;
  for(int i = 0; i < num_cases; i++)
  {
    found = 0, foundmore = 0;
    in >> row1;
    row1--;
    cout << row1 << endl;
    for(int j = 0; j < 4; j++)
    {
      for(int k = 0; k < 4; k++)
        in >> arr1[j][k];
    }
    in >> row2;
    row2--;
    cout << row2 << endl;
    for(int j = 0; j < 4; j++)
    {
      for(int k = 0; k < 4; k++)
        in >> arr2[j][k];
    }
    for(int j = 0; j < 4; j++)
    {
      for(int k = 0; k < 4; k++)
      {
        if(arr1[row1][j] == arr2[row2][k])
        {
          if(found == 1)
            foundmore = 1;
          val = arr1[row1][j];
          found = 1;
        }
      }
      
    }
    outindex = i + 1;
      if(found == 0)
        out << "Case #" << outindex << ": " << "Volunteer cheated!" << endl;
      else if(foundmore == 1)
        out << "Case #" << outindex << ": " << "Bad magician!" << endl;
      else if(found == 1)
        out << "Case #" << outindex << ": " << val << endl;

  }

  return 0;

}
