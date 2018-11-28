#include <set>
#include <vector>
#include <iostream>

void readSet(std::set<int>& s)
{
  for(int j = 0; j < 4; ++j)
  {
    int n;
    std::cin >> n;
    s.insert(n);
  }
}

void printSet(const std::set<int>& s)
{
  for(std::set<int>::const_iterator pos = s.begin(); pos != s.end(); ++pos)
  {
    std::cout << *pos << " ";
  }
  std::cout << std::endl;
}

int main()
{
  int t;
  std::cin >> t;
  std::set<int> tmp;
  for(int ti = 0; ti < t; ++ti)
  {
    int chosen1;
    std::cin >> chosen1;
    //std::cout << "chosen1 : " << chosen1 << std::endl;
    std::set<int> s1;
    for(int i = 0; i < 4; ++i)
    {
      tmp.clear();
      readSet(tmp);
      if(i+1 == chosen1)
        s1 = tmp;
    }
    //printSet(s1);
    int chosen2;
    std::cin >> chosen2;
    //std::cout << "chosen2 : " << chosen2 << std::endl;
    std::set<int> s2;
    for(int i = 0; i < 4; ++i)
    {
      tmp.clear();
      readSet(tmp);
      if(i+1 == chosen2)
        s2 = tmp;
    }
    //printSet(s2);
    int match = -1;
    bool dupFound = false;
    for(std::set<int>::const_iterator pos = s1.begin(); pos != s1.end(); ++pos)
    {
      if(s2.find(*pos) != s2.end())
      {
        if(match == -1)
          match = *pos;
        else
        {
          dupFound = true;
          break;
        }
      }
    }  
    if(dupFound)
      std::cout << "Case #" << (ti + 1) << ": Bad magician!" << std::endl;
    else if(match == -1)
      std::cout << "Case #" << (ti + 1) << ": Volunteer cheated!" << std::endl;
    else
      std::cout << "Case #" << (ti + 1) << ": " << match << std::endl;
  }
}

