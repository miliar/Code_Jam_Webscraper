#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int
get_result();

int
recursion();

int main(int argc, char *argv[])
{
  int case_amount = 0;
  cin >> case_amount;
    
  for (int i = 0; i < case_amount; ++i)
  {
    const int result = get_result();

    cout << "Case #" << 1 + i << ": " << result << endl;

  }

  return 0;
}

#define MAX_SIZE 12

int array[MAX_SIZE];

int
get_result()
{
  int N, X;

  cin >> N >> X;

  memset(array, 0, sizeof(array));
  
  for (int i = 1; i <= N; ++i)
    cin >> array[i];

  sort(array + 1, array + 1 + N, greater<int>());

  int res = 0, padd = 0, * pindex = NULL;
  for (int i = 1; i <= N; ++i)
  {
    if (array[i] <= X)
    {
      padd = X - array[i];
      pindex = std::find_if(array + 1 + i, array + 1 + N,
                            std::bind2nd(std::less<int>(), padd + 1));

      *pindex = X + 1;

      res++;
    }
  }    
  
  return res;
}

int
recursion()
{
  return 0;
}
