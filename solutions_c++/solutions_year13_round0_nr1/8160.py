/** 
 * Kirsten Erich (kirstee)
 *
 * Google Code Jam
 *
 * TicTacToe.cpp
 * 
 * Program that, given a 4x4 "board," will determine what the status
 *  of that tic-tac-toe game is. A player may win by having 4 (or 3 + 1 'T')
 *  of their letters in a row, column, or diagonal of the board. It is a draw
 *  if all places on the board have been taken, but neither player has won. The
 *  game is not complete if there are still spaces, or '.', left on the board.
 * 
 * 
 * April 5, 2012
 * 9:38 PM
 * 
**/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <string.h>
#include <stdio.h>
#include <iosfwd>

using namespace std;

/* checkToken - the "token" used to check for wins is the wildcard, T;
    this method will check for a win when the token is T */
bool checkToken(string a, string b, string c, string d, ofstream & outfile, int ndx){

   string test [4] = {a,b,c,d};

/* ---- CASE 0 ---- */
   if ( ndx == 0 ){

      if ( test[0][1] == test[0][2] && test[0][2] == test[0][3] ){

         outfile << test[0][1];
         outfile << " won" << endl;
         return true;

      } // horizontal win

      else if ( test[1][0] == test[2][0] && test[2][0] == test[3][0] ){

         outfile << test[1][0];
         outfile << " won" << endl;
         return true;

      } // vertical win

      else if ( test[1][1] == test[2][2] && test[2][2] == test[3][3] ){

         outfile << test[1][1];
         outfile << " won" << endl;
         return true;

      } // diagonal win

   } // T was found at (0,0)

/* ---- CASE 1 ---- */
   else if (ndx == 1){

      if ( test[1][0] == test[1][2] && test[1][2] == test[1][3] ){

         outfile << test[1][0];
         outfile << " won" << endl;
         return true;

      } // horizontal win

      else if ( test[0][1] == test[2][1] && test[2][1] == test[3][1] ){

         outfile << test[0][1];
         outfile << " won" << endl;
         return true;

      } // vertical win

      else if ( test[0][0] == test[2][2] && test[2][2] == test[3][3] ){

         outfile << test[0][0];
         outfile << " won" << endl;
         return true;

      } // diagonal win

   } // T was found at (1,1)

/* ---- CASE 2 ---- */
   else if (ndx == 2){

      if ( test[2][0] == test[2][1] && test[2][1] == test[2][3] ){

         outfile << test[2][0];
         outfile << " won" << endl;
         return true;

      } // horizontal win

      else if ( test[0][2] == test[1][2] && test[1][2] == test[3][2] ){

         outfile << test[0][2];
         outfile << " won" << endl;
         return true;

      } // vertical win

      else if ( test[0][0] == test[1][1] && test[1][1] == test[3][3] ){

         outfile << test[0][0];
         outfile << " won" << endl;
         return true;

      } // diagonal win

   } // T was found at (2,2)

/* ---- CASE 3 ---- */
   else if (ndx == 3){

      if ( test[3][0] == test[3][1] && test[3][1] == test[3][2] ){

         outfile << test[3][0];
         outfile << " won" << endl;
         return true;

      } // horizontal win

      else if ( test[0][3] == test[1][3] && test[1][3] == test[2][3] ){

         outfile << test[0][3];
         outfile << " won" << endl;
         return true;

      } // vertical win

      else if ( test[0][0] == test[1][1] && test[1][1] == test[2][2] ){

         outfile << test[0][0];
         outfile << " won" << endl;
         return true;

      } // diagonal win

   } // T was found at (3,3)

   return false;

} // checkToken 


/* checkDraw - checks one board for a draw (if any space still contains 
    a '.' then the game is not yet complete; returns true if the game
    is a draw, false otherwise */
bool checkDraw(string a, string b, string c, string d){

   string test [4] = {a,b,c,d};

   for (int ct = 0; ct < 4; ct ++){

      for (int ct2 = 0; ct2 < 4; ct2++){

         if ( test[ct][ct2] == '.' ){

            return false;

         }

      } // search each column

   } // search each row

   return true;

} // checkDraw


/* checkForWin - checks one board for a win by cross-checking each element
    in a diagonal (and checking the opposite diagonal at the end); generates
    output if someone has been found to have won the game; returns true if 
    the game has been won, false otherwise */
bool checkForWin (string a, string b, string c, string d, ofstream & outfile){

   int ct1 = 0, ct2 = 0, ct3 = 0, ndx = 0;
   string test [4] = {a,b,c,d};

   char token = test[0][0];

   while (ndx < 4){

      if (token == 'T'){
         return checkToken(a, b, c, d, outfile, ndx);
      } 

      if (token != '.'){

         for (int z = 0; z < 4; z ++){

            /* top left to bottom right diagonal */
            if ( test[z][z] == 'T' || test[z][z] == token){
               ct1++;
            }

            /* horizonal win */
            if ( test[ndx][z] == 'T' || test[ndx][z] == token ){
               ct2++; 
            }

            /* vertical win */
            if ( test[z][ndx] == 'T' || test[z][ndx] == token ){
               ct3++; 
            }

         } // for

         if ( ct1 == 4 || ct2 == 4 || ct3 == 4){
            outfile << test[ndx][ndx];
            outfile << " won" << endl;
            return true;
         }

      } // if token != '.'

      ndx++;

      if (ndx < 4){
         ct1 = 0;
         ct2 = 0;
         ct3 = 0;
         token = test[ndx][ndx];
      }

   } // while

   int diagcheck = 3, ct = 0;

   token = test[0][3];

   if (token == 'T'){
      token = test[1][2];
   } // just in case the token is T

   if (token != '.'){

      for (int y = 0; y < 4; y++){

         if ( test[y][diagcheck] == 'T' || test[y][diagcheck] == token ){
           ct ++;
           diagcheck--;
        }

      } // for - top right to bottom left diagonal win

   } // if token != '.'

   if (ct == 4){
      outfile << test[0][3];
      outfile << " won" << endl;
      return true;
   }
   else {
      return false;
   }

} // checkForWin

/* ------------------------------------------------ */

int main (int argc, char *argv[]) {

   // start clock to check time
   clock_t start = clock();

   // initialize variables
   int size = 0, time = 240, ct = 0;
   //int idx = 0;
   string oneLine, twoLine, threeLine, fourLine;

   // declare and initialize infile and outfile
   ifstream infile (argv[1]);
   ofstream outfile (argv[2]);

   // store first int (from infile) into size
   infile >> size;

   while (ct < size){

      /* strings to hold each line (row) of the 4x4 board */
      infile >> oneLine;
      infile >> twoLine;
      infile >> threeLine;
      infile >> fourLine;

      /* generate output for each case */
      outfile << "Case #" << ct+1 << ": ";

      if ( !checkForWin(oneLine, twoLine, threeLine, fourLine, outfile) ) {

         if ( checkDraw(oneLine, twoLine, threeLine, fourLine) ) {
            outfile << "Draw" << endl;
         } // if - draw

         else {
            outfile << "Game has not completed" << endl;
         } // else - game not complete

      } // if nobody has won the game

      ct++;

   } // while there are still boards to be checked

   return 0;

} // main
