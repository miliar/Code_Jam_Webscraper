#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
  ifstream f("A-small-attempt0.in");
  ofstream of("A-small-attempt0.out");
  
  int test_cases = 0;
  f >> test_cases;

  int r1;
  int r2;
  int item;
  for(int tc=0; tc<test_cases; tc++)
  {
    vector<int> possibilities;

    f >> r1;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
      {
        f >> item;
        if (i+1==r1) possibilities.push_back(item);
      }

    f >> r2;
    int solCount = 0;
    int solution = -1;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
      {
        f >> item;
        if (i+1==r2)
        {
          for(int k=0; k<4; k++)
            if (possibilities[k]==item)
            {
              solCount++;
              solution=item;
            }
        }
      }

    of << "Case #" << tc+1 << ": ";
    if (solCount == 0)  of << "Volunteer cheated!";
    else if (solCount == 1) of << solution;
    else of << "Bad magician!";
    of << endl;
  }

  f.close();
  of.close();
}
