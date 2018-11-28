#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int test_cases;
  int arr[4][4]={0};
  int row[2][4]={0};
  int elem_cnt = 0, ans_1,ans_2;
  ifstream readFile("A-small-attempt1.in");
  ofstream writeFile("output.in");
  readFile>> test_cases;
  int i,j,k;
  for(k=0; k<test_cases; k++)
  {
      readFile >> ans_1;
      for(i=0; i<4; i++)
      {
        for(j=0; j<4; j++)
        {
          readFile >> arr[i][j];
          if(i==ans_1-1)
          row[0][j] = arr[i][j];
        }
      }

      readFile >> ans_2;
      for(i=0; i<4; i++)
      {
        for(j=0; j<4; j++)
        {
          readFile >> arr[i][j];
          if(i==ans_2-1)
          row[1][j] = arr[i][j];
        }
      }

      // search in 2 rows
      int res = -1;
      elem_cnt = 0;
      for(i=0; i<4; i++)
      {
         int num = row[0][i];
         for(j=0 ;j<4; j++)
         {
           if(num == row[1][j])
           {
              res = num;
              elem_cnt++;
           }
         }
      }

      if(res != -1 && elem_cnt == 1)
      {
          writeFile <<"Case #"<< k+1 <<": "<< res<<endl;
      }
      else if(elem_cnt > 1)
      {
          writeFile <<"Case #"<< k+1 <<": "<<"Bad magician!"<<endl;
      }
      else
      {
          writeFile <<"Case #"<< k+1 <<": "<<"Volunteer cheated!"<<endl;
      }

  }

  readFile.close();
  writeFile.close();
  return 0;

}
