#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::fstream;
using std::map;
using std::stringstream;
using std::string;
using std::vector;

int main(int argc, char *argv[])
{
  fstream fs("input.txt", fstream::in);
  fstream fout("output.txt", fstream::out);

  if (fs.good())
  {
    int case_amount = 0;
    string line = "";

    getline(fs, line);
    stringstream stream(line);
    stream >> case_amount;
    
    for (int i = 0; i < case_amount; ++i)
    {
      string first_numbers = "";
      {
        string first_row_str = "";
        getline(fs, first_row_str);      
        stringstream stream(first_row_str);

        int first_row = 0;
        stream >> first_row;

        for ( int j = 0; j < 4; ++j)
        {
          string line = "";
          getline(fs, line);
          if (1 + j == first_row)
          {
            first_numbers = line;
          }
        }
      }

      string second_numbers = "";
      {
        string first_row_str = "";
        getline(fs, first_row_str);      
        stringstream stream(first_row_str);

        int first_row = 0;
        stream >> first_row;

        for ( int j = 0; j < 4; ++j)
        {
          string line = "";
          getline(fs, line);
          if (1 + j == first_row)
          {
            second_numbers = line;
          }
        }
      }

      vector<int> first_vec;
      {
        stringstream stream(first_numbers);
        for (int j = 0; j < 4; ++j)
        {
          int temp = 0;
          stream >> temp;
          first_vec.push_back(temp);
        }
      }
      
      vector<int> second_vec;
      {
        stringstream stream(second_numbers);
        for (int j = 0; j < 4; ++j)
        {
          int temp = 0;
          stream >> temp;
          second_vec.push_back(temp);
        }
      }

      bool first_find = false;
      bool second_find = false;
      int n = 0;

      for (int j = 0; j < 4; ++j)
      {
        for (int k = 0; k < 4; ++k)
        {
          if (first_vec[j] == second_vec[k])
          {
            if (!first_find)
            {
              first_find = true;
              n = first_vec[j];
            }
            else
            {
              second_find = true;
              break;
            }
          }
        }
      }

      string result = "";
      if (!first_find)
      {
        result = "Volunteer cheated!";
      }
      else if (first_find && !second_find)
      {
        stringstream stream;
        stream << n;
        stream >> result;
      }
      else
      {
        result = "Bad magician!";
      }
      
      fout << "Case #" << 1 + i << ": " << result << endl;
    }

  }

  fs.close();
  fout.close();
  
  return 0;
}
