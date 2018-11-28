#include <iostream>
#include <string>

int main()
{
   const size_t field_area_size = 4;

   size_t num_of_tests;

   size_t  square_line1[field_area_size]
          ,square_line2[field_area_size];

   std::cin >> num_of_tests;

   size_t pos1, pos2;

   size_t tmp_num;

   size_t cart_value;

   size_t compare_num;

   size_t compare_idx;

   for (size_t k = 0; k < num_of_tests; ++k)
   {
      std::cin >> pos1;

      for (size_t i = 0; i < pos1 - 1; ++i)
         for (size_t j = 0; j < field_area_size; ++j)
            std::cin >> tmp_num;

      for (size_t i = 0; i < field_area_size; ++i)
         std::cin >> square_line1[i];

      for (size_t i = 0; i < 4 - pos1; ++i)
         for (size_t j = 0; j < field_area_size; ++j)
            std::cin >> tmp_num;

      std::cin >> pos2;

      compare_num = 0;

      for (size_t i = 0; i < pos2 - 1; ++i)
         for (size_t j = 0; j < field_area_size; ++j)
            std::cin >> tmp_num;

      for (size_t i = 0; i < field_area_size; ++i)
         std::cin >> square_line2[i];

      for (size_t i = 0; i < field_area_size; ++i)
         for (size_t j = 0; j < field_area_size; ++j)
         {
            if (square_line1[i] == square_line2[j])
            {
               compare_num++;
               compare_idx = i;
            }
         }

      for (size_t i = 0; i < 4 - pos2; ++i)
         for (size_t j = 0; j < field_area_size; ++j)
            std::cin >> tmp_num;

      std::cout << "Case #" << k + 1<< ": ";

      if (!compare_num)
         std::cout << "Volunteer cheated!";
      else if (compare_num == 1)
         std::cout << square_line1[compare_idx];
      else
         std::cout << "Bad magician!";

      std::cout << "\n";
   }

   return 0;
}