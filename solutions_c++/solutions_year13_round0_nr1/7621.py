#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
using namespace std;

//#define SMALL
#define LARGE

#ifdef SMALL
    #define INPATH "A-small-attempt0.in"
    #define OUTPATH "A-small-attempt0.out"
#endif

#ifdef LARGE
    #define INPATH "A-large.in"
    #define OUTPATH "A-large.out"
#endif


struct ProblemVariables {

     int nbrCases;
     int currentCase;
     char input[4][4];
     string output;

     ProblemVariables()
          : nbrCases(0)
          , currentCase(1)
          , output()
     {
     }

     void solveCase () {
          if(verifyWin('X')) {
               output = "X won";
               return;
          }
          if(verifyWin('O')) {
               output = "O won";
               return;
          }
          if(!isCompleted()) {
               output = "Game has not completed";
               return;
          }         
          output = "Draw";
     }
     
     bool isCompleted() {
          for(int i = 0; i < 4; ++i)
               for(int j = 0; j < 4; ++j) {
                    if(input[i][j] == '.')
                         return false;
               }
          return true;
     }
     
     bool verifyWin(char xOrO) {

          //verifyDiagonal
          if (
              (input[0][0] == xOrO || input[0][0] == 'T')
           && (input[1][1] == xOrO || input[1][1] == 'T')
           && (input[2][2] == xOrO || input[2][2] == 'T')
           && (input[3][3] == xOrO || input[3][3] == 'T')
          ) return true;
          
          if (
              (input[0][3] == xOrO || input[0][3] == 'T')
           && (input[1][2] == xOrO || input[1][2] == 'T')
           && (input[2][1] == xOrO || input[2][1] == 'T')
           && (input[3][0] == xOrO || input[3][0] == 'T')
          ) return true;

          for (int i = 0; i < 4; ++i)
          {
               //verifyHorizontal
               if (
                   (input[i][0] == xOrO || input[i][0] == 'T')
                && (input[i][1] == xOrO || input[i][1] == 'T')
                && (input[i][2] == xOrO || input[i][2] == 'T')
                && (input[i][3] == xOrO || input[i][3] == 'T')
               ) return true;
               
               //verifyVertical
               if (
                   (input[0][i] == xOrO || input[0][i] == 'T')
                && (input[1][i] == xOrO || input[1][i] == 'T')
                && (input[2][i] == xOrO || input[2][i] == 'T')
                && (input[3][i] == xOrO || input[3][i] == 'T')
               ) return true;
          }
          return false;
     }

     void printOutput () {
         cout << "Case #" << currentCase << ": " << output << endl;
         currentCase++;
     }

     ~ProblemVariables () {

     }
} variables;

inline void solve () {

     string numberOfCases;
     getline (cin, numberOfCases);
     variables.nbrCases = atoi(numberOfCases.c_str());

     for (int i = 1; i <= variables.nbrCases; ++i) {
         for(int j = 0; j < 4; ++j) {
             for(int k = 0; k < 4; ++k) {
                 cin >> variables.input[j][k];
             }
         }

        variables.solveCase ();
        variables.printOutput ();
     }
}

inline void openStreams () {
    freopen(INPATH,"rt",stdin);
    freopen(OUTPATH,"wt",stdout);
}

int main () {
     openStreams ();
     solve ();

return 0;
}

