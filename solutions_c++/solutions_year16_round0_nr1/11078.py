#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>

void update(int N, std::vector<int> *seen)
{
  do
  {
    int d=N%10;
    (*seen)[d]=1;
    N=N-d;
    N/=10;
  }
  while(N>0); 
}

std::string solve(int N)
{
  if (N==0) return "INSOMNIA";
  std::vector<int> seen(10,0);
  int mul=0;
  for(int stop=0; stop<1000; ++stop)
  {
    mul++;
    update(mul*N, &seen); 
    if (std::accumulate(seen.begin(), seen.end(), 0)==10)
    {
      std::stringstream ss;
      ss<<mul*N;
      return ss.str();
    }
  }
  std::cerr << N << " is INSOMNIA for the first 1000 multiplications!!" << std::endl;
  return "INSOMNIA";
}

int main (int argc, char *argv[])
{
  if (argc<2) return -1;
  std::ifstream in(argv[1]);
  int T; in>>T;
  for (int t=0; t<T; ++t)
  {
    int N;
    in>>N;
    std::cout << "Case #" << t+1 << ": " << solve(N) << std::endl;
  }
  return 0;
}
