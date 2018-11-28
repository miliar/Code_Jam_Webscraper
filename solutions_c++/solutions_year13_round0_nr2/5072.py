#include <iostream>
#include <vector>
#include <map>

bool	compareResultWanted(std::vector< std::vector<int> > &lawn,
			    std::vector< std::vector<int> > &start,
			    int &n, int &m)
{
      bool good = true;
      for (int i = 0; i < n; ++i)
	{
	  for (int j = 0; j < m; ++j)
	    {
	      if (start[i][j] != lawn[i][j])
		{
		  return false;
		}
	    }
	}
      return true;
}

void	tryToLawn(std::vector< std::vector<int> > &lawn,
			    std::vector< std::vector<int> > &start,
			    int &n, int &m)
{
  for (int i = 0; i < n; ++i)
    {
      int maxline = -1;
      for (int j = 0; j < m; ++j)
	{
	  if (lawn[i][j] > maxline)
	    maxline = lawn[i][j];
	}
      for (int j = 0; j < m; ++j)
	{
	  if (maxline < start[i][j])
	    start[i][j] = maxline;
	}	  
    }
  for (int j = 0; j < m; ++j)
    {
      int maxline = -1;
      for (int i = 0; i < n; ++i)
	{
	  if (lawn[i][j] > maxline)
	    maxline = lawn[i][j];
	}
      for (int i = 0; i < n; ++i)
	{
	  if (start[i][j] > maxline)
	    start[i][j] = maxline;
	}
    }
}

int	main()
{
  int nb_cases;

  std::cin >> nb_cases;
  for (int test_case = 1; test_case <= nb_cases; ++test_case)
    {
      std::cout << "Case #" << test_case << ": ";

      int m, n;
      std::cin >> n;
      std::cin >> m;
      std::vector<std::vector<int> > lawn(n, std::vector<int>(m));
      std::vector<std::vector<int> > start(n, std::vector<int>(m));
      for (int i = 0; i < n; ++i)
	{
	  for (int j = 0; j < m; ++j)
	    {
	      std::cin >> lawn[i][j];
	      start[i][j] = 100;
	    }
	}
      tryToLawn(lawn, start, n, m);
      if (compareResultWanted(lawn, start, n, m))
	std::cout << "YES" << std::endl;
      else
	std::cout << "NO" << std::endl;
    }
}
