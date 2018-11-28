#include <signal.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
#include <stdarg.h>

#include <limits>
#include <ostream>
#include <istream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>
#include <numeric> 
#include <memory>


int Lawn[128][128];

int GetRow(int* Cell)
{
     int* Beg = &Lawn[0][0];
     return (Cell - Beg) / 128;
}


int GetColumn(int* Cell)
{
     int* Beg = &Lawn[0][0];
     return (Cell - Beg) % 128;
}

class TestCase
{
     int mID;
     int mColumns;
     int mRows;
     std::vector<int> mMinimalGrassLevelForColumns;
     std::vector<int> mMinimalGrassLevelForRows;
     bool IsPossible() const {
	  for (int r = 0; r < mColumns; r++)
	  {
	       for (int c = 0; c < mRows; c++)
	       {
		    int t = Lawn[r][c];
		    if (t < mMinimalGrassLevelForColumns[c] &&
			t < mMinimalGrassLevelForRows[r])
		    {
			 return false;
		    }
	       }
	  }
	  return true;
     }
public:
     TestCase(int ID, std::istream& fin)
	  : mID(ID)
	  , mMinimalGrassLevelForColumns(128, 0)
	  , mMinimalGrassLevelForRows(128, 0) {
	  fin >> mColumns;
	  fin >> mRows;
	  
	  for (int r = 0; r < mColumns; r++)
	  {
	       for (int c = 0; c < mRows; c++)
	       {
		    int tmp;
		    fin >> tmp;
		    Lawn[r][c] = tmp;
		    mMinimalGrassLevelForRows[r] = std::max(mMinimalGrassLevelForRows[r], tmp);
		    mMinimalGrassLevelForColumns[c] = std::max(mMinimalGrassLevelForColumns[c], tmp);
	       }
	  }
     }
     void EvalAndPrint() const {
	  std::cout << "Case #" << mID << ": ";
	  if (IsPossible())
	  {
	       std::cout << "YES";
	  }
	  else
	  {
	       std::cout << "NO";
	  }
	  std::cout << std::endl;
     }
     void Dump() const {
	  std::cerr << mID << std::endl;
	  for (int c = 0; c < mRows; c++)
	  {
	       std::cerr << "   " << mMinimalGrassLevelForColumns[c];
	  }
	  std::cerr << std::endl;
	  for (int r = 0; r < mColumns; r++)
	  {
	       for (int c = 0; c < mRows; c++)
	       {
		    std::cerr <<  Lawn[r][c] << " (" << GetRow(&Lawn[r][c]) << "," << GetColumn(&Lawn[r][c]) << ")   ";
	       }
	       std::cerr << " - " << mMinimalGrassLevelForRows[r] <<  std::endl;
	  }
	  
     }
};

int main()
{
     int TCNum;
     std::cin >> TCNum;
     for (int i = 1; i <= TCNum; i++)
     {
	  TestCase TC(i, std::cin);
	  TC.EvalAndPrint();
     }
     return 0;
}
