#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

int main ()
{
    ifstream in ("A-small-attempt2.in");
    ofstream out ("output.txt");
    int n;
    int i;
    int j;
    int k;
    char a;
    char v[5][5];
    int solution;
    in >> n;
    for (i = 0; i < n; i++)
        {
        in >> v[1][1] >> v[1][2] >> v[1][3] >> v[1][4];
        in >> v[2][1] >> v[2][2] >> v[2][3] >> v[2][4];
        in >> v[3][1] >> v[3][2] >> v[3][3] >> v[3][4];
        in >> v[4][1] >> v[4][2] >> v[4][3] >> v[4][4];
        solution = 0;
        for (j = 0; j < 4; j++)
            {
            if (v[1][j] == 'X' || v[1][j] == 'T')
               {
               if ((v[2][j] == 'X' || v[2][j] == 'T') &&
                   (v[3][j] == 'X' || v[3][j] == 'T') &&
                   (v[4][j] == 'X' || v[4][j] == 'T'))
                   {
                   out << "Case #" << i+1 << ": X won";
                   solution = 1;
                   };
               };
            if ((solution == 0) && (v[1][j] == 'O' || v[1][j] == 'T'))
               {
               if ((v[2][j] == 'O' || v[2][j] == 'T') &&
                   (v[3][j] == 'O' || v[3][j] == 'T') &&
                   (v[4][j] == 'O' || v[4][j] == 'T'))
                   {
                   out << "Case #" << i+1 << ": O won";
                   solution = 1;
                   };
               };
            if ((solution == 0) && (v[j][1] == 'X' || v[j][1] == 'T'))
               {
               if ((v[j][2] == 'X' || v[j][2] == 'T') &&
                   (v[j][3] == 'X' || v[j][3] == 'T') &&
                   (v[j][4] == 'X' || v[j][4] == 'T'))
                   {
                   out << "Case #" << i+1 << ": X won";
                   solution = 1;
                   };
               };
            if ((solution == 0) && (v[j][1] == 'O' || v[j][1] == 'T'))
               {
               if ((v[j][2] == 'O' || v[j][2] == 'T') &&
                   (v[j][3] == 'O' || v[j][3] == 'T') &&
                   (v[j][4] == 'O' || v[j][4] == 'T'))
                   {
                   out << "Case #" << i+1 << ": O won";
                   solution = 1;
                   };
               };
            };
        if ((solution == 0) && (v[1][1] == 'X' || v[1][1] == 'T'))
           {
           if ((v[2][2] == 'X' || v[2][2] == 'T') &&
               (v[3][3] == 'X' || v[3][3] == 'T') &&
               (v[4][4] == 'X' || v[4][4] == 'T'))
               {
               out << "Case #" << i+1 << ": X won";
               solution = 1;
               };
           };
        if ((solution == 0) && (v[1][4] == 'X' || v[1][4] == 'T'))
           {
           if ((v[2][3] == 'X' || v[2][3] == 'T') &&
               (v[3][2] == 'X' || v[3][2] == 'T') &&
               (v[4][1] == 'X' || v[4][1] == 'T'))
               {
               out << "Case #" << i+1 << ": X won";
               solution = 1;
               };
           };
        if ((solution == 0) && (v[1][1] == 'O') || (v[1][1] == 'T'))
           {
           if ((v[2][2] == 'O' || v[2][2] == 'T') &&
               (v[3][3] == 'O' || v[3][3] == 'T') &&
               (v[4][4] == 'O' || v[4][4] == 'T'))
               {
               out << "Case #" << i+1 << ": O won";
               solution = 1;
               };
           };
        if ((solution == 0) && (v[1][4] == 'O') || (v[1][4] == 'T'))
           {
           if ((v[2][3] == 'O' || v[2][3] == 'T') &&
               (v[3][2] == 'O' || v[3][2] == 'T') &&
               (v[4][1] == 'O' || v[4][1] == 'T'))
               {
               out << "Case #" << i+1 << ": O won";
               solution = 1;
               };
           };
        if (solution == 0)
           {
           for (j = 0; j < n; j++)
               {
               for (k = 0; k < n; k++)
                   {
                   if (v[j][k] == '.') 
                      {
                      solution = 2;   
                      };
                   };
               };
           if (solution == 2)
              {
              out << "Case #" << i+1 << ": Game has not completed";         
              }
           else
               {
               out << "Case #" << i+1 << ": Draw";
               };
           };
        if (i != n-1)
           {
           out << "\n";      
           }
        };
    return 0; 
}
