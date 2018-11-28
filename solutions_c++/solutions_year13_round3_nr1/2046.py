/*
 * Problem-A-Consonants.cpp
 *
 *  Created on: 12.05.2013
 *      Author: XStalkerX
 */

#include <fstream>
#include <iostream>

#include <set>

class SubStr
{
public:
  int a_;
  int b_;

  SubStr (int a, int b) :
    a_(a), b_(b)
  {  }

  bool operator< (const SubStr& op) const
  {
    if (a_ < op.a_)
      return true;

    if (a_ == op.a_ and b_ < op.b_)
      return true;

    return false;
  }
};

int getNValue (const std::string& name, int n)
{
  std::set<char> vowels;
  vowels.insert('a');
  vowels.insert('e');
  vowels.insert('i');
  vowels.insert('o');
  vowels.insert('u');

  std::set<SubStr> all;
  std::set<SubStr> groups;
  for (int i = 0; i < name.size() - n + 1; ++i)
  {
    bool is_group = true;
    for (int c = i; c < i + n; ++c)
    {
      if (vowels.find(name[c]) != vowels.end())
      {
        is_group = false;
        break;
      }
    }

    if (is_group)
      groups.insert(SubStr(i, i + n - 1));
  }


  for (std::set<SubStr>::iterator it = groups.begin();
       it != groups.end();
       ++it)
  {
    for (int left = 0; left <= it->a_; ++left)
      for (int right = name.size() - 1; right >= it->b_; --right)
      {
        all.insert(SubStr(left, right));
      }
  }
  return all.size();
}

int main (int argc, char* argv[])
{
  if (argc != 2)
  {
    std::cout << "No file" << std::endl;
    return 0;
  }

  std::ifstream input (argv[1], std::fstream::in);
  if (!input.is_open())
  {
    std::cout << "Can't read" << std::endl;
    return -1;
  }

  std::ofstream output ("Consonants.out", std::fstream::out);
  if (!output.is_open())
  {
    std::cout << "Can't write" << std::endl;
    return -1;
  }

  /* scroll example:
    4
    quartz 3
    straight 3
    gcj 2
    tsetse 2
  */

  int cases_num = 0;
  input >> cases_num;

  char c;
  std::string name;
  int n;

  // for each test case
  for (int i = 1; i <= cases_num; ++i)
  {
    input >> c;
    while (c != ' ')
    {
      name += c;
      input >> std::noskipws >> c;
    }
    input >> std::skipws >> n;

    output << "Case #" << i << ": " << getNValue(name, n) << std::endl;
    std::cout << "Case #" << i << ": " << getNValue(name, n) << std::endl;
//    std::cout << name << " " << n;
    name.clear();
  }

  input.close();
  output.close();
}

