#include <string>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

typedef long long int int64;

int ReverseDigits(int x, int digits)
{
  int result = 0;
  while (digits-- > 0)
  {
    result = (result * 10) + (x % 10);
    x /= 10;
  }
  return result;
}

bool IsPalindrome(int64 x)
{
  char c[30];
  int digits = 0;
  while (x > 0)
  {
    c[digits++] = x % 10;
    x /= 10;
  }
  for (int i = (digits / 2 - 1); i >= 0; --i)
    if (c[i] != c[digits - 1 - i])
      return false;
  return true;
}

int main()
{
  int T;
  cin >> T;

  for (int test_case = 1; test_case <= T; ++test_case)
  {
    int64 lo, hi;
    cin >> lo >> hi;

    int lo2 = ceil(sqrt(double(lo)));
    int hi2 = floor(sqrt(double(hi)));
    int lo_digits = floor(log10(double(lo2))) + 1;
    int hi_digits = floor(log10(double(hi2))) + 1;
    cerr << "{" << lo2 << "(" << lo_digits << "), " << hi2 << "(" << hi_digits << ")}" << endl;
    int count = 0;
    for (int num_digits = lo_digits; num_digits <= hi_digits; ++num_digits)
    {
      cerr << "#" << num_digits << endl;
      if (num_digits & 1)
      {
	// Odd # digits
	int part_digits = num_digits / 2;
	int part_pow = int(pow(10, part_digits));
	int start = (num_digits == lo_digits) ? (lo2 / part_pow) : part_pow;
	if ((start * part_pow + ReverseDigits(start / 10, part_digits)) < lo2)
	  ++start;

	int end = (num_digits == hi_digits) ? (hi2 / part_pow) : (part_pow * 10 - 1);
	if ((end * part_pow + ReverseDigits(end / 10, part_digits)) > hi2)
	  --end;

	cerr << "[" << start << ", " << end << "]" << endl;
	for (int part = start; part <= end; ++part)
	{
	  int64 pali = part * part_pow + ReverseDigits(part / 10, part_digits);
	  int64 square = pali * pali;
	  if (IsPalindrome(square))
	  {
	    cerr << pali << " " << square << endl;
	    ++count;
	  }
	}
      }
      else
      {
	// Even # digits
	int part_digits = num_digits / 2;
	int part_pow = int(pow(10, part_digits));
	int start = (num_digits == lo_digits) ? (lo2 / part_pow) : (part_pow / 10);
	if ((start * part_pow + ReverseDigits(start, part_digits)) < lo2)
	  ++start;

	int end = (num_digits == hi_digits) ? (hi2 / part_pow) : (part_pow - 1);
	if ((end * part_pow + ReverseDigits(end, part_digits)) > hi2)
	  --end;

	cerr << "[" << start << ", " << end << "]" << endl;
	for (int part = start; part <= end; ++part)
	{
	  int64 pali = part * part_pow + ReverseDigits(part, part_digits);
	  int64 square = pali * pali;
	  if (IsPalindrome(square))
	  {
	    cerr << pali << " " << square << endl;
	    ++count;
	  }
	}
      }
    }
    cerr << "Case #" << test_case << ": " << count << endl;
    cout << "Case #" << test_case << ": " << count << endl;
  }
  return 0;
}

