#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
  ifstream myInput;
  myInput.open("A-small-attempt0.in");
  ofstream myOutput;
  myOutput.open("solution.out");

  int t;
  myInput >> t;
  for(int i = 0; i < t; i++)
  {
    int n;
    myInput >> n;

    int array[n];

    for(int j = 0; j < n; j++)
      myInput >> array[j];

    int cont = 1;

    myOutput << "Case #" << i + 1 << ": ";

    while(cont){
        cont = 0;
        int max[2] = {0, 0};

        for(int j = 0; j < n; j++)
        {
          if(array[j] > array[max[0]])
            max[0] = j;
          else if(array[j] >= array[max[1]]){
            if(max[0] != max[1] && max[1] != 0)
              cont++;
            max[1] = j;
          }
          else if(array[j])
            cont++;
        }

        if(array[max[0]] - array[max[1]] > 1)
          max[1] = max[0];

        char c1 = max[0] + 65;
        char c2 = max[1] + 65;

        if(cont == 1 && array[max[0]] == 1){
          myOutput << c1 << ' ';
          array[max[0]]--;
        }
        else if(cont == 0 && array[max[0]] > array[max[1]]){
          myOutput << c1 << ' ';
          array[max[0]]--;
        }
        else{
          myOutput << c1 << c2 << " ";
          array[max[0]]--;
          array[max[1]]--;
        }

        if(array[max[0]] > 0)
          cont = 1;
    }
    myOutput << endl;
  }
}
