#include <iostream>
#include <fstream>
#include <array>
#include <exception>
#include <set>

struct matrix_t
{
   static const size_t size = 4;

   matrix_t(std::ifstream & in)
   {
      for (size_t i = 0; i < size * size; ++i)
         in >> arr[i];
   }

   int operator() (size_t i, size_t j)
   {
      return arr[i * size + j];
   }

private:
   std::array<int, size * size> arr;
};

enum class Answer { NOT_FOUND, NUMBER, BAD_MAGICIAN };

int main()
{
   std::ifstream in("A-small-attempt0.in");
   std::ofstream out("output.txt");
   int t;
   in >> t;
   for (int q = 1; q <= t; ++q)
   {
      int first_ans;
      in >> first_ans;
      --first_ans;
      matrix_t first(in);
      int second_ans;
      in >> second_ans;
      --second_ans;
      matrix_t second(in);
      std::set<int> row;
      for (size_t j = 0; j < first.size; ++j)
         row.insert(first(first_ans, j));
      Answer ans = Answer::NOT_FOUND;
      int ans_num;
      for (size_t j = 0; j < second.size; ++j)
         if (row.find(second(second_ans, j)) != row.end())
         {
            if (ans == Answer::NOT_FOUND)
            {
               ans = Answer::NUMBER;
               ans_num = second(second_ans, j);
            }
            else
            {
               ans = Answer::BAD_MAGICIAN;
               break;
            }
         }
      out << "Case #" << q << ": ";
      switch (ans)
      {
      case Answer::NOT_FOUND:
         out << "Volunteer cheated!";
         break;
      case Answer::NUMBER:
         out << ans_num;
         break;
      case Answer::BAD_MAGICIAN:
         out << "Bad magician!";
         break;
      default:
         break;
      }
      out << std::endl;
   }
   return 0;
}

