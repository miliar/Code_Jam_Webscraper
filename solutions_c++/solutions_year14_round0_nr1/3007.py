#include <iostream>
#include <fstream>

const int N = 4;

int main(int argc, char *argv[])
{
  if (argc < 2) {
    std::cout << "Usage: magic_trick [input_file]" << std::endl;
    return 0;
  }

  const char * filename = argv[1];  

  std::ifstream in(filename);
  if(!in.is_open()){
    std::cout << "error opening file " << filename << std::endl;
    return -1;
  }

  std::ofstream out("out.txt");
  if(!out.is_open()){
    std::cout << "error creating output file" << std::endl;
    return -2;
  }

  int test_numbers = 0;
  in >> test_numbers;

  for (int i = 0; i < test_numbers; ++i) {
    int temp;
    int first_row = 0;
    int numbers[N] = {0};
    in >> first_row;
    for (int row = 0; row < N; ++row) {
      if (row == first_row - 1){
        for (int index = 0; index < N; ++index) 
          in >> numbers[index];
      } else {
        for (int k = 0;  k < N; ++k)
         in >> temp;
      }
    }

    //    std::cout << numbers[0] << " " << numbers[1] << " " << numbers[2] << " " << numbers[3] << std::endl;

    int second_row = 0;
    int numbers_in_row = 0;
    int answer = 0;
    in >> second_row;
    for (int row = 0; row < N; ++row) {
      if (row == second_row - 1) {
        int num = 0;
        for (int nindex = 0; nindex < N; ++nindex) {
          in >> num;
          for (int k = 0; k < N; ++k) {
	    if (num == numbers[k]) {
              answer = num;
              ++numbers_in_row;
            }
	  }
        }
      } else {
        for (int k = 0; k < N; ++k)
          in >> temp;	  
      }
    }

    out << "Case #" << i+1 << ": ";
    switch(numbers_in_row){
    case 0: 
      out << "Volunteer cheated!";
      break;
    case 1:
      out << answer;
      break;
    default:
      out << "Bad magician!";
      break;
    }
    out << std::endl;
  
  }


  return 0;
}
