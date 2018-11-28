//
// main.cpp for GoogleCodeJamEx01 in /home/kern
// 
// Made by Matthieu Kern
// Login   <kern_m@epitech.net>
// 
// Started on  Sat Apr 12 01:14:12 2014 Matthieu Kern
// Last update Sat Apr 12 02:13:21 2014 Matthieu Kern
//

#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <vector>

int
nb_corres(int fl[4],
	  int sl[4],
	  int &c)
{
  int		i, j, sol;

  sol = 0;
  for (i = 0 ; i < 4 ; ++i)
    {
      for (j = 0 ; j < 4 ; ++j)
	{
	  if (fl[i] == sl[j])
	    {
	      c = fl[i];
	      ++sol;
	    }
	}
    }
  return (sol);
}

int
main()
{
  int	nb, i, j, k, l, c;
  int	fl[4], sl[4];
  int	fst, sec;
  int	v;

  std::cin >> nb;
  for (i = 0 ; i < nb ; ++i)
    {
      for (j = 0 ; j < 2 ; ++j)
	{
	  if (j == 0)
	    std::cin >> fst;
	  else
	    std::cin >> sec;
	  for (k = 0 ; k < 4 ; ++k)
	    {
	      for (l = 0 ; l < 4 ; ++l)
		{
		  if (k + 1 == fst && j == 0)
		    std::cin >> fl[l];
		  else if (k + 1 == sec && j == 1)
		    std::cin >> sl[l];
		  else
		    std::cin >> v;
		}
	      if (k + 1 == sec && j == 1)
		{
		  std::cout << "Case #" << i + 1 << ": ";
		  switch (nb_corres(fl, sl, c))
		    {
		    case 0:
		      std::cout << "Volunteer cheated!" << std::endl;
		      break;
		    case 1:
		      std::cout << c << std::endl;
		      break;
		    default:
		      std::cout << "Bad magician!" << std::endl;
		      break;
		    }
		}
	    }
	}
    }
}
