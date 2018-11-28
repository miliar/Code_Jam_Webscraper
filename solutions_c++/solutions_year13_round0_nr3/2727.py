#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool ispalindrome(long long num);
int dim = 15;

int main()
{
  long long cases, start, finish, current, total;
  ofstream fout("palindrome.out");
  ifstream fin("C-small-attempt0.in");

  fin >> cases;

  for (int i = 1; i <= cases; i++)
    {
      fin >> start >> finish;
      current = 0;
      total = 0;
      while (current*current < start)
	current++;
      while (current*current <= finish)
	{
	  if (ispalindrome(current))
	    if (ispalindrome(current * current))
	      total++;
	  current++;
	}
      fout << "Case #" << i << ": " << total << endl;
    }
}

bool ispalindrome(long long num)
{
  int arraynum[dim];
  int digits;
  for(int i = 0; i < dim; i++)
    {
      arraynum[i] = num % 10;
      if (arraynum[i] > 0)
	digits = i + 1;
      num = num / 10;
    }
  bool check = true;
  for (int j = 0; j <= digits / 2; j++)
    if (arraynum[j] != arraynum[digits - 1 - j])
      check = false;
  return check;
}
