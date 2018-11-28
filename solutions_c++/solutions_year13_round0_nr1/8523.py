#include <fstream>

using namespace std;

struct board_t
{
   char data_[4][4];

   unsigned int res; // 0 - draw; 1 - x; 2 - o; 3 - otherwise;
};

int main()
{
   unsigned int test_cnt = 0;

   ifstream in;
   ofstream out;

   in.open ("file.in") ;
   out.open("file.out");

   in >> test_cnt;

   unsigned int column_cnt = test_cnt * 5 - 1;

   board_t * input = new board_t[test_cnt];

   for (unsigned int k = 0; k < test_cnt; ++k)
   {
      for (unsigned int i = 0; i < 4; ++i)
         for (unsigned int j = 0; j < 4; ++j)
            in >> input[k].data_[i][j];
   }

   bool have_empty, have_solution = false;

   unsigned int x_h, o_h, x_w[4], o_w[4], x_d, o_d, x_id, o_id;

   for (unsigned int k = 0; k < test_cnt; ++k)
   {
      have_empty = false;

      for (int i = 0; i < 4; ++i)
      {
         x_w[i] = 0;
         o_w[i] = 0;
      }

      x_d = 0;
      o_d = 0;

      x_id = 0;
      o_id = 0;

      for (int i = 0; i < 4; ++i)
      {
         x_h = 0;
         o_h = 0;

         have_solution = false;

         for (int j = 0; j < 4; ++j)
         {
            if (input[k].data_[i][j] == 'X' || input[k].data_[i][j] == 'T')
            {
               x_h++;

               x_w[j]++;

               if (i == j)
                  x_d++;
               else if (i + j == 3)
                  x_id++;
            }
            else if (input[k].data_[i][j] == 'O' || input[k].data_[i][j] == 'T')
            {
               o_h++;

               o_w[j]++;

               if (i == j)
                  o_d++;
               else if (i + j == 3)
                  o_id++;
            }
            else if (input[k].data_[i][j] == '.')
               have_empty = true;
         }

         if (x_h > 3)
         {
            input[k].res = 1;
            have_solution = true;
            break;
         }
         else if (o_h > 3)
         {
            input[k].res = 2;
            have_solution = true;
            break;
         }
      }

      if (!have_solution)
      {
         if ((x_d > 3) || (x_id > 3) || (x_w[0] > 3) || (x_w[1] > 3) || (x_w[2] > 3) || (x_w[3] > 3))
            input[k].res = 1;
         else if ((o_d > 3) || (o_id > 3) || (o_w[0] > 3) || (o_w[1] > 3) || (o_w[2] > 3) || (o_w[3] > 3))
            input[k].res = 2;
         else if (have_empty)
            input[k].res = 3;
         else
            input[k].res = 0;
      }
   }

   for (unsigned int i = 0; i < test_cnt; ++i)
   {
      if (input[i].res == 0)
         out << "Case #" << i + 1 << ": Draw" << endl;
      else if (input[i].res == 1)
         out << "Case #" << i + 1<< ": X won" << endl;
      else if (input[i].res == 2)
         out << "Case #" << i + 1<< ": O won" << endl;
      else if (input[i].res == 3)
         out << "Case #" << i + 1<< ": Game has not completed" << endl;
   }

   return 0;
}