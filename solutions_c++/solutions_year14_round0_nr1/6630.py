#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int t, w1, w2, a[7][7], used[7][21];
void inmake()
{ ifstream fin;
  fin.open("in.txt");
  
  ofstream fout;
  fout.open("out.txt");
  
  fin >> t;
  for (int i = 0; i < t; i++)
  { fin >> w1;
    for (int j = 0; j < 4; j++)
    for (int k = 0; k < 4; k++)
    { fin >> a[j][k];
      used[j][a[j][k] - 1] = 1;
     }
    
    fin >> w2;
    for (int j = 0; j < 4; j++)
    for (int k = 0; k < 4; k++)
    fin >> a[j][k];
    
    int save = 0, ok = 0;
    for (int j = 0; j < 4; j++)
    if (used[w1 - 1][a[w2 - 1][j] - 1] != 0)
    { save = a[w2 - 1][j]; ok++; }
    
    if (ok == 0) fout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
    else if (ok == 1) fout << "Case #" << i + 1 << ": " << save << endl;
    else if (ok > 1) fout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
    
    memset(used, 0, sizeof(used));
   }
}

int main()
{ 
  inmake();
  
  cin >> t;
  return 0;
}
