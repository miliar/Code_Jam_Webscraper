//
// main.cpp for GoogleCodeJamEx01 in /home/kern
// 
// Made by Matthieu Kern
// Login   <kern_m@epitech.net>
// 
// Started on  Sat Apr 12 01:14:12 2014 Matthieu Kern
// Last update Sat Apr 12 03:24:10 2014 Matthieu Kern
//

#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <vector>

float
time_to_win(float x, float f, int factories, float t)
{
  float	cps;

  cps = 2.f + f * (float)factories;
  return (x / cps + t);
}

void
exec_cookies(float c, float x, float f, int r)
{
  float	t = 0;
  int	factories = 0;

  while (1)
    {
      if (time_to_win(x, f, factories + 1, time_to_win(c, f, factories, t)) <
	  time_to_win(x, f, factories, t))
	{
	  t = time_to_win(c, f, factories, t);
	  ++factories;
	}
      else
	{
	  std::cout << "Case #" << r << ": ";
	  std::cout.precision(7);
	  std::cout.setf(std::ios::fixed, std::ios::floatfield);
	  std::cout << time_to_win(x, f, factories, t) << std::endl;
	  return ;
	}
    }
}

int
main()
{
  int	nb, i;
  float	c, x, f;

  std::cin >> nb;
  for (i = 0 ; i < nb ; ++i)
    {
      std::cin >> c >> f >> x;
      exec_cookies(c, x, f, i + 1);
    }
}
