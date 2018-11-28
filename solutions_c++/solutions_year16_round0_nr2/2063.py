#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int min(int a, int b) {return (a<b)?a:b;}
int max(int a, int b) {return (a>b)?a:b;}

using namespace std;

typedef long long unsigned llu;

unsigned testNum, k, c, s;


int main(int argc, char **argv)
{
  ifstream ifile("B-large.in");
  FILE *ofile = fopen("out.txt", "w");
  ifile >> testNum;
  string panc;
  getline(ifile, panc);
  for (unsigned i = 0; i < testNum; ++i) {
    unsigned flips = 0;
    getline(ifile, panc);
    char prev_char = panc[0];
    for (unsigned j = 1; j < panc.length (); ++j)
      {
        if (panc[j] != prev_char)
          ++flips;
        prev_char = panc[j];
      }
    if (panc[panc.length ()-1] == '-')
      ++flips;
    printf ("Case #%d: %d\n", i+1, flips);
    fprintf (ofile, "Case #%d: %d\n", i+1, flips);

  }
  ifile.close();
  fclose(ofile);
  return 0;
}
