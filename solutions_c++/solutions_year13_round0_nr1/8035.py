#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <fstream>
#include <iostream>

#define D 4
#define X 'X'
#define O 'O'
#define S "A-small-attempt1.in"
#define L "C-large-attempt0.in"

using namespace std;

char A[D][D];
int Xc = 0;
int Oc = 0;
int x=-1,y=-1;
int ch(char s)
{
    int i,j;
    i = j = 0;
    int out=-1;
    A[x][y] = s;
    for (;i<D;i++)
                  if(s == A[i][0] && A[i][0] == A[i][1] && A[i][1] == A[i][2] && A[i][2] == A[i][3])
                  {
                             out = 4;
                             break;
                  }
                             
    for (;j<D;j++)
                  if(s ==A[0][j] && A[0][j] == A[1][j] && A[1][j] == A[2][j] && A[2][j] == A[3][j])
                  {
                             out = 4;
                             break;
                  }
    if(s == A[0][0] && A[0][0] == A[1][1] && A[1][1] == A[2][2] && A[2][2] == A[3][3])
         out = 4;
    if(s == A[0][3] && A[0][3] == A[1][2] && A[1][2] == A[2][1] && A[2][1] == A[3][0])
               out = 4;
    A[x][y] = 'T';
    return out;
}  
int NoDot()
{
    int i, j;
    for(i=0; i < D; i++)
        {
                 for(j=0; j < D; j++)
                          if(A[i][j]=='.')
                                          return 0;          
        }
        return 1;
}


int main(int argc, char* argv[])
{
    int i, j, k, c = 0, a, b,f =1;
    int var = 0;
    char result[30], buffer[50];
    ifstream file;
    ofstream fil;
    file.open(S, ios::in);
    fil.open("C.out", ios::out);
    file>>var;
    cout<<var<<"\n";
    for (int loop = 0; loop < var; loop++)
    {
        Oc = Xc = 0;
        for(i=0; i < D; i++)
                     for(j=0; j < D; j++)
                     {
                              file>>A[i][j];
                              if(A[i][j]=='T')
                              {
                                              x = i;
                                              y = j;
                              }
                     }
        Xc=ch(X);
        Oc=ch(O);
        if(Xc==4)
                 strcpy(result, "X won");
        else if(Oc==4)
                 strcpy(result, "O won");
        else if(NoDot()==0)
                 strcpy(result, "Game has not completed");
        else
                 strcpy(result, "Draw");
        
        sprintf(buffer, "Case #%d: %s\n", loop+1, result);
        printf("%s",buffer);
        fil<<buffer;
       
    }
    system("pause");
    file.close();
    fil.close();
    return 0;
}
/*
        for(i=0; i < D; i++)
        {
                 for(j=0; j < D; j++)
                          cout<<A[i][j]<<" ";
                 cout<<'\n';           
        }
        cout<<"\n\n";
        
        cout<<::Xc<<' '<<::Oc;
        cout<<".\n\n";*/
