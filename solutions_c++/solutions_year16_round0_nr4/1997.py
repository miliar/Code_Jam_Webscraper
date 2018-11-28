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

llu testNum, k, c, s;
vector<llu> clean_places;

llu pow (llu b, llu e)
{
  if (e == 0)
    return 1;

  llu p = 1;
  for (llu i = 0; i < e; ++i)
    p *= b;

  return p;
}

string expand (string base, llu comp)
{
  string exp = base, prev = base, golds = "";
  for (llu i = 0; i < base.length (); ++i)
    golds += "G";
  for (llu i = 1; i < comp; ++i)
    {
      exp = "";
      for (llu j = 0; j < prev.length (); ++j)
        {
          if (prev[j] == 'L')
            exp += base;
          else
            exp += golds;
        }
      prev = exp;
    }
  return exp;
}

void print_all_expansions (llu len, llu comp)
{
  for (llu i = 0; i < (1<<len); ++i)
    {
      llu bin = i;
      string base = "";
      for (llu j = 0; j < len; ++j)
        {
          base += (bin&1)?"L":"G";
          bin /= 2;
        }
      cout << expand (base, comp) << endl;
    }
}

llu get_clean_place (llu len, llu comp)
{
  llu clean_place = 0;
  for (llu i = 0; i < comp-1; ++i)
    {
      clean_place += min(len-1, i);
      clean_place *= len;
    }
  clean_place += min(len-1, comp-1);
  return clean_place+1;
}

bool find_best_clean_places (llu len, llu comp, llu stud)
{
  if (stud == 0)
    return false;
  if (len == 1)
    {
      clean_places.push_back (1);
      return true;
    }
  llu elim = comp;
  llu offs = elim*pow (len, comp-1);

  llu insert_place = clean_places.size ();
  clean_places.push_back (get_clean_place (len, comp));

  if (len <= elim)
    return true;
  if (!find_best_clean_places (len-elim, comp, stud-1))
    return false;

    for (llu j = insert_place+1; j != clean_places.size (); ++j)
    {
      llu prev_place = clean_places[j]-1;
      llu corrected_place = 0;
      //cout << "prev: " << (prev_place+1) << endl;
      for (llu i = comp-1; ; --i)
        {
          /*cout << "adding: " << endl;
          cout << "(" << pow(len, i) << " * " << "(" << elim << " + "
               << prev_place << "/" << pow(len-elim, comp-1-i) << ")" << ")"
               << endl;*/
          corrected_place +=
            pow(len, i)*(elim + prev_place/pow(len-elim, i));
          prev_place =
            prev_place - (prev_place/pow(len-elim, i))*pow(len-elim, i);

          if (i == 0)
            break;
        }

      //cout << "corrected: " << (corrected_place+1) << endl;
      clean_places[j] = corrected_place+1;
    }
  return true;
}

int main(int argc, char **argv)
{
  ifstream ifile("D-large.in");
  FILE *ofile = fopen("out.txt", "w");
  ifile >> testNum;
  for (llu i = 0; i < testNum; ++i) {
    clean_places.clear ();
    ifile >> k >> c >> s;
    if (pow(k, c) < 10 && k < 5)
      print_all_expansions (k, c);
    printf ("Case #%lld: ", i+1);
    fprintf (ofile, "Case #%lld: ", i+1);
    if (!find_best_clean_places (k, c, s))
      {
        printf ("IMPOSSIBLE\n");
        fprintf (ofile, "IMPOSSIBLE\n");
        continue;
      }
    for (auto it = clean_places.begin (); it != clean_places.end (); ++it)
      {
        printf ("%lld ", *it);
        fprintf (ofile, "%lld ", *it);
      }
    printf ("\n");
    fprintf (ofile, "\n");
  }
  ifile.close();
  fclose(ofile);
  return 0;
}
