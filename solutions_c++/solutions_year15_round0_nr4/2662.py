#include <map>
#include <limits>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
  string ans;
  
  for(int X = 1; X <= 4; X++)
    for(int R = 1; R <= 4; R++)
      for(int C = R; C <= 4; C++)
	{
	  if(R*C < X)
	    ans = "RICHARD";
	  else if((R*C)%X != 0)
	    ans = "RICHARD";
	  else
	    {
	      if(X <= 2)
		ans = "GABRIEL";
	      else if(X == 3)
		{
		  if(R*C == 3)
		    ans = "RICHARD";
		  else
		    ans = "GABRIEL";
		}
	      else
		{
		  if(R*C == 12 || R*C == 16)
		    ans = "GABRIEL";
		  else
		    ans = "RICHARD";
		}
	    }

	  cout << "Ans: " << ans << endl;
	}

  return 0;
}
