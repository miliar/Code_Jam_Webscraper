#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;



void	read_file(string const &filename)
{
  ifstream file(filename);

  int nb_test;

  file >> nb_test;
  for (int i = 0; i < nb_test; ++i)
    {
      double min = -1;
      double c, f, x;

      file >> c >> f >> x;
      double n = 0;
      //for (double n = 0; n < n_max_farm; ++n)
      while (n < x * f)
	{
	  double time = 0;
	  for (double i = 0; i < n; ++i)
	    {
	      double tmp = c / (2.0 + (double)i * f);
// 	      if (min > 0 && time + tmp > min)
// 		break;
	      time += tmp;
	    }
	  time += x / (2.0 + (double)n * f);
	  if (min < 0 || time < min)
	    min = time;
	  n += 1;
	}
      std::cout.precision(7);
      cout << "Case #" << i+1 << ": " << std::fixed << min << endl;
    }
}

int	main(int ac, char **av)
{
  if (ac != 2)
    {
      cout << "file needed" << endl;
      return 1;
    }
  read_file(av[1]);
  return 0;
}
