#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main()
{
    ofstream output;
    string line,result;
    int input_data[4][4];
    const char* input_line;
    int number_test,sum;
    bool not_completed;
    output.open ("output.txt");
    fstream input("input.txt");
     if (output.is_open())
     {
    if (input.is_open())
    {
     if( input.good() )
      {
        getline (input,line);
        number_test=atoi(line.c_str());
        for(int i=1;i<=number_test;i++)
        {
            not_completed=false;
            result="-1";
            if(input.good())
            {
                if(i>1)
                 getline(input,line);
                for(int row=0;row<4;row++)
                {
                getline(input,line);
                input_line=line.c_str();
                for(int j=0;j<line.length();j++)
                {
                    switch(input_line[j])
                    {
                    case 'X':
                        input_data[row][j]=2;
                        break;
                    case 'O':
                        input_data[row][j]=-3;
                        break;
                    case '.':
                         input_data[row][j]=-1000;not_completed=true;
                        break;

                    default:
                        input_data[row][j]=5;
                        break;
                    }
                }
                }
                for(int z=0;z<4;z++)
                {
                    sum=input_data[z][0]*input_data[z][1]*input_data[z][2]*input_data[z][3];
                  if(sum==16 || sum==40 ||sum==81|| sum==-135)
                    {
                        switch(sum)
                   {
                        case 16:result="X won";break;
                        case 40:result="X won";break;
                        case 81:result="O won";break;
                        case -135:result="O won";break;
                   }
                        break;
                    }
                  sum=input_data[0][z]*input_data[1][z]*input_data[2][z]*input_data[3][z];
                  if(sum==16 || sum==40 ||sum==81|| sum==-135)
                    {
                        switch(sum)
                   {
                        case 16:result="X won";break;
                        case 40:result="X won";break;
                        case 81:result="O won";break;
                        case -135:result="O won";break;
                   }
                        break;
                    }
                }
                if(result=="-1")
                {
                sum=input_data[0][0]*input_data[1][1]*input_data[2][2]*input_data[3][3];
                if(sum==16 || sum==40 ||sum==81|| sum==-135)
                  {
                      switch(sum)
                 {
                      case 16:result="X won";break;
                      case 40:result="X won";break;
                      case 81:result="O won";break;
                      case -135:result="O won";break;
                 }
                  }
                sum=input_data[0][3]*input_data[1][2]*input_data[2][1]*input_data[3][0];
                if(sum==16 || sum==40 ||sum==81|| sum==-135)
                  {
                      switch(sum)
                 {
                      case 16:result="X won";break;
                      case 40:result="X won";break;
                      case 81:result="O won";break;
                      case -135:result="O won";break;
                 }
                  }
                 if(!not_completed && result=="-1")
                    result="Draw";
                else if(result=="-1" && not_completed)
                    result="Game has not completed";
                }
                output<<"Case #"<<i<<": "<<result<<endl;
            }
        }
      }
     output.close();
      input.close();
    }
    else cout << "Unable to open input.txt file";
     }
     else
    cout << "Unable to open file output.txt!" << endl;

    return 0;
}

