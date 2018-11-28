#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string find_number(std::string s)
  {
  std::vector<long> letters(26, 0);
  for (size_t i = 0; i < s.size(); ++i)
    ++letters[s[i] - 'A'];

  std::vector<long> result(10, 0);

  // ZERO Z
  for (int i = 0; i < letters[25]; ++i)
    {
    --letters[4]; --letters[17]; --letters[14]; ++result[0];
    }
  letters[25] = 0;
  // TWO W
  for (int i = 0; i < letters[22]; ++i)
    {
    --letters[19]; --letters[14]; ++result[2];
    }
  letters[22] = 0;
  // SIX X
  for (int i = 0; i < letters[23]; ++i)
    {
    --letters[18]; --letters[8]; ++result[6];
    }
  letters[23] = 0;
  // EIGHT G
  for (int i = 0; i < letters[6]; ++i)
    {
    --letters[4]; --letters[8]; --letters[7]; --letters[19]; ++result[8];
    }
  letters[6] = 0;
  // THREE H
  for (int i = 0; i < letters[7]; ++i)
    {
    --letters[19]; --letters[17]; --letters[4]; --letters[4]; ++result[3];
    }
  letters[7] = 0;
  // FOUR R
  for (int i = 0; i < letters[17]; ++i)
    {
    --letters[5]; --letters[14]; --letters[20]; ++result[4];
    }
  letters[17] = 0;
  // FIVE F
  for (int i = 0; i < letters[5]; ++i)
    {
    --letters[8]; --letters[21]; --letters[4]; ++result[5];
    }
  letters[5] = 0;
  // ONE O
  for (int i = 0; i < letters[14]; ++i)
    {
    --letters[13]; --letters[4]; ++result[1];
    }
  letters[14] = 0;
  // SEVEN S
  for (int i = 0; i < letters[18]; ++i)
    {
    --letters[4]; --letters[21]; --letters[4]; --letters[13]; ++result[7];
    }
  letters[18] = 0;
  // NINE I
  for (int i = 0; i < letters[8]; ++i)
    {
    --letters[13]; --letters[13]; --letters[4]; ++result[9];
    }
  letters[8] = 0;
  // 0 1 2 3 4 5 6 7 8 9 10	11 12	13	14	15	16	17	18	19	20	21  22	23	24	25
  // A B C D E F G H I J K  L  M  N   O   P   Q   R   S   T   V   U   W   X   Y   Z

  std::string s_result;
  for (size_t i = 0; i < 10; ++i)
    for (size_t j = 0; j < result[i]; ++j)
      s_result += std::to_string(i);

  return s_result;
  }

int main()
  {
  long n;
  
  std::ifstream fin(L"A-large.in");
  std::ofstream fout(L"A-large.out");
  std::istream& in = fin;
  std::ostream& out = fout;
  
  /*
  std::istream& in = std::cin;
  std::ostream& out = std::cout;
  */
  in >> n;
  for (long i = 1; i <= n; ++i)
    {
    std::string s;
    in >> s;
    out << "Case #" << i << ": " << find_number(s) << std::endl;
    }

  return 0;
  }