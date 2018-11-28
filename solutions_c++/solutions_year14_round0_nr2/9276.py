#include <iostream>

// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>     /* atoi */
#include <sstream>      /*  iss   */

using namespace std;

int main()
{
  string line;
      int testNum;
      double set[3][100];
    //cout << "Hello world!" << endl;
    ifstream myfile ("B-small-attempt0.in");
    if (myfile.is_open())
  {
      getline (myfile,line);
      testNum = atoi(line.c_str());
      //cout<<testNum<<'\n';

      for (int lineNum=0; getline (myfile,line) && lineNum<(testNum); lineNum++)
      {
        istringstream iss(line);
        int column=0;
        while (column<3)
            {
            string sub;
            iss >> sub;
            set[column][lineNum] = atof(sub.c_str());
            //cout << "Substring: " << set[column][lineNum] << endl;
            column++;
            }

         // cout << line << '\n';
      }



  myfile.close();
  }
  else cout << "Unable to open file";


ofstream myOut ("output.txt");
        if (myOut.is_open())
        {

  for(int i=0;i<testNum;i++)
  {


  double direct;
  double trick;
  double aim = set[2][i];
  double wage=2;
  double addWage = set[1][i];
  double farm = set[0][i];

  direct = aim/wage;
  trick = farm/wage;
  wage=wage+addWage;
  trick += aim/wage;

    if(direct<trick)
    {
//        cout.precision(15);
//        cout << "Result"<< direct<<endl;
        myOut.precision(15);
        myOut<< "Case #" << i+1 <<": "<<direct<<endl;
        continue;
    }

  while(1){

  direct=trick;

  trick=trick-aim/wage;

  trick += farm/wage;
  wage=wage+addWage;

  trick += aim/wage;

    if(direct<trick)
    {
        //myOut << "Result"<< direct<<endl;
//        cout.precision(15);
//        cout << "Result"<< direct<<endl;
        myOut.precision(15);
        myOut<< "Case #" << i+1 <<": "<<direct<<endl;
        break;
    }
    //direct=trick;

  }


  }

  myOut.close();
}else cout << "Unable to open file";



    return 0;
}
