#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
  int n;
  int col = 0;
  int count = 0;
  int sc;
  int result = 0;
  vector<int> firsts; 
  firsts.resize(4);
  
  std::cin >> n;
  std::cin.ignore();
  
  for(int i = 0; i < n; i++)
    {
      count = 0;
      std::cin >> col;
      std::cin.ignore();
      
      for(int f = 0; f < 4; f++)
	{
	  for(int t = 0; t < 4; t++)
	    {
	      std::cin >> sc;
	      if(f == col - 1)
		  firsts[t] = sc;
	    }	  
	  std::cin.ignore();
	}
      
      std::cin >> col;
      std::cin.ignore();
      for(int f = 0; f < 4; f++)
	{
	      for(int t = 0; t < 4; t++)
		{
		  std::cin >> sc;
		  if(f == col - 1)
		    {
		      //		      std::cout << sc << std::endl;
		      for(int s = 0; s < 4; s++)
			{
			  if(firsts[s] == sc)
			    {
			      count++;
			      result = sc;
			    }
			}
		    }
		  std::cin.ignore();
		}

	}
      if(count == 1)
	std::cout << "Case #" << i+1 << ": " << result << std::endl;
      else if(count == 0)
	std::cout << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;
      else
	std::cout << "Case #" << i+1 << ": Bad magician!" << std::endl;

    }

  return 0;

}
