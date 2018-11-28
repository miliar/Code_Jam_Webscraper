#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>

using std::cout;
using std::cin;
using std::cerr;
using std::endl;
using std::vector;

long long solve(const vector < long long > &result)
{
  long long A, B;
  scanf("%lld %lld", &A, &B);

  long long a = (long long)sqrt((double)A) - 1;
  long long b = (long long)sqrt((double)B) + 1;

  while (a * a < A)
    a++;
  while (b * b > B)
    b--;
  a--;

  return result[b] - result[a];
}

bool check_polindrom(long long k)
{
  char k_string[100];
  sprintf(k_string, "%lld", k);

  int n = strlen(k_string);
  for (int index = 0; index < n / 2; ++index)
    if (k_string[index] != k_string[n - 1- index])
      return false;

  return true;
}

void calculate_pre_result(vector < long long > &result)
{
  result.resize(10000005, 0);
  for (long long index = 1; index < result.size(); ++index)
  {
    if (check_polindrom(index) && check_polindrom(index * index))
    {
      cerr << index << " " << index * index << endl;
      result[index] = 1;
    }

    result[index] += result[index - 1];
  }
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests_count;
  scanf("%d\n", &tests_count);

  vector < long long > pre_result;
  calculate_pre_result(pre_result);

  for (int test = 0; test < tests_count; ++test)
  {
    cout << "Case #" << test + 1 << ": " << solve(pre_result) << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}

