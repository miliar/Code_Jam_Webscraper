#include <iostream>
#include <fstream>

using namespace std;
const int N = 4;
void ReadCase   (ifstream&, char**);
void showM      (char**);
int  chekWin    (char**, char);
bool isDot      (char**);
bool checkDraw  (char**);
void checkCase  (ofstream&, char**);


int main()
{
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    char **M;
    M = new char *[N];
    for (int i = 0; i < N; i++)
        M[i] = new char [N];
    
    int numOfCases = 0;
    
    infile >> numOfCases;
    
    for (int i = 0; i < numOfCases; i++)
    {
        ReadCase  (infile,  M);
        outfile << "Case #" << i+1 << ": ";
        checkCase (outfile, M);
    }
	
	cout << "It's ok." << endl;
    infile.close();
    outfile.close();
    return 0;
}

void ReadCase (ifstream& infile, char** M)
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            infile >> M[i][j];
}

void showM (char** M)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cout << M[i][j];
        cout << endl;
    }
}

int chekWin (char **M, char c)
{
    char T = 'T';

    for (int i = 0; i < N; i++)
    {
        if ((M[i][0]==c||M[i][0]==T)&&(M[i][1]==c||M[i][1]==T)&&(M[i][2]==c||M[i][2]==T)&&(M[i][3]==c||M[i][3]==T))
        {   
            return 1;
        }
         
        else continue;
     }   
     
     for (int i = 0; i < N; i++)
     {
        if ((M[0][i]==c||M[0][i]==T)&&(M[1][i]==c||M[1][i]==T)&&(M[2][i]==c||M[2][i]==T)&&(M[3][i]==c||M[3][i]==T))
        {  
            return 1;
        }
        
        else continue;
      } 
       
      if ((M[0][0]==c||M[0][0]==T)&&(M[1][1]==c||M[1][1]==T)&&(M[2][2]==c||M[2][2]==T)&&(M[3][3]==c||M[3][3]==T))
      {   
          return 1;
      }

      else if ((M[0][3]==c||M[0][3]==T)&&(M[1][2]==c||M[1][2]==T)&&(M[2][1]==c||M[2][1]==T)&&(M[3][0]==c||M[3][0]==T))
      {   
          return 1;
      }
    
    return 0;
}

bool isDot (char** M)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (M[i][j] == '.')
                return true;
            else continue;
        }
    }
    
    return false;
}

bool checkDraw (char** M)
{
    if (!(chekWin (M, 'X') && !(chekWin (M, 'O'))) && !isDot(M))
        return true;
    else 
        return false;
}

void checkCase (ofstream& outfile, char** M)
{
    if (chekWin (M, 'X')) 
            outfile << "X won\n";
    else if (chekWin (M, 'O'))
            outfile << "O won\n";
    else if (checkDraw(M))
            outfile << "Draw\n";
    else outfile << "Game has not completed\n";
}
