
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int min(int a, int b) {return (a<b)?a:b;}
int max(int a, int b) {return (a>b)?a:b;}

using namespace std;

typedef long long unsigned llu;

unsigned testNum, k, c, s;

map<unsigned, unsigned> count_map;

void preproc ()
{
  FILE *hfile = fopen("help.txt", "w");
  bool digits[10];
  for (unsigned i = 0; i <= 1000000; ++i)
    {
      for (unsigned j = 0; j <= 9; ++j)
        digits[j] = false;

      unsigned count = i;
      if (count == 0)
        count = -1;
      else if (i%100 == 0 && count_map.find(i/10) != count_map.end ())
          count = count_map[i/10]*10;
      else
        {
          while (true)
            {
              unsigned count_digits = count;
              while (count_digits > 0)
                {
                  digits[count_digits%10] = true;
                  count_digits /= 10;
                }

              bool missing = false;
              for (unsigned j = 0; j <= 9; ++j)
                {
                  if (digits[j] == false)
                    {
                      missing = true;
                      break;
                    }
                }

              if (!missing)
                break;
              count += i;
            }
        }

      count_map[i] = count;
      printf ("%d: %d\n", i, count);
      fprintf (hfile, "%d %d\n", i, count);
    }
  fclose (hfile);
}

void read_preproc_file ()
{
  ifstream hfile("help.txt");
  while (!hfile.eof ())
    {
      unsigned num, count;
      hfile >> num >> count;
      count_map[num] = count;
      //cout << num << ": " << count << endl;
    }
  hfile.close();
}

int main(int argc, char **argv)
{
  //preproc ();
  //return 0;
  read_preproc_file ();
  ifstream ifile("A-large.in");
  FILE *ofile = fopen("out.txt", "w");
  ifile >> testNum;
  for (unsigned i = 0; i < testNum; ++i) {
    unsigned ans = 0, num;
    ifile >> num;
    if (count_map[num] == -1)
      {
        printf ("Case #%d: INSOMNIA\n", i+1);
        fprintf (ofile, "Case #%d: INSOMNIA\n", i+1);
      }
    else
      {
        printf ("Case #%d: %d\n", i+1, count_map[num]);
        fprintf (ofile, "Case #%d: %d\n", i+1, count_map[num]);
      }
  }
  ifile.close();
  fclose(ofile);
  return 0;
}
