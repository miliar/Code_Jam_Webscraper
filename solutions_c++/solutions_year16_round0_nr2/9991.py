//
//  main.cpp
//  codejam_revenge_pancakes
//
//  Created by Lucas Prieels on 10/04/16.
//  Copyright © 2016 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin ("/Users/Lucas/Downloads/codejam_revenge_pancakes.in");
    ofstream fout ("/Users/Lucas/Downloads/codejam_revenge_pancakes.out");
    int nbrfois;
    fin >> nbrfois;
    for (int i; i<nbrfois; i++)
    {
        int compteur=0;
        string S;
        fin >> S;
        bool debut(true);
        bool moinsavant(false);
        for (int i=0; i<S.size();i++)
        {
          if (debut and S[i]=='-')
          {
              compteur++;
              moinsavant=true;
          }
          else if (S[i]=='-' and moinsavant==false)
          {
              compteur+=2;
              moinsavant=true;
          }
          else if (S[i]=='+')
          {
              moinsavant=false;
          }
            debut=false;
        }
        fout << "Case #" << i+1 << ": " << compteur << endl;
    }
    return 0;
}
