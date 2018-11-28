#include <iostream>
#include <string>
#include <vector>

using namespace std;

long compute(int A, int B, int K)
{
  //  cout << A << " " << B << " " << K;
  long count = 0;
  int res = 0;
  for(int i = 0; i < A; i++)
    {
      for(int j = 0; j < B; j++)
	{
	  res = i & j;
	  //	  cout << " res: " << i << " " << j << " " << res << endl; 
	  if(res < K)
	    count++; 
	}
    }
  return count;
}



int main()
{
  int n;
  int sizes = 0;
  int A, B, K;


  std::cin >> n;
  std::cin.ignore();
  
  for(int i = 0; i < n; i++)
    {
      std::cout << "Case #" << i+1 << ": ";
      std::cin >> A;
      std::cin >> B;
      std::cin >> K;

      cout << compute(A, B, K);	 

      cout << std::endl;
    }

  return 0;

}


