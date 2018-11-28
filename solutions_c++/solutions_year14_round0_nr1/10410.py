#include <iostream>
#include <stdio.h>

int main()
{
  int n, m, kol;
  freopen ("A-small-attempt.in", "r", stdin);
  freopen ("outp.txt", "w", stdout);
  std::cin >> kol;
  for (int k = 1; k <= kol; ++k)
    {
      int vec[4], vec2[4];
      std::cin >> n;
      for (int i=1; i<=4; ++i)
	if (i == n)
	  {
	    std::cin >> vec[0];
	    std::cin >> vec[1];
	    std::cin >> vec[2];
	    std::cin >> vec[3];
	  }
	else
	  for (int j=0; j < 4; ++j)
	    std::cin >> m;
      std::cin >> n;
      for (int i=1; i<=4; ++i)
	if (i == n)
	  {
	    std::cin >> vec2[0];
	    std::cin >> vec2[1];
	    std::cin >> vec2[2];
	    std::cin >> vec2[3];
	  }
	else
	  for (int j=0; j < 4; ++j)
	    std::cin >> m;
      int sovp = 0, numbsovp = 0;
      for (int i=0; i<4; ++i)
	for (int j=0; j<4; ++j)
	  if (vec[i] == vec2[j])
	    {
	      sovp++;
	      numbsovp = vec[i];
	    }
      //      std::cout << numbsovp << " " << sovp << " ";
      //std::cout << vec[0] << " " << vec[1] << " " << vec[2] << " " << vec[3] << "   " << vec[0] << " " << vec2[1] << " " << vec2[2] << " " << vec2[3] << " " ;
      switch (sovp)
	{
	case 1:
	  std::cout << "Case #" << k << ": " << numbsovp << "\n";
	  break;
	case 0:
	  std::cout << "Case #" << k <<  ": Volunteer cheated!\n";
	  break;
	default:
	  std::cout << "Case #" << k << ": Bad magician!\n";
	  break;
	}
    }
  return 0;
}
