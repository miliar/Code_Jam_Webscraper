#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool is_palindrome(int i)
{
  int j = i;
  int nbc = 0;
  char nb[100];

  for (int k = 0; j >= 1; k++)
    {
      nb[k] = j % 10;
      j /= 10;
      nbc++;
    }
  
  nb[nbc] = 0;

  j = 0;

  for (int k = 0; nb[k] != 0; k++)
    {
      j *= 10;
      j += nb[k];
    }

  if (j != i)
    return false;

  return true;
}

bool is_fair_and_square(int i)
{
  double sqrd;
  int sqri;

  if (!is_palindrome(i))
    return false;
  
  sqrd = (double) i;
  sqrd = sqrt(sqrd);
  sqri = (int) sqrd;
  sqri *= sqri;

  if (sqri != i)
    return false;

  sqri = (int) sqrd;
  if (!is_palindrome(sqri))
    return false;

  return true;
}

int main(int argc, char **argv)
{
  ifstream in_file;
  ofstream out_file;
  string read;
  int read_number;
  int nb_test;

  int A;
  int B;
  int nb_fair_and_square;


  if (argc != 3)
    {
      cout << "Wrong number of arguments" << endl;
      return 1;
    }

  in_file.open(argv[1]);
  out_file.open(argv[2]);

  if (in_file.is_open() == false || out_file.is_open() == false)
    {
      cout << "File cannot be open" << endl;
      return 1;
    }

  in_file >> read_number;
  nb_test = read_number;

  for (int i = 0; i < nb_test; i++)
    {
      nb_fair_and_square = 0;

      in_file >> read_number;
      A = read_number;
      in_file >> read_number;
      B = read_number;

      for (int j = A; j <= B; j++)
	if (is_fair_and_square(j))
	  nb_fair_and_square++;

      out_file << "Case #" << i + 1 << ": " << nb_fair_and_square << endl;
    }

  in_file.close();
  out_file.close();

  return 0;
}
