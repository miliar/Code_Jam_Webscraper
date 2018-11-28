#include "test.hh"
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <iostream>

Test::Test(std::vector<int> audience)
     : audience_(audience)
{}

long Test::find_min()
{
  unsigned shyness = 0;
  long nb_people = 0;
  for (unsigned i = 0; i < audience_.size(); ++i)
  {
    if (i > shyness)
    {
      nb_people++;
      shyness++;
    }
    shyness += audience_[i];
  }
  return nb_people;
}
